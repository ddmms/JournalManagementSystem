from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import pymysql
from datetime import date
import time


class LinkDatabaseInMysql:
    def __init__(self, username, pass_word):
        self.connection = pymysql.connect(
            host='localhost',
            port=3306,
            user=username,
            password=password,
            db='journaldatabase',
            charset='utf8mb4'
        )
        self.cur = self.connection.cursor()
        print('登录成功')

    # 查询语句返回结果
    def select_sql(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result)
        return result

    # 更新、删除、插入时的sql语句调用
    def update_sql(self, sql: str):
        try:
            self.cur.execute(sql)
            self.connection.commit()
            print(sql.split(' ')[0] + '语句执行成功')
            return True
        except pymysql.Error as e:
            print(sql.split(' ')[0] + '语句执行失败')
            print(e.args[0], e.args[1])
            self.connection.rollback()
            return False

    def update_sql_with_data(self, sql: str, data):
        try:
            self.cur.execute(sql, data)
            self.connection.commit()
            print(sql.split(' ')[0] + '语句执行成功')
            return True
        except pymysql.Error as e:
            print(sql.split(' ')[0] + '语句执行失败')
            print(e.args[0], e.args[1])
            self.connection.rollback()
            return False

    # 登录验证
    def check_log_in(self, account, pwd, mode):
        isValidate = False
        if account == "":
            feedback = "请输入账号！"
            return isValidate, feedback
        if pwd == "":
            feedback = "请输入密码！"
            return isValidate, feedback
        if mode == "":
            feedback = "请选择账户类型！"
            return isValidate, feedback
        table = "administer" if mode == "admin" else "reader"
        account_attribute = "ANO" if mode == "admin" else "RNO"
        sql = "select * from %s where %s = '%s';" % (table, account_attribute, account)
        result = self.select_sql(sql)
        if len(result) == 0:
            feedback = "账号错误！请重新输入"
            return isValidate, feedback
        if result[0][2] != pwd:
            feedback = "密码错误！请重新输入"
            return isValidate, feedback
        isValidate = True
        feedback = "账号密码正确！"

        return isValidate, feedback

    # 读者功能方法
    def borrow_inquiry(self, reader_no):
        # 进行查询
        sql = '''select JNAME, YEAR, VOLUME, NUMBER, BORROWTIME, RETURNTIME is not null AS isRETURN 
                 from borrow, journalregister
                 where borrow.JNO = journalregister.JNO and
                       borrow.RNO = '%s';''' % reader_no
        result = self.select_sql(sql)
        return result

    def borrow_inquiry_with_condition(self, reader_no):
        # 进行未归还借阅查询
        sql = '''select JNAME, YEAR, VOLUME, NUMBER, BORROWTIME, RETURNTIME is not null AS isRETURN 
                 from borrow, journalregister
                 where borrow.JNO = journalregister.JNO and
                       borrow.RETURNTIME is null and borrow.RNO = '%s';''' % reader_no
        result = self.select_sql(sql)
        return result

    def journal_inquiry(self, keyword):
        sql = '''select JNAME, YEAR, VOLUME, NUMBER, PAPERTITLE, AUTHOR, PAGES
                                         from journalcontent, journalregister
                                         where journalcontent.JNO = journalregister.JNO and
                                               (journalcontent.KEYWORD1 = '%s' or 
                                               journalcontent.KEYWORD2 = '%s' or
                                               journalcontent.KEYWORD3 = '%s' or
                                               journalcontent.KEYWORD4 = '%s' or
                                               journalcontent.KEYWORD5 = '%s');''' % \
              (keyword, keyword, keyword, keyword, keyword)
        result = self.select_sql(sql)
        return result

    def book(self, record):
        journal_name = record[1]
        year = int(record[2])
        volume = int(record[3])
        number = int(record[4])

        # 检查待预定期刊是否存在
        journal_whether_exist_sql = """select JNO
                                     from journalregister
                                     where JNAME="%s" and YEAR=%d and VOLUME=%d and NUMBER=%d """ % \
                                    (journal_name, year, volume, number)
        journal_exist_result = connect.select_sql(journal_whether_exist_sql)
        if len(journal_exist_result) == 0:
            result, feedback = False, "NotExist"
            return result, feedback

        # 检查待预定期刊借阅情况
        journal_no = journal_exist_result[0][0]
        borrowed_jno = connect.select_sql('''select JNO 
                                             from borrow
                                             where RETURNTIME is NULL;''')
        if journal_exist_result[0] not in borrowed_jno:
            result, feedback = False, "ReadyToBorrow"
            return result, feedback

        current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        insert_subscribe_sql = """ insert into subscribe(`RNO`,`JNO`,`APPOINTTIME`) values(%s,%s,%s)"""
        data = [record[0], journal_no, current_time]
        insert_result = self.update_sql_with_data(insert_subscribe_sql, data)
        feedback = "Ok"
        return insert_result, feedback

    def get_maxJNO(self):
        sql = "select JNO from journalregister"
        JNOs = self.select_sql(sql)
        maxJNO = max([int(i[0]) for i in JNOs]) + 1
        return maxJNO

    # 管理员功能方法
    def instock_register(self, instocks):
        for i in range(len(instocks)):
            it = instocks[i]
            x = self.get_maxJNO()
            y = [x]
            data = y + it
            sql = '''INSERT INTO journalregister(JNO, JNAME, YEAR, VOLUME, NUMBER) VALUES (%s, %s, %s, %s, %s)'''
            if not self.update_sql_with_data(sql, data):  # 返回数据库插入操作是否成功
                return False
        return True

    def catalog_register(self, catalogs):
        for i in range(len(catalogs)):
            data = catalogs[i]
            # print(data)
            sql = '''INSERT INTO journallist(JNAME,ISSN,CN,POSTCODE,CIRCLE,ADDRESS,SECTION) 
            VALUES(%s,%s,%s,%s,%s,%s,%s)'''
            if not self.update_sql_with_data(sql, data):
                return False
        return True

    def get_JNO(self, journal_name, year, volume, number):
        print("In getJNO!")
        find_jno_sql = '''select JNO
                          from journalregister
                          where JNAME='%s' and YEAR=%d and VOLUME=%d and NUMBER=%d;''' % \
                       (journal_name, year, volume, number)
        journal_no = self.select_sql(find_jno_sql)
        if len(journal_no) == 0:
            return None
        return journal_no[0][0]

    def content_register(self, contents):
        for i in range(len(contents)):
            p = contents[i]
            journal_name = p[0]
            year = int(p[1])
            volume = int(p[2])
            number = int(p[3])
            journal_no = self.get_JNO(journal_name, year, volume, number)
            if journal_no is None:
                return False
            data = [journal_no] + p[4:]
            sql = '''INSERT INTO journalcontent
            (JNO,PAPERTITLE,AUTHOR,KEYWORD1,KEYWORD2,KEYWORD3,KEYWORD4,KEYWORD5,PAGES) 
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            if not self.update_sql_with_data(sql, data):
                return False
        return True

    def borrow_register(self, record):
        reader_no = record[0]
        journal_name = record[1]
        year = int(record[2])
        volume = int(record[3])
        number = int(record[4])
        borrow_date = record[5]
        journal_no = self.get_JNO(journal_name, year, volume, number)
        if journal_no is None:
            return False
        insert_sql = '''insert
                        into borrow
                        values ('%s', '%s', '%s', NULL);''' % (reader_no, journal_no, borrow_date)
        insert_result = self.update_sql(insert_sql)
        return insert_result

    def return_register(self, record):
        reader_no = record[0]
        journal_name = record[1]
        year = int(record[2])
        volume = int(record[3])
        number = int(record[4])
        return_date = record[5]
        journal_no = self.get_JNO(journal_name, year, volume, number)
        if journal_no is None:
            return False
        update_sql = '''update borrow
                        set RETURNTIME = '%s'
                        where RNO = '%s' and JNO = '%s' ;''' % (return_date, reader_no, journal_no)
        update_result = self.update_sql(update_sql)
        return update_result

    def whereabouts_inquiry(self, jno):
        check_in_journal_sql = """select JNO
                                        from journalregister
                                        where JNO="%s" """ \
                                     % jno
        check_in_result = connect.select_sql(check_in_journal_sql)
        if len(check_in_result) == 0:
            result, feedback = [], "NotExist"
            return result, feedback

        destination_sql = """select reader.RNO,reader.RNAME,
                            timestampdiff(day,borrow.BORROWTIME,ifnull(borrow.RETURNTIME,now())),
                            borrow.BORROWTIME,
                            ifnull(borrow.RETURNTIME,now())
                            from reader,borrow
                            where reader.RNO=borrow.RNO and borrow.JNO="%s" """ \
                          % jno
        result = connect.select_sql(destination_sql)
        feedback = "Ok"
        return result, feedback

    def subscribe(self, old_subscribes, new_subscribes):
        d = date.today()
        year = d.year + 1  # 年份

        row_count = len(old_subscribes)
        for row in range(row_count):
            amount = int(old_subscribes[row][2])
            sql = '''INSERT INTO `order`(JNAME,YEAR,AMOUNT) VALUES ("%s",%d,%d);''' % \
                  (old_subscribes[row][0], year, amount)
            if not self.update_sql(sql):
                return False

        row_count = len(new_subscribes)
        for row in range(row_count):
            third = int(new_subscribes[row][3])
            sql2 = '''INSERT INTO `order`(JNAME,YEAR,AMOUNT) VALUES ("%s",%d,%d);''' % \
                   (new_subscribes[row][0], year, third)
            if not self.update_sql(sql2):
                return False
        return True


class LinkDatabaseInPyQt:
    def login(self, username, password):
        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('journaldatabase')
        self.db.setUserName(username)
        self.db.setPassword(password)
        if not self.db.open():
            print(self.db.lastError().text())
        else:
            print('登录成功')

    def get_all_table_names(self):
        print(self.db.tables())

    # 执行selectsql语句返回查询结果
    def selectsql(self, sql):
        query = QSqlQuery(sql)
        while query.next():
            print(query.value(0))

    # 执行删除、插入、更新语句
    def changesql(self, sql):
        pass


user = 'root'
password = 'zhangweikuo1997+'
connect = LinkDatabaseInMysql(user, password)


if __name__ == "__main__":
    rno = input("please input reader no: ")
    print("output:")
    if len(rno) != 9:
        print("illegal reader no")
    else:
        result = connect.borrow_inquiry(rno)
        if len(result) == 0:
            print("the reader hasn't borrowed a journal!")
        else:
            print("the borrow results are above.")
