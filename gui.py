# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 731)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Graficaintervalos = QtWidgets.QTabWidget(Dialog)
        self.Graficaintervalos.setGeometry(QtCore.QRect(0, 0, 651, 731))
        self.Graficaintervalos.setObjectName("Graficaintervalos")
        self.Abiertos = QtWidgets.QWidget()
        self.Abiertos.setObjectName("Abiertos")
        self.Abiertos1 = QtWidgets.QFrame(self.Abiertos)
        self.Abiertos1.setGeometry(QtCore.QRect(0, 10, 641, 1061))
        self.Abiertos1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Abiertos1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Abiertos1.setObjectName("Abiertos1")
        self.btnSolucion = QtWidgets.QPushButton(self.Abiertos1)
        self.btnSolucion.setGeometry(QtCore.QRect(30, 350, 291, 31))
        self.btnSolucion.setStyleSheet("background-color: rgb(15, 183, 255);")
        self.btnSolucion.setObjectName("btnSolucion")
        self.frameMetodosAbiertos = QtWidgets.QFrame(self.Abiertos1)
        self.frameMetodosAbiertos.setGeometry(QtCore.QRect(30, 100, 591, 231))
        self.frameMetodosAbiertos.setStyleSheet("\n"
"background-color: rgb(0, 170, 255);")
        self.frameMetodosAbiertos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMetodosAbiertos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMetodosAbiertos.setObjectName("frameMetodosAbiertos")
        self.label_11 = QtWidgets.QLabel(self.frameMetodosAbiertos)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.label_11.setObjectName("label_11")
        self.inputIngreseFuncion = QtWidgets.QLineEdit(self.frameMetodosAbiertos)
        self.inputIngreseFuncion.setGeometry(QtCore.QRect(120, 20, 421, 21))
        self.inputIngreseFuncion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputIngreseFuncion.setObjectName("inputIngreseFuncion")
        self.label_12 = QtWidgets.QLabel(self.frameMetodosAbiertos)
        self.label_12.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_12.setObjectName("label_12")
        self.inputIngreseError = QtWidgets.QLineEdit(self.frameMetodosAbiertos)
        self.inputIngreseError.setGeometry(QtCore.QRect(120, 70, 421, 21))
        self.inputIngreseError.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputIngreseError.setObjectName("inputIngreseError")
        self.label_10 = QtWidgets.QLabel(self.frameMetodosAbiertos)
        self.label_10.setGeometry(QtCore.QRect(20, 130, 101, 16))
        self.label_10.setObjectName("label_10")
        self.inputRaiz = QtWidgets.QLineEdit(self.frameMetodosAbiertos)
        self.inputRaiz.setGeometry(QtCore.QRect(120, 130, 421, 21))
        self.inputRaiz.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputRaiz.setObjectName("inputRaiz")
        self.textMetodosAbiertos = QtWidgets.QTextBrowser(self.Abiertos1)
        self.textMetodosAbiertos.setGeometry(QtCore.QRect(30, 400, 591, 261))
        self.textMetodosAbiertos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textMetodosAbiertos.setObjectName("textMetodosAbiertos")
        self.label_5 = QtWidgets.QLabel(self.Abiertos1)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 161, 41))
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"TEXT-COLOR:WHITE;")
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.btnGraficaNewton = QtWidgets.QPushButton(self.Abiertos1)
        self.btnGraficaNewton.setGeometry(QtCore.QRect(340, 350, 281, 31))
        self.btnGraficaNewton.setStyleSheet("background-color: rgb(15, 183, 255);")
        self.btnGraficaNewton.setObjectName("btnGraficaNewton")
        self.Graficaintervalos.addTab(self.Abiertos, "")
        self.invervalos = QtWidgets.QWidget()
        self.invervalos.setObjectName("invervalos")
        self.Intervalos = QtWidgets.QFrame(self.invervalos)
        self.Intervalos.setGeometry(QtCore.QRect(0, 0, 641, 701))
        self.Intervalos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Intervalos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Intervalos.setObjectName("Intervalos")
        self.btnsolucion_intervalos = QtWidgets.QPushButton(self.Intervalos)
        self.btnsolucion_intervalos.setGeometry(QtCore.QRect(30, 360, 291, 31))
        self.btnsolucion_intervalos.setStyleSheet("background-color: rgb(15, 183, 255);")
        self.btnsolucion_intervalos.setObjectName("btnsolucion_intervalos")
        self.frameMetodoIntervalos = QtWidgets.QFrame(self.Intervalos)
        self.frameMetodoIntervalos.setGeometry(QtCore.QRect(30, 110, 591, 231))
        self.frameMetodoIntervalos.setStyleSheet("\n"
"background-color: rgb(0, 170, 255);")
        self.frameMetodoIntervalos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMetodoIntervalos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMetodoIntervalos.setObjectName("frameMetodoIntervalos")
        self.label_15 = QtWidgets.QLabel(self.frameMetodoIntervalos)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.label_15.setObjectName("label_15")
        self.inputIngreseFuncion_intervalos = QtWidgets.QLineEdit(self.frameMetodoIntervalos)
        self.inputIngreseFuncion_intervalos.setGeometry(QtCore.QRect(120, 20, 421, 21))
        self.inputIngreseFuncion_intervalos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputIngreseFuncion_intervalos.setObjectName("inputIngreseFuncion_intervalos")
        self.label_16 = QtWidgets.QLabel(self.frameMetodoIntervalos)
        self.label_16.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_16.setObjectName("label_16")
        self.inputError_intervalos = QtWidgets.QLineEdit(self.frameMetodoIntervalos)
        self.inputError_intervalos.setGeometry(QtCore.QRect(120, 70, 421, 21))
        self.inputError_intervalos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputError_intervalos.setObjectName("inputError_intervalos")
        self.inputA = QtWidgets.QLineEdit(self.frameMetodoIntervalos)
        self.inputA.setGeometry(QtCore.QRect(120, 130, 421, 21))
        self.inputA.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputA.setObjectName("inputA")
        self.inputB = QtWidgets.QLineEdit(self.frameMetodoIntervalos)
        self.inputB.setGeometry(QtCore.QRect(120, 180, 421, 21))
        self.inputB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputB.setObjectName("inputB")
        self.label_14 = QtWidgets.QLabel(self.frameMetodoIntervalos)
        self.label_14.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.label_14.setObjectName("label_14")
        self.label_13 = QtWidgets.QLabel(self.frameMetodoIntervalos)
        self.label_13.setGeometry(QtCore.QRect(20, 180, 61, 16))
        self.label_13.setObjectName("label_13")
        self.textintervalos = QtWidgets.QTextBrowser(self.Intervalos)
        self.textintervalos.setGeometry(QtCore.QRect(30, 410, 591, 261))
        self.textintervalos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textintervalos.setObjectName("textintervalos")
        self.comboIntervalos = QtWidgets.QComboBox(self.Intervalos)
        self.comboIntervalos.setGeometry(QtCore.QRect(30, 40, 591, 51))
        self.comboIntervalos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboIntervalos.setObjectName("comboIntervalos")
        self.comboIntervalos.addItem("")
        self.comboIntervalos.addItem("")
        self.btnGraficaIntervalos = QtWidgets.QPushButton(self.Intervalos)
        self.btnGraficaIntervalos.setGeometry(QtCore.QRect(340, 360, 281, 31))
        self.btnGraficaIntervalos.setStyleSheet("background-color: rgb(15, 183, 255);")
        self.btnGraficaIntervalos.setObjectName("btnGraficaIntervalos")
        self.Graficaintervalos.addTab(self.invervalos, "")
        self.diferenciacion = QtWidgets.QWidget()
        self.diferenciacion.setObjectName("diferenciacion")
        self.frame1 = QtWidgets.QFrame(self.diferenciacion)
        self.frame1.setGeometry(QtCore.QRect(0, 0, 641, 701))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.btnSolucion_diferencia = QtWidgets.QPushButton(self.frame1)
        self.btnSolucion_diferencia.setGeometry(QtCore.QRect(30, 360, 291, 31))
        self.btnSolucion_diferencia.setStyleSheet("background-color: rgb(15, 183, 255);")
        self.btnSolucion_diferencia.setObjectName("btnSolucion_diferencia")
        self.frame_2 = QtWidgets.QFrame(self.frame1)
        self.frame_2.setGeometry(QtCore.QRect(30, 70, 591, 271))
        self.frame_2.setStyleSheet("\n"
"background-color: rgb(0, 170, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.label.setObjectName("label")
        self.inputfuncion_diferencia = QtWidgets.QLineEdit(self.frame_2)
        self.inputfuncion_diferencia.setGeometry(QtCore.QRect(120, 20, 421, 21))
        self.inputfuncion_diferencia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputfuncion_diferencia.setObjectName("inputfuncion_diferencia")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_2.setObjectName("label_2")
        self.inputerror_diferencia = QtWidgets.QLineEdit(self.frame_2)
        self.inputerror_diferencia.setGeometry(QtCore.QRect(120, 70, 421, 21))
        self.inputerror_diferencia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputerror_diferencia.setObjectName("inputerror_diferencia")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(20, 120, 61, 16))
        self.label_7.setObjectName("label_7")
        self.inputH = QtWidgets.QLineEdit(self.frame_2)
        self.inputH.setGeometry(QtCore.QRect(120, 120, 421, 21))
        self.inputH.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputH.setObjectName("inputH")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 81, 16))
        self.label_6.setObjectName("label_6")
        self.inputpunto_diferencia = QtWidgets.QLineEdit(self.frame_2)
        self.inputpunto_diferencia.setGeometry(QtCore.QRect(120, 180, 421, 21))
        self.inputpunto_diferencia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputpunto_diferencia.setObjectName("inputpunto_diferencia")
        self.comboDiferencia = QtWidgets.QComboBox(self.frame_2)
        self.comboDiferencia.setGeometry(QtCore.QRect(120, 230, 421, 22))
        self.comboDiferencia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboDiferencia.setObjectName("comboDiferencia")
        self.comboDiferencia.addItem("")
        self.comboDiferencia.addItem("")
        self.comboDiferencia.addItem("")
        self.comboDiferencia.addItem("")
        self.textdiferencia = QtWidgets.QTextBrowser(self.frame1)
        self.textdiferencia.setGeometry(QtCore.QRect(30, 410, 591, 261))
        self.textdiferencia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textdiferencia.setObjectName("textdiferencia")
        self.btnGraficaDiferencia = QtWidgets.QPushButton(self.frame1)
        self.btnGraficaDiferencia.setGeometry(QtCore.QRect(340, 360, 281, 31))
        self.btnGraficaDiferencia.setStyleSheet("background-color: rgb(15, 183, 255);")
        self.btnGraficaDiferencia.setObjectName("btnGraficaDiferencia")
        self.Graficaintervalos.addTab(self.diferenciacion, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame1_4 = QtWidgets.QFrame(self.tab)
        self.frame1_4.setGeometry(QtCore.QRect(0, 0, 641, 701))
        self.frame1_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1_4.setObjectName("frame1_4")
        self.btnsolucion_integracion = QtWidgets.QPushButton(self.frame1_4)
        self.btnsolucion_integracion.setGeometry(QtCore.QRect(30, 360, 291, 31))
        self.btnsolucion_integracion.setStyleSheet("background-color: rgb(15, 183, 255);")
        self.btnsolucion_integracion.setObjectName("btnsolucion_integracion")
        self.frame_4 = QtWidgets.QFrame(self.frame1_4)
        self.frame_4.setGeometry(QtCore.QRect(30, 70, 591, 271))
        self.frame_4.setStyleSheet("\n"
"background-color: rgb(0, 170, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.label_3.setObjectName("label_3")
        self.inputfuncion_integracion = QtWidgets.QLineEdit(self.frame_4)
        self.inputfuncion_integracion.setGeometry(QtCore.QRect(120, 20, 421, 21))
        self.inputfuncion_integracion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputfuncion_integracion.setObjectName("inputfuncion_integracion")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_4.setObjectName("label_4")
        self.puntoXo = QtWidgets.QLineEdit(self.frame_4)
        self.puntoXo.setGeometry(QtCore.QRect(120, 70, 421, 21))
        self.puntoXo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.puntoXo.setObjectName("puntoXo")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(20, 120, 61, 16))
        self.label_8.setObjectName("label_8")
        self.inputXn = QtWidgets.QLineEdit(self.frame_4)
        self.inputXn.setGeometry(QtCore.QRect(120, 120, 421, 21))
        self.inputXn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputXn.setObjectName("inputXn")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(20, 180, 81, 16))
        self.label_9.setObjectName("label_9")
        self.inputN = QtWidgets.QLineEdit(self.frame_4)
        self.inputN.setGeometry(QtCore.QRect(120, 180, 421, 21))
        self.inputN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputN.setObjectName("inputN")
        self.comboingracion = QtWidgets.QComboBox(self.frame_4)
        self.comboingracion.setGeometry(QtCore.QRect(120, 230, 421, 22))
        self.comboingracion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboingracion.setObjectName("comboingracion")
        self.comboingracion.addItem("")
        self.comboingracion.addItem("")
        self.comboingracion.addItem("")
        self.textintegracion = QtWidgets.QTextBrowser(self.frame1_4)
        self.textintegracion.setGeometry(QtCore.QRect(30, 410, 591, 261))
        self.textintegracion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textintegracion.setObjectName("textintegracion")
        self.btnGraficaIntegracion = QtWidgets.QPushButton(self.frame1_4)
        self.btnGraficaIntegracion.setGeometry(QtCore.QRect(340, 360, 281, 31))
        self.btnGraficaIntegracion.setStyleSheet("background-color: rgb(15, 183, 255);")
        self.btnGraficaIntegracion.setObjectName("btnGraficaIntegracion")
        self.Graficaintervalos.addTab(self.tab, "")

        self.retranslateUi(Dialog)
        self.Graficaintervalos.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnSolucion.setText(_translate("Dialog", "SOLUCION"))
        self.label_11.setText(_translate("Dialog", "Ingrese Funcion :"))
        self.label_12.setText(_translate("Dialog", "Ingrese error :"))
        self.label_10.setText(_translate("Dialog", "Aproximacion Raiz :"))
        self.label_5.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">NEWTON</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">NEWTON</span></p></body></html>"))
        self.btnGraficaNewton.setText(_translate("Dialog", "GRAFICA"))
        self.Graficaintervalos.setTabText(self.Graficaintervalos.indexOf(self.Abiertos), _translate("Dialog", "Newton"))
        self.btnsolucion_intervalos.setText(_translate("Dialog", "SOLUCION"))
        self.label_15.setText(_translate("Dialog", "Ingrese Funcion :"))
        self.label_16.setText(_translate("Dialog", "Ingrese error :"))
        self.label_14.setText(_translate("Dialog", "Ingresar a :"))
        self.label_13.setText(_translate("Dialog", "Ingresar b :"))
        self.textintervalos.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.comboIntervalos.setItemText(0, _translate("Dialog", "BISECCION"))
        self.comboIntervalos.setItemText(1, _translate("Dialog", "REGLAFALSA"))
        self.btnGraficaIntervalos.setText(_translate("Dialog", "GRAFICA"))
        self.Graficaintervalos.setTabText(self.Graficaintervalos.indexOf(self.invervalos), _translate("Dialog", "Metodos por intervalos"))
        self.btnSolucion_diferencia.setText(_translate("Dialog", "SOLUCION"))
        self.label.setText(_translate("Dialog", "Ingrese Funcion :"))
        self.label_2.setText(_translate("Dialog", "Ingrese error :"))
        self.label_7.setText(_translate("Dialog", "Ingrese H :"))
        self.label_6.setText(_translate("Dialog", "Ingrese punto :"))
        self.comboDiferencia.setItemText(0, _translate("Dialog", "Dos puntos"))
        self.comboDiferencia.setItemText(1, _translate("Dialog", "Tres puntos 1 : formula"))
        self.comboDiferencia.setItemText(2, _translate("Dialog", "Tres puntos 2 : formula"))
        self.comboDiferencia.setItemText(3, _translate("Dialog", "Segunda derivada"))
        self.btnGraficaDiferencia.setText(_translate("Dialog", "GRAFICA"))
        self.Graficaintervalos.setTabText(self.Graficaintervalos.indexOf(self.diferenciacion), _translate("Dialog", "diferenciacion numerica"))
        self.btnsolucion_integracion.setText(_translate("Dialog", "SOLUCION"))
        self.label_3.setText(_translate("Dialog", "Ingrese Funcion :"))
        self.label_4.setText(_translate("Dialog", "Punto Xo:"))
        self.label_8.setText(_translate("Dialog", "Ingrese Xn:"))
        self.label_9.setText(_translate("Dialog", "Ingrese N :"))
        self.comboingracion.setItemText(0, _translate("Dialog", "Trapecio"))
        self.comboingracion.setItemText(1, _translate("Dialog", "-"))
        self.comboingracion.setItemText(2, _translate("Dialog", "-"))
        self.btnGraficaIntegracion.setText(_translate("Dialog", "GRAFICA"))
        self.Graficaintervalos.setTabText(self.Graficaintervalos.indexOf(self.tab), _translate("Dialog", "Integracion numerica"))
