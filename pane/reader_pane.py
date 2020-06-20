from PyQt5.Qt import *
from UI.reader_interface import Ui_MainWindow
import sys


class ReaderPane(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("期刊管理系统")
        self.mode = "reader"
        self.setupUi(self)
        self.retranslateUi(self)

    def log_out(self):
        self.log_out_signal.emit(self.mode)

    def journal_inquiry(self):
        self.to_journal_inquiry_signal.emit()

    def borrow_inquiry(self):
        self.to_borrow_inquiry_signal.emit()

    def book_and_inquiry(self):
        self.to_book_signal.emit()

    log_out_signal = pyqtSignal(str)
    to_journal_inquiry_signal = pyqtSignal()
    to_borrow_inquiry_signal = pyqtSignal()
    to_book_signal = pyqtSignal()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ReaderPane()
    window.show()

    sys.exit(app.exec_())
