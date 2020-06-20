from PyQt5.Qt import *
from UI.catalog_registration import Ui_MainWindow
import sys
from databaselink2 import connect


class CatalogPane(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("期刊管理系统")
        self.mode = "catalog"
        self.setupUi(self)
        self.retranslateUi(self)

    def Return(self):
        self.return_signal.emit(self.mode)

    def Submit(self):
        row_count = self.new_catalog.rowCount()
        column_count = self.new_catalog.columnCount()
        catalogs = []  # 入库登记内容
        for row in range(row_count):
            if self.new_catalog.item(row, 0) is None:
                continue
            catalog = []
            for col in range(column_count):
                item = self.new_catalog.item(row, col)
                if item is None:
                    QMessageBox.warning(self, "登记提示", "录入信息不完整！请重试",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    return
                catalog.append(item.text())
            catalogs.append(catalog)  # 逐条记录添加
        print(catalogs)

        insert_success = connect.catalog_register(catalogs)
        if insert_success:
            QMessageBox.information(self, "登记提示", "登记成功！",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, "登记提示", "登记失败！请重试",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def AddLine(self):
        self.new_catalog.setRowCount(self.new_catalog.rowCount()+1)

    return_signal = pyqtSignal(str)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CatalogPane()
    window.show()

    sys.exit(app.exec_())
