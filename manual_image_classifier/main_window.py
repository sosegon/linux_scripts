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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(683, 484)
        self.gv_image = QtGui.QGraphicsView(Dialog)
        self.gv_image.setGeometry(QtCore.QRect(10, 80, 661, 361))
        self.gv_image.setObjectName(_fromUtf8("gv_image"))
        self.chk_recursive = QtGui.QCheckBox(Dialog)
        self.chk_recursive.setGeometry(QtCore.QRect(590, 20, 88, 22))
        self.chk_recursive.setObjectName(_fromUtf8("chk_recursive"))
        self.btn_src = QtGui.QPushButton(Dialog)
        self.btn_src.setGeometry(QtCore.QRect(11, 11, 85, 27))
        self.btn_src.setObjectName(_fromUtf8("btn_src"))
        self.lbl_src = QtGui.QLabel(Dialog)
        self.lbl_src.setGeometry(QtCore.QRect(100, 16, 481, 17))
        self.lbl_src.setText(_fromUtf8(""))
        self.lbl_src.setObjectName(_fromUtf8("lbl_src"))
        self.lbl_dst = QtGui.QLabel(Dialog)
        self.lbl_dst.setGeometry(QtCore.QRect(100, 47, 571, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_dst.sizePolicy().hasHeightForWidth())
        self.lbl_dst.setSizePolicy(sizePolicy)
        self.lbl_dst.setText(_fromUtf8(""))
        self.lbl_dst.setObjectName(_fromUtf8("lbl_dst"))
        self.btn_dst = QtGui.QPushButton(Dialog)
        self.btn_dst.setGeometry(QtCore.QRect(12, 42, 85, 27))
        self.btn_dst.setObjectName(_fromUtf8("btn_dst"))
        self.btn_start = QtGui.QPushButton(Dialog)
        self.btn_start.setGeometry(QtCore.QRect(401, 451, 85, 27))
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.btn_pause = QtGui.QPushButton(Dialog)
        self.btn_pause.setGeometry(QtCore.QRect(492, 451, 85, 27))
        self.btn_pause.setObjectName(_fromUtf8("btn_pause"))
        self.btn_stop = QtGui.QPushButton(Dialog)
        self.btn_stop.setGeometry(QtCore.QRect(583, 451, 85, 27))
        self.btn_stop.setObjectName(_fromUtf8("btn_stop"))
        self.gv_image.raise_()
        self.chk_recursive.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.chk_recursive.setText(_translate("Dialog", "Recursive", None))
        self.btn_src.setText(_translate("Dialog", "Source", None))
        self.btn_dst.setText(_translate("Dialog", "Destination", None))
        self.btn_start.setText(_translate("Dialog", "Start", None))
        self.btn_pause.setText(_translate("Dialog", "Pause", None))
        self.btn_stop.setText(_translate("Dialog", "Stop", None))

