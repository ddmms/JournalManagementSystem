from PyQt5.Qt import *
from UI.instock_registration import Ui_MainWindow
import sys
from databaselink2 import connect


class InstockPane(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("期刊管理系统")
        self.mode = "instock"
        self.setupUi(self)
        self.retranslateUi(self)

    def Return(self):
        self.return_signal.emit(self.mode)

    # 提交按钮对应的槽函数，请完善
    def Submit(self):
        row_count = self.new_instock.rowCount()
        column_count = self.new_instock.columnCount()
        instocks = []  # 入库登记内容
        for row in range(row_count):
            if self.new_instock.item(row, 0) is None:
                continue
            instock = []
            for col in range(column_count):
                item = self.new_instock.item(row, col)
                if item is None:
                    QMessageBox.warning(self, "登记提示", "录入信息不完整！请重试",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    return
                instock.append(item.text())
            instocks.append(instock)  # 逐条记录添加
        print(instocks)

        insert_success = connect.instock_register(instocks)
        if insert_success:
            QMessageBox.information(self, "登记提示", "登记成功！",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, "登记提示", "登记失败！请重试",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def AddLine(self):
        self.new_instock.setRowCount(self.new_instock.rowCount()+1)

    return_signal = pyqtSignal(str)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = InstockPane()
    window.show()

    sys.exit(app.exec_())
