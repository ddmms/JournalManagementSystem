from PyQt5.Qt import *
from UI.admin_interface import Ui_MainWindow
import sys


class AdminPane(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.mode = "admin"
        self.setupUi(self)
        self.retranslateUi(self)

    def log_out(self):
        self.log_out_signal.emit(self.mode)

    def instock_register(self):
        self.to_instock_register_signal.emit()

    def catalog_register(self):
        self.to_catalog_register_signal.emit()

    def content_register(self):
        self.to_content_register_signal.emit()

    def borrow_register(self):
        self.to_borrow_register_signal.emit()

    def journal_whereabouts_inquiry(self):
        self.to_journal_whereabouts_signal.emit()

    def subscribe(self):
        self.to_subscribe_signal.emit()

    log_out_signal = pyqtSignal(str)
    to_instock_register_signal = pyqtSignal()
    to_catalog_register_signal = pyqtSignal()
    to_content_register_signal = pyqtSignal()
    to_borrow_register_signal = pyqtSignal()
    to_journal_whereabouts_signal = pyqtSignal()
    to_subscribe_signal = pyqtSignal()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = AdminPane()
    window.show()

    sys.exit(app.exec_())
