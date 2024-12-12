# Form implementation generated from reading ui file 'intro_gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_window_intro(object):
    def setupUi(self, window_intro):
        window_intro.setObjectName("window_intro")
        window_intro.resize(350, 251)
        window_intro.setMinimumSize(QtCore.QSize(350, 250))
        self.centralwidget = QtWidgets.QWidget(parent=window_intro)
        self.centralwidget.setObjectName("centralwidget")
        self.label_player_name_one = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_player_name_one.setGeometry(QtCore.QRect(40, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_player_name_one.setFont(font)
        self.label_player_name_one.setObjectName("label_player_name_one")
        self.label_player_name_two = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_player_name_two.setGeometry(QtCore.QRect(40, 140, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_player_name_two.setFont(font)
        self.label_player_name_two.setObjectName("label_player_name_two")
        self.input_player_name_one = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_player_name_one.setGeometry(QtCore.QRect(190, 90, 113, 31))
        self.input_player_name_one.setObjectName("input_player_name_one")
        self.input_player_name_two = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_player_name_two.setGeometry(QtCore.QRect(190, 140, 113, 31))
        self.input_player_name_two.setObjectName("input_player_name_two")
        self.button_enter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(140, 200, 61, 31))
        self.button_enter.setObjectName("button_enter")
        self.label_title = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_instructions = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_instructions.setGeometry(QtCore.QRect(30, 40, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_instructions.setFont(font)
        self.label_instructions.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_instructions.setObjectName("label_instructions")
        window_intro.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=window_intro)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 18))
        self.menubar.setObjectName("menubar")
        window_intro.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=window_intro)
        self.statusbar.setObjectName("statusbar")
        window_intro.setStatusBar(self.statusbar)

        self.retranslateUi(window_intro)
        QtCore.QMetaObject.connectSlotsByName(window_intro)

    def retranslateUi(self, window_intro):
        _translate = QtCore.QCoreApplication.translate
        window_intro.setWindowTitle(_translate("window_intro", "Welcome to Connect 4!"))
        self.label_player_name_one.setText(_translate("window_intro", "Player One:"))
        self.label_player_name_two.setText(_translate("window_intro", "Player Two:"))
        self.button_enter.setText(_translate("window_intro", "Enter"))
        self.label_title.setText(_translate("window_intro", "Welcome to Connect 4!"))
        self.label_instructions.setText(_translate("window_intro", "Please enter your names to continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_intro = QtWidgets.QMainWindow()
    ui = Ui_window_intro()
    ui.setupUi(window_intro)
    window_intro.show()
    sys.exit(app.exec())