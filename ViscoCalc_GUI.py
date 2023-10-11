import sys
import typing
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from GUI.GUI_Code import Ui_ViscoCalc
import Calculator as ca
import math
import sympy as sp

# pyuic6.exe -o .\GUI\GUI_Code.py .\GUI\ViscoCalc.ui

        
class GUI(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_ViscoCalc()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculator)
        self.ui.toolButton.clicked.connect(self.infobox)
        # self.ui.setWindowIcon('VC_Logo.ico')
        self.show()

    def calculator(self):
        self.ui.label_2.setText('Berechnung läuft')
        my_target = self.ui.input_my.value()
        temp = self.ui.input_T.value()
        print(my_target, temp)

        calc = ca.Calculator(temp, my_target)
        try: 
            result = "%.2f" % (calc.solve()*100)
            output = f'Für eine Viskosität von {"%.0f" % my_target} mPa s bei {temp} °C <br> werden <b>{result} wt-% </b> Glycerin benötigt.'
        except: output = 'Diese Kombination aus Viskosität und <br> Temperatur ist nicht möglich!'
        self.ui.label_2.setText(output)

    def infobox(self):
        newbox = QMessageBox()
        newbox.setText('<br> <b> Viskositätsberechnung für Glycerin-Wasser-Mischungen zwischen 0 und 100 °C </b><br>Basierend auf Cheng, N.-S. (2008). "Formula for the viscosity of a glycerol− water mixture." Industrial & Engineering Chemistry Research 47(9): 3285-3288. <br><br> © David Märker, 2023')
        newbox.setWindowTitle('Infos')
        newbox.setTextFormat(QtCore.Qt.TextFormat.RichText)
        newbox.setWindowIcon(QtGui.QIcon('assets/VC_Logo.ico'))
        newbox.exec()
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec())