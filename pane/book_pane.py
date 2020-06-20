from PyQt5.Qt import *
from UI.book_and_inquiry import Ui_MainWindow
import sys
from databaselink2 import connect
from datetime import date


class BookPane(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("期刊管理系统")
        self.mode = "book"
        self.setupUi(self)
        self.retranslateUi(self)

    def Return(self):
        self.return_signal.emit(self.mode)

    # 预定的提交
    def Book(self):
        #rno = "D11714004"
        rno=self.property("rno")
        journal_name = self.journal_name.text()
        year = self.year.text()
        volume = self.volume.text()
        number = self.issue.text()
        record = [rno, journal_name, year, volume, number]
        insert_success, feedback = connect.book(record)
        print(feedback)
        if feedback == "NotExist":
            QMessageBox.information(self, "预定提示", "该期刊不存在！",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        if feedback == "ReadyToBorrow":
            QMessageBox.information(self, "预定提示", "当前期刊无需预定！可直接借阅",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        if not insert_success:
            QMessageBox.information(self, "预定提示", "预定失败！请重试",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        self.showbookedJournal()

    def showbookedJournal(self):
        #rno = "D11714004"
        rno=self.property("rno")
        sql = '''select JNAME, YEAR, VOLUME, NUMBER, APPOINTTIME
                 from subscribe, journalregister
                 where subscribe.JNO=journalregister.JNO and
                       subscribe.RNO='%s';''' % rno
        bookedJournal = connect.select_sql(sql)
        self.booked_journal.setRowCount(len(bookedJournal))
        for i in range(len(bookedJournal)):
            record = bookedJournal[i]
            for j in range(len(record)):
                newItem = QTableWidgetItem(str(record[j]))
                self.booked_journal.setItem(i, j, newItem)

    return_signal = pyqtSignal(str)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = BookPane()
    window.show()

    sys.exit(app.exec_())
