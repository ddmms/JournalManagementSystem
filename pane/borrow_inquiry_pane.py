from PyQt5.Qt import *
from UI.borrow_inquiry import Ui_MainWindow
from databaselink2 import connect
import sys


class BorrowInquiryPane(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("期刊管理系统")
        self.mode = "borrow_inquiry"
        self.setupUi(self)
        self.retranslateUi(self)

    def Return(self):
        self.return_signal.emit(self.mode)

    def showAllBorrowResult(self):
        rno = self.property("rno")
        results = connect.borrow_inquiry(rno)
        self.showResults(results)

    def SiftNotReturn(self):
        rno = self.property("rno")
        if self.notReturnOnly.isChecked():
            self.borrow_result.clearContents()
            results = connect.borrow_inquiry_with_condition(rno)
            self.showResults(results)
        else:
            self.showAllBorrowResult()

    def showResults(self, results):
        if len(results) == 0:
            self.borrow_result.setRowCount(1)
            newItem = QTableWidgetItem("没有借阅记录")
            self.borrow_result.setItem(0, 0, newItem)
        self.borrow_result.setRowCount(len(results))
        for i in range(len(results)):
            record = results[i]
            newItem = QTableWidgetItem(str(record[0]))
            self.borrow_result.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(str(record[1]))
            self.borrow_result.setItem(i, 1, newItem)
            newItem = QTableWidgetItem(str(record[2]))
            self.borrow_result.setItem(i, 2, newItem)
            newItem = QTableWidgetItem(str(record[3]))
            self.borrow_result.setItem(i, 3, newItem)
            newItem = QTableWidgetItem(str(record[4]))
            self.borrow_result.setItem(i, 4, newItem)
            isReturn = record[5]
            if isReturn:
                showIsReturn = "是"
            else:
                showIsReturn = "否"
            newItem = QTableWidgetItem(showIsReturn)
            self.borrow_result.setItem(i, 5, newItem)

    return_signal = pyqtSignal(str)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = BorrowInquiryPane()
    window.show()

    sys.exit(app.exec_())
