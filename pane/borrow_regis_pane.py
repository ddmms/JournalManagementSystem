from PyQt5.Qt import *
from UI.borrow_registration import Ui_MainWindow
import sys
from databaselink2 import connect

# 注：以下的日期均为字符串类型，而非日期类型，必要时请转换


class BorrowRegisPane(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("期刊管理系统")
        self.mode = "borrow_regis"
        self.setupUi(self)
        self.retranslateUi(self)

    def Return(self):
        self.return_signal.emit(self.mode)

    def Borrow_regis(self):
        print("I'm in borrow!")
        input_objects = [self.reader_no, self.journal_name, self.year, self.volume, self.number, self.borrow_date]
        for input_object in input_objects:
            if input_object.text() == '':
                QMessageBox.warning(self, "登记提示", "录入信息不完整！请重试",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                return
        record = [input_object.text() for input_object in input_objects]

        insert_success = connect.borrow_register(record)
        if insert_success:
            QMessageBox.information(self, "登记提示", "登记成功！",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, "登记提示", "登记失败！请重试",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(record)

    def Return_regis(self):
        print("I'm in return!")
        input_objects = [self.reader_no, self.journal_name, self.year, self.volume, self.number, self.return_date]
        for input_object in input_objects:
            if input_object.text() == '':
                QMessageBox.warning(self, "登记提示", "录入信息不完整！请重试",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                return
        record = [input_object.text() for input_object in input_objects]
        # 需要根据record中的期刊号和读者号找到数据库相应记录，并填入归还日期

        insert_success = connect.return_register(record)
        if insert_success:
            QMessageBox.information(self, "登记提示", "登记成功！",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, "登记提示", "登记失败！请重试",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(record)

    return_signal = pyqtSignal(str)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = BorrowRegisPane()
    window.show()

    sys.exit(app.exec_())
