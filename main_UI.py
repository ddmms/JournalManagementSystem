from pane.login_pane import LoginPane
from pane.admin_pane import AdminPane
from pane.reader_pane import ReaderPane
from pane.instock_pane import InstockPane
from pane.catalog_pane import CatalogPane
from pane.content_pane import ContentPane
from pane.borrow_regis_pane import BorrowRegisPane
from pane.journal_whereabouts_pane import JournalWhereaboutsPane
from pane.subcribe_pane import SubscribePane
from pane.journal_inquiry_pane import JournalInquiryPane
from pane.borrow_inquiry_pane import BorrowInquiryPane
from pane.book_pane import BookPane
import sys
from PyQt5.QtWidgets import *
import databaselink2


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 以下是实现跳转逻辑的槽函数
    def log_in(account, password, mode):
        isValidate, feedback = databaselink2.connect.check_log_in(account, password, mode)
        print(feedback)
        if not isValidate:
            login_window.failureTip.setText(feedback)
            return
        x, y = login_window.x(), login_window.y()
        if mode == "admin":
            admin_window.move(x, y)
            admin_window.show()
        if mode == "reader":
            reader_window.move(x, y)
            reader_window.show()
            borrow_inquiry_window.setProperty("rno", account)
            borrow_inquiry_window.showAllBorrowResult()
            book_window.setProperty("rno", account)
            book_window.showbookedJournal()
        login_window.close()

    def log_out(mode):
        x, y = login_window.x(), login_window.y()
        if mode == "admin":
            x, y = admin_window.x(), admin_window.y()
            admin_window.close()
        if mode == "reader":
            x, y = reader_window.x(), reader_window.y()
            reader_window.close()
        login_window.move(x, y)
        login_window.show()

    def to_instock():
        x, y = admin_window.x(), admin_window.y()
        instock_window.move(x, y)
        instock_window.show()
        admin_window.close()

    def to_catalog():
        x, y = admin_window.x(), admin_window.y()
        catalog_window.move(x, y)
        catalog_window.show()
        admin_window.close()

    def to_content():
        x, y = admin_window.x(), admin_window.y()
        content_window.move(x, y)
        content_window.show()
        admin_window.close()

    def to_borrow_regis():
        x, y = admin_window.x(), admin_window.y()
        borrow_regis_window.move(x, y)
        borrow_regis_window.show()
        admin_window.close()

    def to_whereabouts():
        x, y = admin_window.x(), admin_window.y()
        whereabouts_window.move(x, y)
        whereabouts_window.show()
        admin_window.close()

    def to_subscribe():
        x, y = admin_window.x(), admin_window.y()
        subscribe_window.move(x, y)
        subscribe_window.show()
        admin_window.close()

    def return_to_admin(mode):
        x, y = admin_window.x(), admin_window.y()
        if mode == "instock":
            x, y = instock_window.x(), instock_window.y()
            instock_window.close()
        if mode == "catalog":
            x, y = catalog_window.x(), catalog_window.y()
            catalog_window.close()
        if mode == "content":
            x, y = content_window.x(), content_window.y()
            content_window.close()
        if mode == "borrow_regis":
            x, y = borrow_regis_window.x(), borrow_regis_window.y()
            borrow_regis_window.close()
        if mode == "whereabouts":
            x, y = whereabouts_window.x(), whereabouts_window.y()
            whereabouts_window.close()
        if mode == "subscribe":
            x, y = subscribe_window.x(), subscribe_window.y()
            subscribe_window.close()
        admin_window.move(x, y)
        admin_window.show()

    def to_journal_inquiry():
        x, y = reader_window.x(), reader_window.y()
        journal_inquiry_window.move(x, y)
        journal_inquiry_window.show()
        reader_window.close()

    def to_borrow_inquiry():
        x, y = reader_window.x(), reader_window.y()
        borrow_inquiry_window.move(x, y)
        borrow_inquiry_window.show()
        reader_window.close()

    def to_book():
        x, y = reader_window.x(), reader_window.y()
        book_window.move(x, y)
        book_window.show()
        reader_window.close()

    def return_to_reader(mode):
        x, y = reader_window.x(), reader_window.y()
        if mode == "journal_inquiry":
            x, y = journal_inquiry_window.x(), journal_inquiry_window.y()
            journal_inquiry_window.close()
        if mode == "borrow_inquiry":
            x, y = borrow_inquiry_window.x(), borrow_inquiry_window.y()
            borrow_inquiry_window.close()
        if mode == "book":
            x, y = book_window.x(), book_window.y()
            book_window.close()
        reader_window.move(x, y)
        reader_window.show()

    # 登录界面
    login_window = LoginPane()
    login_window.log_in_signal.connect(log_in)

    # 管理员界面
    admin_window = AdminPane()
    admin_window.log_out_signal.connect(log_out)
    admin_window.to_instock_register_signal.connect(to_instock)
    admin_window.to_content_register_signal.connect(to_content)
    admin_window.to_catalog_register_signal.connect(to_catalog)
    admin_window.to_borrow_register_signal.connect(to_borrow_regis)
    admin_window.to_journal_whereabouts_signal.connect(to_whereabouts)
    admin_window.to_subscribe_signal.connect(to_subscribe)

    # 读者登录界面
    reader_window = ReaderPane()
    reader_window.log_out_signal.connect(log_out)
    reader_window.to_journal_inquiry_signal.connect(to_journal_inquiry)
    reader_window.to_borrow_inquiry_signal.connect(to_borrow_inquiry)
    reader_window.to_book_signal.connect(to_book)

    # 入库登记界面
    instock_window = InstockPane()
    instock_window.return_signal.connect(return_to_admin)

    # 目录登记界面
    catalog_window = CatalogPane()
    catalog_window.return_signal.connect(return_to_admin)

    # 内容登记界面
    content_window = ContentPane()
    content_window.return_signal.connect(return_to_admin)

    # 借阅登记界面
    borrow_regis_window = BorrowRegisPane()
    borrow_regis_window.return_signal.connect(return_to_admin)

    # 去向查询界面
    whereabouts_window = JournalWhereaboutsPane()
    whereabouts_window.return_signal.connect(return_to_admin)

    # 征订界面
    subscribe_window = SubscribePane()
    subscribe_window.return_signal.connect(return_to_admin)

    # 期刊查询界面
    journal_inquiry_window = JournalInquiryPane()
    journal_inquiry_window.return_signal.connect(return_to_reader)

    # 借阅查询界面
    borrow_inquiry_window = BorrowInquiryPane()
    borrow_inquiry_window.return_signal.connect(return_to_reader)

    # 预定界面
    book_window = BookPane()
    book_window.return_signal.connect(return_to_reader)

    login_window.show()

    sys.exit(app.exec_())
