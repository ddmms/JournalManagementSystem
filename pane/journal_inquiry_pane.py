from PyQt5.Qt import *
from UI.journal_inquiry import Ui_MainWindow
import sys
from databaselink2 import connect


class JournalInquiryPane(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("期刊管理系统")
        self.mode = "journal_inquiry"
        self.setupUi(self)
        self.retranslateUi(self)

    def Return(self):
        self.return_signal.emit(self.mode)

    def Search(self):
        keyword = self.input_keyword.text()
        results = connect.journal_inquiry(keyword)  # 调用方法
        self.result.clearContents()
        if len(results) == 0:
            self.result.setRowCount(1)
            newItem = QTableWidgetItem("没有期刊记录")
            self.result.setItem(0, 0, newItem)
            return
        self.result.setRowCount(len(results))
        for i in range(len(results)):
            record = results[i]
            for j in range(len(record)):
                newItem = QTableWidgetItem(str(record[j]))
                self.result.setItem(i, j, newItem)

    return_signal = pyqtSignal(str)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = JournalInquiryPane()
    window.show()

    sys.exit(app.exec_())
