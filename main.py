import sys
import numpy as np
from sympy import *
import sympy as sym
import matplotlib.pyplot as plt
from math import *
import itertools
from gui import *


def fnew(f, x):
    import math
    return eval(f)

class Ui_aplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnSolucion.clicked.connect(self.obtener)
        self.ui.btnsolucion_intervalos.clicked.connect(self.obtener2)
        self.ui.btnSolucion_diferencia.clicked.connect(self.obtener3)
        self.ui.btnsolucion_integracion.clicked.connect(self.obtener4)
        self.ui.btnGraficaNewton.clicked.connect(self.Grafican)
        self.ui.btnGraficaDiferencia.clicked.connect(self.Graficadiferencia)
        self.ui.btnGraficaIntervalos.clicked.connect(self.Graficarintervalo)
        self.ui.btnGraficaIntegracion.clicked.connect(self.GraficaIntegracion)


    def Grafican(self):
        ent = self.ui.inputIngreseFuncion.text()
        x = np.linspace(-5, 5, 1000)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_position('center')
        ax.spines['top'].set_position('zero')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        # Trazar la funcion
        plt.plot(x, [fnew(ent,i) for i in x])
        plt.show()

    def Graficarintervalo(self):
        ent = self.ui.inputIngreseFuncion_intervalos.text()
        x = np.linspace(-1, 1, 1000)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_position('center')
        ax.spines['top'].set_position('zero')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x, [fnew(ent,i) for i in x])
        plt.show()

    def Graficadiferencia(self):
        ent = self.ui.inputfuncion_diferencia.text()
        x = np.linspace(-5, 5, 1000)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_position('center')
        ax.spines['top'].set_position('zero')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        # Trazar la funcion
        plt.plot(x, [fnew(ent,i) for i in x])
        plt.show()

    def GraficaIntegracion(self):
        ent = self.ui.inputfuncion_integracion.text()
        x = np.linspace(-5, 5, 1000)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_position('center')
        ax.spines['top'].set_position('zero')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        # Trazar la funcion
        plt.plot(x, [fnew(ent,i) for i in x])
        plt.show()

    def obtener2(self):
        entrada = self.ui.comboIntervalos.itemText(self.ui.comboIntervalos.currentIndex())

        if entrada == "BISECCION":
            fx = self.ui.inputIngreseFuncion_intervalos.text()

            error = self.ui.inputError_intervalos.text()
            er = float(error)
            err = 10 ** (er)

            variableA = self.ui.inputA.text()
            a1 = float(variableA)
            variableB = self.ui.inputB.text()
            b1 = float(variableB)
            g = "'Iteracion', 'limiteINF', 'limiteMAY', 'xm', 'fa', 'fb', 'fxm', 'error','siga'" + "\n "
            tolerancia = 1
            ys = []
            contador = 1
            x = a1
            fa = eval(fx)
            x = b1
            fb = eval(fx)
            mult = fa * fb
            # Revisa condicion  f(a)*f(b) < 0
            if mult > 0:
                print(
                    "los intervalos ingresados no cumplen con la condicion f(a)*f(b) < 0 , ingrese nuevos intervalos : ",
                    mult)
                print("Ingrese a :")
                a1 = float(input())
                print("Ingrese b :")
                b1 = float(input())
                x = a1
                fa = eval(fx)
                x = b1
                fb = eval(fx)
                mult = fa * fb
            puntoMedio = (a1 + b1) / 2
            while tolerancia > err:
                puntoAnterior = puntoMedio
                x = a1
                fa = eval(fx)
                x = b1
                fb = eval(fx)
                x = puntoMedio
                fxm = eval(fx)
                if fa == 0:
                    g = " f(a) es una raiz :" + a1
                    break
                if fb == 0:
                    g = " f(b) es una raiz :" + b1
                    break
                if fxm == 0:
                    g = " f(b) es una raiz :" + puntoMedio
                    break
                if (err > abs(fxm)):
                    siga = "PARE"
                else:
                    siga = "SIGA"
                g += "\n " + str(contador) + " :[ limiteINF: " + str(a1) + " , limiteMAY: " + str(b1) + " , xm: " + str(
                    puntoMedio) + " , fa: " + str(
                    fa) + " , fb: " + str(fb) + " , fxm: " + str(fxm) + " , ERROR " + str(tolerancia) + "]" + "\n "
                if fa * fxm < 0:
                    b1 = puntoMedio
                    puntoMedio = (a1 + b1) / 2
                if fxm * fb < 0:
                    a1 = puntoMedio
                    puntoMedio = (a1 + b1) / 2
                contador = contador + 1
                tolerancia = abs(puntoMedio - puntoAnterior)
            self.ui.textintervalos.setText(g)

        if entrada == "REGLAFALSA":
            fx = self.ui.inputIngreseFuncion_intervalos.text()

            error = self.ui.inputError_intervalos.text()
            er = float(error)
            err = 10 ** (er)

            variableA = self.ui.inputA.text()
            a1 = float(variableA)
            variableB = self.ui.inputB.text()
            b1 = float(variableB)
            g = "'Iteracion', 'limiteINF', 'limiteMAY', 'xm', 'fa', 'fb', 'fxm', 'error'" + "\n "

            tol = abs(b1 - a1)
            ys = []
            contador = 1
            puntoAnterior = 0
            x = a1
            fa = eval(fx)
            x = b1
            fb = eval(fx)
            mult = fa * fb

            # Revisa condicion  f(a)*f(b) < 0
            if mult > 0:
                g = "los intervalos ingresados no cumplen con la condicion f(a)*f(b) < 0 , ingrese nuevos intervalos : " + str(
                    mult)
                self.ui.textintervalos.setText(g)
            else:
                while tol > err:
                    x = a1
                    fa = eval(fx)
                    x = b1
                    fb = eval(fx)
                    punto = (a1 - ((fa * (b1 - a1)) / (fb - fa)))
                    tol = abs(punto - puntoAnterior)
                    puntoAnterior = punto
                    x = punto
                    fxm = eval(fx)
                    if fa == 0:
                        print(" f(a) es una raiz :", a1)
                        break
                    if fb == 0:
                        print(" f(b) es una raiz :", b1)
                        break
                    if fxm == 0:
                        print(" f(b) es una raiz :", punto)
                        break
                    if (err > abs(fxm)):
                        siga = "PARE"
                    else:
                        siga = "SIGA"
                    g += "\n " + str(contador) + " :[ limiteINF : " + str(a1) + " , limiteMAY:" + str(
                        b1) + " , xm: " + str(punto) + " , fa: " + str(
                        fa) + " , fb: " + str(fb) + " , fxm: " + str(fxm) + " , error: " + str(tol) + "]" + "\n "
                    if fa * fxm < 0:
                        b1 = punto
                    if fxm * fb < 0:
                        a1 = punto
                    punto = (a1 - ((fa * (b1 - a1)) / (fb - fa)))
                    contador = contador + 1
                self.ui.textintervalos.setText(g)

    def obtener(self):

        f = self.ui.inputIngreseFuncion.text()
        error = self.ui.inputIngreseError.text()
        er = float(error)
        err = 10 ** (er)
        g = " X , F(x) , F'(x) , ERROR  " + "\n"
        raiz = self.ui.inputRaiz.text()
        x_anterior = float(raiz)
        fx = sym.parse_expr(f)
        x = sym.Symbol('x')
        tolerancia = 1
        iteracion = 0
        derivada = fx.diff(x)
        f_anterior = fx.subs(x, x_anterior)
        derivada_anterior = derivada.subs(x, x_anterior)
        while f_anterior == 0:
            g = "la raiz es :" + str(x_anterior)
            tolerancia = err * -1
        while derivada_anterior == 0:
            g = "EL metodo no converge"
            tolerancia = err * -1
        while tolerancia > err:
            g += "\n" + str(iteracion) + ":[ X: " + str(x_anterior) + " , F(x): " + str(
                f_anterior) + " , F'(x): " + str(
                derivada_anterior) + " , ERROR:  " + str(tolerancia) + "]" + "\n "
            x_siguiente = x_anterior - f_anterior / derivada_anterior
            tolerancia = abs(x_siguiente - x_anterior)
            x_anterior = x_siguiente

            f_anterior = fx.subs(x, x_anterior)
            derivada_anterior = derivada.subs(x, x_anterior)
            while derivada_anterior == 0:
                g = "\n " + "metodo no converge" + "\n "
                break
            iteracion = iteracion + 1
        g += "\n " + "La raiz es:" + str(x_anterior) + " Fue encontrada en la iteración: " + str(
            iteracion) + " con un error de: " + str(tolerancia) + "\n "
        self.ui.textMetodosAbiertos.setText(g)

    def obtener3(self):
        metodo = self.ui.comboDiferencia.itemText(self.ui.comboDiferencia.currentIndex())
        f = self.ui.inputfuncion_diferencia.text()

        error = self.ui.inputerror_diferencia.text()
        er = float(error)
        err = 10 ** (er)

        valorh = self.ui.inputH.text()
        H = float(valorh)

        valorpunto = self.ui.inputpunto_diferencia.text()
        Xo = float(valorpunto)
        g = "'f','Xo','H','Derivada','Error'"
        iteracion = 0
        tolerancia = 1
        if metodo == "Dos puntos":
            x = Xo + H
            f1 = eval(f)
            x = Xo
            f2 = eval(f)
            Drv = (f1 - f2) / H
        if metodo == "Tres puntos 1 : formula":
            x = Xo
            f1 = eval(f)
            x = Xo + H
            f2 = eval(f)
            x = Xo + 2 * H
            f3 = eval(f)
            Drv = ((1 / (2 * H)) * (- 3 * (f1) + 4 * (f2) - (f3)))
        if metodo == "Tres puntos 2 : formula":
            x = Xo + H
            f1 = eval(f)
            x = Xo - H
            f2 = eval(f)
            Drv = ((1 / (2 * H)) * ((f1) - (f2)))
        if metodo == "Segunda derivada":
            x = Xo - H
            f1 = eval(f)
            x = Xo
            f2 = eval(f)
            x = Xo + H
            f3 = eval(f)
            Drv = ((1 / (H ** 2)) * ((f1) - 2 * (f2) + (f3)))
        D = []
        while tolerancia > err:
            D.append([f, Xo, H, Drv, tolerancia])
            g += "\n " + str(iteracion) + " :[ F: " + str(f) + " , XO: " + str(Xo) + " , H: " + str(
                H) + " , Derivada: " + str(
                Drv) + " , ERROR " + str(tolerancia) + "]" + "\n "
            H = H / 10
            if metodo == "Dos puntos":
                x = Xo + H
                f1 = eval(f)
                x = Xo
                f2 = eval(f)
                Drv1 = (f1 - f2) / H
            if metodo == "Tres puntos 1 : formula":
                x = Xo
                f1 = eval(f)
                x = Xo + H
                f2 = eval(f)
                x = Xo + 2 * H
                f3 = eval(f)
                Drv1 = ((1 / (2 * H)) * (- 3 * (f1) + 4 * (f2) - (f3)))

            if metodo == "Tres puntos 2 : formula":
                x = Xo + H
                f1 = eval(f)
                x = Xo - H
                f2 = eval(f)
                Drv1 = ((1 / (2 * H)) * ((f1) - (f2)))
            if metodo == "Segunda derivada":
                x = Xo - H
                f1 = eval(f)
                x = Xo
                f2 = eval(f)
                x = Xo + H
                f3 = eval(f)
                Drv1 = ((1 / (H ** 2)) * ((f1) - 2 * (f2) + (f3)))

            tolerancia = abs(Drv1 - Drv)
            Drv = Drv1
            iteracion = iteracion + 1
        self.ui.textdiferencia.setText(g)

    def obtener4(self):
        met = self.ui.comboingracion.itemText(self.ui.comboingracion.currentIndex())
        if met == "Trapecio":
            g = ""
            f = self.ui.inputfuncion_integracion.text()
            fx = sym.parse_expr(f)
            x = sym.Symbol('x')
            xo = self.ui.puntoXo.text()
            a = float(xo)
            xn = self.ui.inputXn.text()
            b = float(xn)
            val = self.ui.inputN.text()
            n = int(val)
            h = (b - a) / n
            suma = (fx.subs(x, a)) + (fx.subs(x, b))

            for i in range(n - 1):
                suma += (2 * (fx.subs(x, a + (h * (i + 1)))))
            integral = (h / 2) * suma

            g += "\n " + "suma: " + str(suma) + "\n " + "integral : " + str(integral) + "\n "
            self.ui.textintegracion.setText(g)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = Ui_aplication()
    mi_app.show()
    sys.exit(app.exec_())
