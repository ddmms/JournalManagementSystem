from PyQt5.Qt import *
from UI.login import Ui_MainWindow
import sys


class LoginPane(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("期刊管理系统")
        self.setupUi(self)
        self.retranslateUi(self)

    def show_user_interface(self):
        account = self.accountInput.text()
        password = self.passwordInput.text()
        mode = ""
        if self.reader_select.isChecked():
            mode = "reader"
        if self.admin_select.isChecked():
            mode = "admin"
        self.log_in_signal.emit(account, password, mode)

    log_in_signal = pyqtSignal(str, str, str)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoginPane()
    window.show()

    sys.exit(app.exec_())
