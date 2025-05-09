from Tools.scripts.generate_global_objects import generate_runtime_init
from mimetypes import inited
from pathlib import WindowsPath
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QMessageBox, QLineEdit, QVBoxLayout, QListWidget, QGridLayout
from PyQt6.QtCore import Qt, QObject, pyqtSignal
from PyQt6.QtGui import QPixmap, QIcon

def singelton(cls):
    classes = {}
    def get_isinstance(*args, **kargs):
        if cls(*args, **kargs) not in classes:
            classes[cls] = cls(*args, **kargs)
        return classes[cls]
    return get_isinstance

@singelton
class Users:
    def __init__(self):
        self.__users = []
    def is_available_passwords(self, password):
        for user in self.__users:
            if user.password == password:
                return user
        return 0
    def sign_up(self, new_user):
        self.__users.append(new_user)

all_users = Users()

class User:
    def __init__(self, balance, password):
        self.balance = balance
        self.password = password
        all_users.sign_up(self)

user1 = User(2000000, "6202")
user2 = User(1000000, "0000")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("Hamid's ATM")
        self.l1 = QGridLayout()
        buttum1 = QPushButton("English")
        buttum1.clicked.connect(self.win_eng)
        buttum2 = QPushButton("فارسی")
        buttum2.clicked.connect(self.win_pars)
        lebel1 = QLabel("Choose language")
        lebel2 = QLabel("زبان خود را انتخاب کنید")
        self.l1.addWidget(buttum1, 0, 0)
        self.l1.addWidget(lebel1, 0, 1)
        self.l1.addWidget(lebel2, 0, 2)
        self.l1.addWidget(buttum2, 0,3)
        self.setLayout(self.l1)
    def win_eng(self):
        self.window1 = WindowEnglish1()
        self.window1.show()
    def win_pars(self):
        self.window2 = WindowParsian1()
        self.window2.show()

