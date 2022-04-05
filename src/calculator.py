
from konsoli_io import KonsoliIO

KOMENNOT = {
    "x": "x lopeta",
    "1": "1 add number1 + number2",
    "2": "2 distract number1 - number2",
}


class Calculator:
    def __init__(self, number1, number2):
        self._io = KonsoliIO()
        self.number1 = number1
        self.number2 = number2

    def kaynnista(self):
        self._io.tulosta("Calculator")
        self._tulosta_ohje()

        while True:
            komento = self._io.lue("komento: ")

            if not komento in KOMENNOT:
                self._io.tulosta("virheellinen komento")
                self._tulosta_ohje()
                continue

            if komento == "x":
                break
            elif komento == "1":
                self._add_number()
            elif komento == "2":
                self._dist_number()

    def _add_number(self):
        number1 = self._io.lue("enter first number: ")
        number2 = self._io.lue("enter second number: ")
        temp = number1+number2
        self._io.tulosta(temp)

    def _dist_number(self):
        number1 = self._io.lue("enter first number: ")
        number2 = self._io.lue("enter second number: ")
        temp = number1-number2
        self._io.tulosta(temp)