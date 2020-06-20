from PyQt5.Qt import *
from UI.journal_whereabouts import Ui_MainWindow
import sys
from databaselink2 import connect


class JournalWhereaboutsPane(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("期刊管理系统")
        self.mode = "whereabouts"
        self.setupUi(self)
        self.retranslateUi(self)

    def Return(self):
        self.return_signal.emit(self.mode)

    def Search(self):
        journal_no = self.journal_no.text()
        results, feedback = connect.whereabouts_inquiry(journal_no)  # 调用方法
        self.whereabouts_result.clearContents()
        if feedback == "NotExist":
            QMessageBox.information(self, "查询提示", "该期刊不存在！",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        if len(results) == 0:
            self.whereabouts_result.setRowCount(1)
            newItem = QTableWidgetItem("没有去向记录")
            self.whereabouts_result.setItem(0, 0, newItem)
            return
        self.whereabouts_result.setRowCount(len(results))
        for i in range(len(results)):
            record = results[i]
            newItem = QTableWidgetItem(str(record[0]))
            self.whereabouts_result.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(str(record[1]))
            self.whereabouts_result.setItem(i, 1, newItem)
            newItem = QTableWidgetItem(str(record[2]))
            self.whereabouts_result.setItem(i, 2, newItem)
            newItem = QTableWidgetItem(str(record[3]))
            self.whereabouts_result.setItem(i, 3, newItem)
            newItem = QTableWidgetItem(str(record[4]))
            self.whereabouts_result.setItem(i, 4, newItem)

    return_signal = pyqtSignal(str)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = JournalWhereaboutsPane()
    window.show()

    sys.exit(app.exec_())