class WindowEnglish1(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("Hammid' ATM English")
        self.l1 = QVBoxLayout()
        lebel1 = QLabel("Please enter your password")
        self.line_edit1 = QLineEdit()
        self.lebel2 = QLabel("")
        buttum1 = QPushButton("Submit")
        buttum1.clicked.connect(self.window_show_widgets)
        self.l1.addWidget(lebel1)
        self.l1.addWidget(self.lebel2)
        self.l1.addWidget(self.line_edit1)
        self.l1.addWidget(buttum1)
        self.setLayout(self.l1)
    def window_show_widgets(self):
        if all_users.is_available_passwords(self.line_edit1.text()):
            window0.user = all_users.is_available_passwords(self.line_edit1.text())
            self.window_english2 = WindowEnglish2()
            self.window_english2.show()
        else:
            self.lebel2.setText("The password is wrong")

class WindowEnglish2(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("Table of Widgets")
        self.gird1 = QGridLayout()
        buttum1 = QPushButton("Get Cash")
        buttum1.clicked.connect(self.get_cash)
        buttum2 = QPushButton("Change Password")
        buttum2.clicked.connect(self.change_password)
        buttum3 = QPushButton("Money Transfer")
        buttum3.clicked.connect(self.transfer_window)
        buttum4 = QPushButton("Account Balance")
        buttum4.clicked.connect(self.checkout_balance)
        self.gird1.addWidget(buttum1, 0, 0)
        self.gird1.addWidget(buttum2, 0, 1)
        self.gird1.addWidget(buttum3, 1, 0)
        self.gird1.addWidget(buttum4, 1, 1)
        self.setLayout(self.gird1)
    def get_cash(self):
        self.window_get_cash = WindowGetCash()
        self.window_get_cash.show()
    def change_password(self):
        self.window_change_password = WindowChangePassword()
        self.window_change_password.show()
    def transfer_window(self):
        self.transfer_wind = WindowTransfer()
        self.transfer_wind.show()
    def checkout_balance(self):
        self.checkout_window = CheckOutWindow()
        self.checkout_window.show()

class WindowGetCash(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("Get Cash")
        self.gird1 = QGridLayout()
        buttum1 = QPushButton("500/000")
        buttum1.clicked.connect(self.buttum1)
        buttum2 = QPushButton("1/000/000")
        buttum2.clicked.connect(self.buttum2)
        buttum3 = QPushButton("1/500/000")
        buttum3.clicked.connect(self.buttum3)
        buttum4 = QPushButton("2/000/000")
        buttum4.clicked.connect(self.buttum4)
        self.lebel1 = QLabel("")
        lebel2 = QLabel("Enter your other amount")
        self.line_edit1 = QLineEdit()
        buttum5 = QPushButton("Submit")
        buttum5.clicked.connect(self.buttum5)
        self.gird1.addWidget(buttum1, 0, 0)
        self.gird1.addWidget(buttum2, 1, 0)
        self.gird1.addWidget(buttum3, 0, 2)
        self.gird1.addWidget(buttum4, 1, 2)
        self.gird1.addWidget(self.lebel1, 2, 1)
        self.gird1.addWidget(lebel2, 3, 1)
        self.gird1.addWidget(self.line_edit1, 4, 1)
        self.gird1.addWidget(buttum5, 5, 1)
        self.setLayout(self.gird1)
    def buttum1(self):
        if window0.user.balance >= 500000:
            window0.user.balance -= 500000
            self.final_window()
        else:
            self.lebel1.setText("Not Enough Money")
    def buttum2(self):
        if window0.user.balance >= 1000000:
            window0.user.balance -= 1000000
            self.final_window()
        else:
            self.lebel1.setText("Not Enough Money")
    def buttum3(self):
        if window0.user.balance >= 1500000:
            window0.user.balance -= 1500000
            self.final_window()
        else:
            self.lebel1.setText("Not Enough Money")
    def buttum4(self):
        if window0.user.balance >= 2000000:
            window0.user.balance -= 2000000
            self.final_window()
        else:
            self.lebel1.setText("Not Enough Money")
    def buttum5(self):
        amount = int(self.line_edit1.text())
        if window0.user.balance >= amount:
            window0.user.balance -= amount
            self.final_window()
        else:
            self.lebel1.setText("Not Enough Money")
    def final_window(self):
        self.final_w = WindowFinal()
        self.final_w.show()

class WindowChangePassword(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("Change Password")
        self.gird = QGridLayout()
        lebel1 = QLabel("Enter New Password:")
        self.lebel2 = QLabel("")
        self.line_edit1 = QLineEdit()
        buttum1 = QPushButton("Confrim")
        buttum1.clicked.connect(self.change_pass_and_new_window)
        self.gird.addWidget(lebel1, 0, 0)
        self.gird.addWidget(self.line_edit1, 0, 1)
        self.gird.addWidget(self.lebel2, 1, 0)
        self.gird.addWidget(buttum1, 1, 1)
        self.setLayout(self.gird)
    def change_pass_and_new_window(self):
        new_password = self.line_edit1.text()
        if len(new_password) != 4:
            self.lebel2.setText("The Format of Password is Wrong")
        else:
            window0.user.password = new_password
            self.final_window()
    def final_window(self):
        self.final_w = WindowFinal()
        self.final_w.show()

class WindowTransfer(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("Transfer Window")
        self.lbox = QVBoxLayout()
        lebel1 = QLabel("Enter The Desired Amount:")
        self.line_edit1 = QLineEdit()
        lebel2 = QLabel("Enter The Destination Card Number:")
        self.line_edit2 = QLineEdit()
        self.lebel3 = QLabel("")
        buttum1 = QPushButton("Confrim")
        buttum1.clicked.connect(self.transfer_and_finall_window)
        self.lbox.addWidget(lebel1)
        self.lbox.addWidget(self.line_edit1)
        self.lbox.addWidget(lebel2)
        self.lbox.addWidget(self.line_edit2)
        self.lbox.addWidget(self.lebel3)
        self.lbox.addWidget(buttum1)
        self.setLayout(self.lbox)
    def transfer_and_finall_window(self):
        amount = int(self.line_edit1.text())
        destination_card = self.line_edit2.text()
        if amount > window0.user.balance:
            self.lebel3.setText("Not Enough Money!")
        else:
            if all_users.is_available_passwords(destination_card):
               destination_user = all_users.is_available_passwords(destination_card)
               window0.user.balance -= amount
               destination_user.balance += amount
               self.final_window()
            else:
                self.lebel3.setText("The Card Number Not Found!")
    def final_window(self):
        self.final_w = WindowFinal()
        self.final_w.show()

class CheckOutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("Check Out Balance Window")
        self.lbox = QVBoxLayout()
        lebel1 = QLabel(f"Your Bank Account Balance is : {window0.user.balance}")
        buttum1 = QPushButton("Confrim")
        buttum1.clicked.connect(self.final_window)
        self.lbox.addWidget(lebel1)
        self.lbox.addWidget(buttum1)
        self.setLayout(self.lbox)
    def final_window(self):
        self.final_w = WindowFinal()
        self.final_w.show()

class WindowFinal(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("Final Mission")
        self.gird = QGridLayout()
        lebel = QLabel("Mission Accomplished Successfully!")
        buttum1 = QPushButton("Good Bye")
        buttum1.clicked.connect(self.end_mission)
        buttum2 = QPushButton("New Mission")
        buttum2.clicked.connect(self.new_mission)
        self.gird.addWidget(lebel, 0, 1)
        self.gird.addWidget(buttum1, 1, 0)
        self.gird.addWidget(buttum2, 1, 2)
        self.setLayout(self.gird)
    def end_mission(self):
       app.quit()
    def new_mission(self):
        self.new_missio = WindowEnglish2()
        self.new_missio.show()













class WindowParsian1(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("سامانه بانکی حمید")
        self.l1 = QVBoxLayout()
        lebel1 = QLabel("رمز خود را وارد کنید")
        self.line_edit1 = QLineEdit()
        self.lebel2 = QLabel("")
        buttum1 = QPushButton("ثبت")
        buttum1.clicked.connect(self.window_show_widgets)
        self.l1.addWidget(lebel1)
        self.l1.addWidget(self.lebel2)
        self.l1.addWidget(self.line_edit1)
        self.l1.addWidget(buttum1)
        self.setLayout(self.l1)
    def window_show_widgets(self):
        if all_users.is_available_passwords(self.line_edit1.text()):
            window0.user = all_users.is_available_passwords(self.line_edit1.text())
            self.window_parsian2 = WindowParsian2()
            self.window_parsian2.show()
        else:
            self.lebel2.setText("رمز نادرست می باشد")

class WindowParsian2(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("صفحه نمایش امکانات")
        self.gird1 = QGridLayout()
        buttum1 = QPushButton("برداشت وجه")
        buttum1.clicked.connect(self.get_cash)
        buttum2 = QPushButton("تغییر رمز")
        buttum2.clicked.connect(self.change_password)
        buttum3 = QPushButton("کارت به کارت")
        buttum3.clicked.connect(self.transfer_window)
        buttum4 = QPushButton("اعلام موجودی")
        buttum4.clicked.connect(self.checkout_balance)
        self.gird1.addWidget(buttum1, 0, 0)
        self.gird1.addWidget(buttum2, 0, 1)
        self.gird1.addWidget(buttum3, 1, 0)
        self.gird1.addWidget(buttum4, 1, 1)
        self.setLayout(self.gird1)
    def get_cash(self):
        self.window_get_cash = WindowGetCashPars()
        self.window_get_cash.show()
    def change_password(self):
        self.window_change_password = WindowChangePasswordPars()
        self.window_change_password.show()
    def transfer_window(self):
        self.transfer_wind = WindowTransferPars()
        self.transfer_wind.show()
    def checkout_balance(self):
        self.checkout_window = CheckOutWindowPars()
        self.checkout_window.show()

class WindowGetCashPars(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("برداشت وجه")
        self.gird1 = QGridLayout()
        buttum1 = QPushButton("500/000")
        buttum1.clicked.connect(self.buttum1)
        buttum2 = QPushButton("1/000/000")
        buttum2.clicked.connect(self.buttum2)
        buttum3 = QPushButton("1/500/000")
        buttum3.clicked.connect(self.buttum3)
        buttum4 = QPushButton("2/000/000")
        buttum4.clicked.connect(self.buttum4)
        self.lebel1 = QLabel("")
        lebel2 = QLabel("مقدار مورد نظر خود را وارد کنید")
        self.line_edit1 = QLineEdit()
        buttum5 = QPushButton("ثبت")
        buttum5.clicked.connect(self.buttum5)
        self.gird1.addWidget(buttum1, 0, 0)
        self.gird1.addWidget(buttum2, 1, 0)
        self.gird1.addWidget(buttum3, 0, 2)
        self.gird1.addWidget(buttum4, 1, 2)
        self.gird1.addWidget(self.lebel1, 2, 1)
        self.gird1.addWidget(lebel2, 3, 1)
        self.gird1.addWidget(self.line_edit1, 4, 1)
        self.gird1.addWidget(buttum5, 5, 1)
        self.setLayout(self.gird1)
    def buttum1(self):
        if window0.user.balance >= 500000:
            window0.user.balance -= 500000
            self.final_window()
        else:
            self.lebel1.setText("موجودی کافی نمی باشد")
    def buttum2(self):
        if window0.user.balance >= 1000000:
            window0.user.balance -= 1000000
            self.final_window()
        else:
            self.lebel1.setText("موجودی کافی نمی باشد")
    def buttum3(self):
        if window0.user.balance >= 1500000:
            window0.user.balance -= 1500000
            self.final_window()
        else:
            self.lebel1.setText("موجودی کافی نمی باشد")
    def buttum4(self):
        if window0.user.balance >= 2000000:
            window0.user.balance -= 2000000
            self.final_window()
        else:
            self.lebel1.setText("موجودی کافی نمی باشد")
    def buttum5(self):
        amount = int(self.line_edit1.text())
        if window0.user.balance >= amount:
            window0.user.balance -= amount
            self.final_window()
        else:
            self.lebel1.setText("موجودی کافی نمی باشد")
    def final_window(self):
        self.final_w = WindowFinalPars()
        self.final_w.show()

class WindowChangePasswordPars(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("رمز نادرست می باشد")
        self.gird = QGridLayout()
        lebel1 = QLabel("لطفا رمز خود را وارد کنید:")
        self.lebel2 = QLabel("")
        self.line_edit1 = QLineEdit()
        buttum1 = QPushButton("تایید")
        buttum1.clicked.connect(self.change_pass_and_new_window)
        self.gird.addWidget(lebel1, 0, 0)
        self.gird.addWidget(self.line_edit1, 0, 1)
        self.gird.addWidget(self.lebel2, 1, 0)
        self.gird.addWidget(buttum1, 1, 1)
        self.setLayout(self.gird)
    def change_pass_and_new_window(self):
        new_password = self.line_edit1.text()
        if len(new_password) != 4:
            self.lebel2.setText("رمز باید از چهار رقم تشکیل شده باشد")
        else:
            window0.user.password = new_password
            self.final_window()
    def final_window(self):
        self.final_w = WindowFinalPars()
        self.final_w.show()

class WindowTransferPars(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("کارت به کارت")
        self.lbox = QVBoxLayout()
        lebel1 = QLabel("مبلغ مورد نظر خود را وارد فرمایید:")
        self.line_edit1 = QLineEdit()
        lebel2 = QLabel("شماره کارت واریز شونده:")
        self.line_edit2 = QLineEdit()
        self.lebel3 = QLabel("")
        buttum1 = QPushButton("تایید")
        buttum1.clicked.connect(self.transfer_and_finall_window)
        self.lbox.addWidget(lebel1)
        self.lbox.addWidget(self.line_edit1)
        self.lbox.addWidget(lebel2)
        self.lbox.addWidget(self.line_edit2)
        self.lbox.addWidget(self.lebel3)
        self.lbox.addWidget(buttum1)
        self.setLayout(self.lbox)
    def transfer_and_finall_window(self):
        amount = int(self.line_edit1.text())
        destination_card = self.line_edit2.text()
        if amount > window0.user.balance:
            self.lebel3.setText("موجودی کافی نمی باشد")
        else:
            if all_users.is_available_passwords(destination_card):
               destination_user = all_users.is_available_passwords(destination_card)
               window0.user.balance -= amount
               destination_user.balance += amount
               self.final_window()
            else:
                self.lebel3.setText("شماره کارت موجود نمی باشد")
    def final_window(self):
        self.final_w = WindowFinalPars()
        self.final_w.show()

class CheckOutWindowPars(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("اعلام موجودی")
        self.lbox = QVBoxLayout()
        lebel1 = QLabel(f" موجودی حساب شما: {window0.user.balance}")
        buttum1 = QPushButton("تایید")
        buttum1.clicked.connect(self.final_window)
        self.lbox.addWidget(lebel1)
        self.lbox.addWidget(buttum1)
        self.setLayout(self.lbox)
    def final_window(self):
        self.final_w = WindowFinalPars()
        self.final_w.show()

class WindowFinalPars(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)
        self.setWindowTitle("پایان عملیات")
        self.gird = QGridLayout()
        lebel = QLabel("عملیات با موفقیت انجام شد")
        buttum1 = QPushButton("خدا نگهدار")
        buttum1.clicked.connect(self.end_mission)
        buttum2 = QPushButton("عملیات جدبد")
        buttum2.clicked.connect(self.new_mission)
        self.gird.addWidget(lebel, 0, 1)
        self.gird.addWidget(buttum1, 1, 0)
        self.gird.addWidget(buttum2, 1, 2)
        self.setLayout(self.gird)
    def end_mission(self):
       app.quit()
    def new_mission(self):
        self.new_missio = WindowParsian2()
        self.new_missio.show()


app = QApplication(sys.argv)
window0 = MainWindow()
window0.show()
app.exec()