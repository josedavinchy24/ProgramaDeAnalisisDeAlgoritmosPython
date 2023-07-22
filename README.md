# ProgramaDeAnalisisDeAlgoritmosPython

[![Alt text](https://img.youtube.com/vi/37CqS714ybk/0.jpg)](https://www.youtube.com/watch?v=37CqS714ybk)

El programa desarrollado en Python con una interfaz gráfica creada con Qt Designer, que resuelve problemas de análisis de algoritmos utilizando varios métodos. Los métodos incluidos son el método de Newton, el método por intervalos (que utiliza la bisección y la regla falsa), la diferencia numérica y la integración numérica.

El programa está diseñado para recibir diferentes parámetros según el método seleccionado y devuelve una serie de valores y resultados correspondientes a cada método. Además, genera una representación gráfica de los resultados en un plano cartesiano.

Método de Newton:
En este método, se debe ingresar una función, el error y una aproximación inicial para la raíz. El programa devuelve los valores de F(X), F'(X), el error, la raíz y la cantidad de iteraciones realizadas. Además, muestra la gráfica de la función y la aproximación de la raíz en el plano cartesiano.

Método por intervalos:
Este método tiene dos opciones: bisección y regla falsa. Se deben ingresar una función, el error, el punto inicial y el punto final del intervalo. El programa devuelve los valores de límite inferior, límite superior, punto medio (xm), f(a), f(xm) y el error correspondiente. También muestra la gráfica de la función y los intervalos de búsqueda en el plano cartesiano.

Diferencia numérica:
En este método, se ofrecen opciones para calcular la diferencia utilizando dos puntos, tres puntos y la segunda derivada. Se deben ingresar una función, el error, un valor de paso (h) y un punto de referencia. El programa devuelve los valores de f, Xo, H, la derivada calculada y el error correspondiente. Además, muestra la gráfica de la función y los puntos utilizados para el cálculo en el plano cartesiano.

Integración numérica:
Este método requiere ingresar una función, un punto inicial (xo), un punto final (xn) y un número de intervalos (n). El programa devuelve la suma total y el resultado de la integral. También muestra la gráfica de la función y las áreas bajo la curva en el plano cartesiano.

El programa combina la funcionalidad de estos métodos con una interfaz gráfica intuitiva creada con Qt Designer, lo que facilita su uso y comprensión. Esta aplicación en Python puede ser útil para aquellos que necesiten resolver problemas de análisis de algoritmos y deseen utilizar diferentes métodos para encontrar soluciones numéricas y aproximadas, además de visualizar los resultados en un plano cartesiano.

