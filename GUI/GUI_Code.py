# Form implementation generated from reading ui file '.\ViscoCalc.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ViscoCalc(object):
    def setupUi(self, ViscoCalc):
        ViscoCalc.setObjectName("ViscoCalc")
        ViscoCalc.resize(400, 600)
        ViscoCalc.setMinimumSize(QtCore.QSize(400, 600))
        ViscoCalc.setMaximumSize(QtCore.QSize(400, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        ViscoCalc.setFont(font)
        # icon = QtGui.QIcon.fromTheme("VC_Logo.ico")
        ViscoCalc.setWindowIcon(QtGui.QIcon('assets/VC_Logo.ico'))
        self.gridLayoutWidget = QtWidgets.QWidget(parent=ViscoCalc)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 2)
        self.input_my = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.input_my.setDecimals(0)
        self.input_my.setMinimum(1.0)
        self.input_my.setMaximum(1500.0)
        self.input_my.setSingleStep(25.0)
        self.input_my.setProperty("value", 100.0)
        self.input_my.setObjectName("input_my")
        self.gridLayout.addWidget(self.input_my, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.my_label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.my_label.setFont(font)
        self.my_label.setObjectName("my_label")
        self.gridLayout.addWidget(self.my_label, 3, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.input_T = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.input_T.setDecimals(1)
        self.input_T.setMaximum(100.0)
        self.input_T.setSingleStep(1.0)
        self.input_T.setProperty("value", 20.0)
        self.input_T.setObjectName("input_T")
        self.gridLayout.addWidget(self.input_T, 4, 1, 1, 1)
        self.T_label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.T_label.setFont(font)
        self.T_label.setObjectName("T_label")
        self.gridLayout.addWidget(self.T_label, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(99999, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=ViscoCalc)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 440, 381, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.toolButton = QtWidgets.QToolButton(parent=ViscoCalc)
        self.toolButton.setGeometry(QtCore.QRect(290, 560, 101, 31))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(ViscoCalc)
        QtCore.QMetaObject.connectSlotsByName(ViscoCalc)

    def retranslateUi(self, ViscoCalc):
        _translate = QtCore.QCoreApplication.translate
        ViscoCalc.setWindowTitle(_translate("ViscoCalc", "ViscoCalc Tool"))
        self.pushButton.setText(_translate("ViscoCalc", "Berechnung starten"))
        self.my_label.setText(_translate("ViscoCalc", "Ziel-Viskosität [mPa s]"))
        self.T_label.setText(_translate("ViscoCalc", "Temperatur [°C]"))
        self.label.setText(_translate("ViscoCalc", "ViscoCalc"))
        self.toolButton.setText(_translate("ViscoCalc", "Info"))