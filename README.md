# **IMPLEMENTACIÓN DE ALGORITMO DE DEUTSCH Y DEUTSCH-JOZSA**

En este trabajo se siguieron los siguentes pasos para hacer la entrega del reporte final.

1. Implemente las 4 funciones posibles de {0,1} a {0,1} usando el computador cuántico de IBM.

- Dibujo de función
- Matriz correpondiente
- Circuito correspondiente
- Resultados de las 4 pruebas

2. Verifique que el algoritmos de Deutsch funciona para comprobar cuáles de estas funciones son balanceadas o constantes.

- Circuito
- Resultados

3. Implemente al menos 4 funciones con n= 4 (3 balanceadas y una constante) para probar el funcionamiento del algoritmo Deustch-Jozsa

- Dibujo función
- Matriz correspondiente (Generada por computador)
- Circuito
- Pruebas
- Prueba del experimento Deutsch-Jozsa

4. Explique sus resultados.

- En cada sección explique sus resultados con textos y ecuaciones.

---

## 📲 Pre-requisitos

*Esto necesitaras para correr la librería:*

IDLE Python, librerías de Qiskit para ejectutar los archivos:

`QuantumCircuit, transpile, Aer, plot_histogram, matplotlib.pyplot`

Se deben descargar los archivos .py en este repositorio, las carpetas solo están por tema de organización pero no es necesaria su descarga.

## 🌊 Ejecutando las pruebas

Encontraras 5 tipos de archvos .py en este repositorio, 

*aCero.py, aUno.py, Cruzados.py, Iguales.py* pertenecen a las funciones iniciales.

*aCeroD.py*, *aUnoD.py*, *CruzadosD.py*, *IgualesD.py* pertenecen a las funciones iniciales usando el algoritmo de Deutsch.

En *funciones.py* encontrarás los circuitos solicitados del punto #4

En funcionesDeutschJozsa.py encontrarás los solicitados del punto #4 aplicando el algoritmo de Deutsch Jozsa

En Pruebas.py encontrarás las pruebas de los anteriores archivos por medio del unit test, podrás verificar si las funciones son correctas. 

***IMPORTANTE:*** en su ejecución salen los siguientes errores, sin embargo, no afecta en la visualización de los resultados.

```python
ImportWarning: **package** != **spec**.parent
from . import noise
ImportWarning: __package__ != __spec__.parent
from . import utils
ImportWarning: __package__ != __spec__.parent
from .version import __version__
PendingDeprecationWarning: The qiskit.Aer entry point will be deprecated in a future release and subsequently removed. Instead you should use this directly from the root of the qiskit-aer package.
simulator = Aer.get_backend('qasm_simulator')
PendingDeprecationWarning: The `QasmSimulator` backend will be deprecated in the future. It has been superseded by the `AerSimulator` backend.
warn('The `QasmSimulator` backend will be deprecated in the'
```

## RESULTADOS

A la par de la creación de los programas se realizó un reporte que contiene la discusión de los resultados presentados que encontrarás en REPORTE Ana Duran.pdf

## **Autor ✒️**

- **Ana María Durán Burgos** - *IMPLEMENTACIÓN DE ALGORITMO DE DEUTSCH Y DEUTSCH-JOZSA* **-** [anndr0](https://github.com/anndr0)
