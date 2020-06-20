from PyQt5.Qt import *
from UI.subscription import Ui_MainWindow
import sys
from databaselink2 import connect


class SubscribePane(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("期刊管理系统")
        self.mode = "subscribe"
        self.setupUi(self)
        self.retranslateUi(self)
        self.showExistedJournal()

    def Return(self):
        self.return_signal.emit(self.mode)

    def showExistedJournal(self):
        sql = "select JNAME, ISSN from journallist;"
        existedJournal = connect.select_sql(sql)
        self.old_select.setRowCount(len(existedJournal))
        for i in range(len(existedJournal)):
            record = existedJournal[i]
            journal_name = QTableWidgetItem(str(record[0]))
            self.old_select.setItem(i, 0, journal_name)
            issn = QTableWidgetItem(str(record[1]))
            self.old_select.setItem(i, 1, issn)
            select = QTableWidgetItem()
            select.setCheckState(Qt.Unchecked)
            self.old_select.setItem(i, 2, select)

    # 生成征订表提交
    def Submit(self):
        # 从已有期刊选择进行征订
        old_subscribes = []  # 选择已有期刊的征订
        row_count = self.old_select.rowCount()
        for row in range(row_count):
            if self.old_select.item(row, 0) is None:
                continue
            journal_name = self.old_select.item(row, 0).text()     # 期刊名
            issn = self.old_select.item(row, 1).text()             # issn号
            isSelected = self.old_select.item(row, 2).checkState()  # 是否选中
            if isSelected:
                amount = self.old_select.item(row, 3)  # 征订数量
                if amount is None:
                    QMessageBox.warning(self, "征订提示", "录入信息不完整！请重试",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    return
                amount = amount.text()
                old_subscribes.append([journal_name, issn, amount])  # 逐条选中记录添加
        print(old_subscribes)

        # 新征订的期刊
        new_subscribes = []
        row_count = self.new_select.rowCount()
        column_count = self.new_select.columnCount()
        for row in range(row_count):
            if self.new_select.item(row, 0) is None:
                continue
            new_subscribe = []
            for col in range(column_count):
                item = self.new_select.item(row, col)
                if item is None:
                    QMessageBox.warning(self, "征订提示", "录入信息不完整！请重试",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    return
                new_subscribe.append(item.text())
            new_subscribes.append(new_subscribe)  # 逐条记录添加
        print(new_subscribes)

        operation_success = connect.subscribe(old_subscribes, new_subscribes)  # 功能函数的调用

        if operation_success:
            QMessageBox.information(self, "征订提示", "征订成功！",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, "征订提示", "征订失败！请重试",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    return_signal = pyqtSignal(str)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SubscribePane()
    window.show()

    sys.exit(app.exec_())
