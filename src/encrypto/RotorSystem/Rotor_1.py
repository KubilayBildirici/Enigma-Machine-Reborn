"""
ROTOR - 1 --> MEKANIZMASI

* Girdi -> Rotor 1 -> Farkli harfe donustur
* her tusa basildiginda bir pozisyon ilerler
* en hizli hareket eden rotordur.
* Pozisyon her seferinde 1 artar.
"""

from parameters import Parameters

from RotorSystem.rotor import Rotor, rotate_wiring


class Rotor1(Rotor):
    def __new__(cls, sifreleme: str, ornek_cumle: str):
        print(f"Rotor 1 Creating.. --> {cls.__name__}")
        instance = super().__new__(cls)
        return instance

    def __init__(self, sifreleme: str, ornek_cumle: str) -> None:
        self.position = 0
        self.sifreleme = sifreleme
        self.ornek_cumle = ornek_cumle
        self.sifrelenmis_cumle = ""

    def __repr__(self):
        return (self.position, self.sifreleme, self.ornek_cumle, self.sifrelenmis_cumle)

    def __str__(self):
        return (
            f"Rotor 1 - position: {self.position} --> "
            f"Sifrelenmis cumle: {self.sifrelenmis_cumle}"
        )

    def build_mapping(self) -> list[tuple[str, str]]:
        liste = []

        sifreleme = rotate_wiring(self.sifreleme, position=self.position)

        for harf, karsilik in zip(
            Parameters.alfabe.lower(), sifreleme.lower(), strict=True
        ):
            liste.append((harf, karsilik))

        return liste

    def encrypt(self) -> tuple:
        for i in self.ornek_cumle:
            liste = self.build_mapping()
            for x, y in liste:
                if i == x:
                    self.sifrelenmis_cumle += y
                    self.position = (self.position + 1) % 26
                    print(self.position)

        return (self.sifrelenmis_cumle, self.position, liste)
