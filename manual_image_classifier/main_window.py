# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(676, 531)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gv_image = QtGui.QGraphicsView(self.centralwidget)
        self.gv_image.setGeometry(QtCore.QRect(8, 79, 661, 361))
        self.gv_image.setObjectName(_fromUtf8("gv_image"))
        self.lbl_dst = QtGui.QLabel(self.centralwidget)
        self.lbl_dst.setGeometry(QtCore.QRect(98, 46, 571, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_dst.sizePolicy().hasHeightForWidth())
        self.lbl_dst.setSizePolicy(sizePolicy)
        self.lbl_dst.setText(_fromUtf8(""))
        self.lbl_dst.setObjectName(_fromUtf8("lbl_dst"))
        self.lbl_src = QtGui.QLabel(self.centralwidget)
        self.lbl_src.setGeometry(QtCore.QRect(98, 15, 481, 17))
        self.lbl_src.setText(_fromUtf8(""))
        self.lbl_src.setObjectName(_fromUtf8("lbl_src"))
        self.btn_start = QtGui.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(399, 450, 85, 27))
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.btn_pause = QtGui.QPushButton(self.centralwidget)
        self.btn_pause.setGeometry(QtCore.QRect(490, 450, 85, 27))
        self.btn_pause.setObjectName(_fromUtf8("btn_pause"))
        self.btn_stop = QtGui.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(581, 450, 85, 27))
        self.btn_stop.setObjectName(_fromUtf8("btn_stop"))
        self.btn_src = QtGui.QPushButton(self.centralwidget)
        self.btn_src.setGeometry(QtCore.QRect(9, 10, 85, 27))
        self.btn_src.setObjectName(_fromUtf8("btn_src"))
        self.chk_recursive = QtGui.QCheckBox(self.centralwidget)
        self.chk_recursive.setGeometry(QtCore.QRect(588, 13, 88, 22))
        self.chk_recursive.setObjectName(_fromUtf8("chk_recursive"))
        self.btn_dst = QtGui.QPushButton(self.centralwidget)
        self.btn_dst.setGeometry(QtCore.QRect(10, 41, 85, 27))
        self.btn_dst.setObjectName(_fromUtf8("btn_dst"))
        self.txt_class_name = QtGui.QLineEdit(self.centralwidget)
        self.txt_class_name.setEnabled(False)
        self.txt_class_name.setGeometry(QtCore.QRect(88, 451, 201, 27))
        self.txt_class_name.setObjectName(_fromUtf8("txt_class_name"))
        self.lbl_class_name = QtGui.QLabel(self.centralwidget)
        self.lbl_class_name.setGeometry(QtCore.QRect(12, 456, 69, 17))
        self.lbl_class_name.setObjectName(_fromUtf8("lbl_class_name"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_start.setText(_translate("MainWindow", "Start", None))
        self.btn_pause.setText(_translate("MainWindow", "Pause", None))
        self.btn_stop.setText(_translate("MainWindow", "Stop", None))
        self.btn_src.setText(_translate("MainWindow", "Source", None))
        self.chk_recursive.setText(_translate("MainWindow", "Recursive", None))
        self.btn_dst.setText(_translate("MainWindow", "Destination", None))
        self.lbl_class_name.setText(_translate("MainWindow", "Class name:", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))

