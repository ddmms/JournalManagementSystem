from PyQt5.Qt import *
from UI.content_registration import Ui_MainWindow
import sys
from databaselink2 import connect


class ContentPane(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("期刊管理系统")
        self.mode = "content"
        self.setupUi(self)
        self.retranslateUi(self)

    def Return(self):
        self.return_signal.emit(self.mode)

    def Submit(self):
        row_count = self.new_content.rowCount()
        column_count = self.new_content.columnCount()
        contents = []  # 入库登记内容
        for row in range(row_count):
            if self.new_content.item(row, 0) is None:
                continue
            content = []
            for col in range(column_count):
                item = self.new_content.item(row, col)
                if col not in range(6, 11) and item is None:  # 非关键字为空进行警告
                    QMessageBox.warning(self, "登记提示", "录入信息不完整！请重试",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    return
                content.append(item.text())
            contents.append(content)  # 逐条记录添加
        print(contents)

        insert_success = connect.content_register(contents)
        if insert_success:
            QMessageBox.information(self, "登记提示", "登记成功！",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, "登记提示", "登记失败！请重试",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def AddLine(self):
        self.new_content.setRowCount(self.new_instock.rowCount()+1)

    return_signal = pyqtSignal(str)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ContentPane()
    window.show()

    sys.exit(app.exec_())
