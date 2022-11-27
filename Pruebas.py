import unittest
import aCero, aUno, Cruzados, Iguales
import aCeroD, aUnoD, CruzadosD, IgualesD
import funciones, funcionesDeutschJosza


class MytestCase(unittest.TestCase):
    global __package__

    def test(self):
        print("PRUEBAS FUNCIONES")
        self.assertEqual(aCero.Test(), [{'00': 1000}, {'01': 1000}, {'10': 1000}, {'11': 1000}])
        self.assertEqual(aUno.Test(), [{'01': 1000}, {'00': 1000}, {'11': 1000}, {'10': 1000}])
        self.assertEqual(Cruzados.Test(), [{'01': 1000}, {'00': 1000}, {'10': 1000}, {'11': 1000}])
        self.assertEqual(Iguales.Test(), [{'00': 1000}, {'01': 1000}, {'11': 1000}, {'10': 1000}])

        print("Funciones Deutsch")
        self.assertEqual(aCeroD.Test(), [{'0': 1000}]) # Constante
        self.assertEqual(aUnoD.Test(), [{'0': 1000}])   # Constante
        self.assertEqual(CruzadosD.Test(), [{'1': 1000}])   # Balanceada
        self.assertEqual(IgualesD.Test(), [{'1': 1000}])    # Balanceada

        print("Funciones Deutsch Jozsa")
        print("\nFunciones:")
        self.assertEqual(funciones.Test(), [{'01010': 1000},{'00010': 1000},{'00100': 1000},{'00000': 1000}])
        print("Funciones n = 4")
        self.assertEqual(funcionesDeutschJosza.Test(), [{'1111': 1000},{'0001': 1000},{'0011': 1000},{'0000': 1000}])


    if __name__ == "__main__" and __package__ is None:
        __package__ = "expected.package.name"
        unittest.main()