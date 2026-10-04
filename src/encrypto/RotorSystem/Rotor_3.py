"""
ROTOR - 3 --> MEKANIZMASI
rotor 2 girdinisi donusturur.
* Pozisyon her seferinde 9 artar.
"""

from RotorSystem.rotor import Rotor, rotate_wiring


class Rotor3(Rotor):
    def __new__(cls, sifreleme: str, ornek_cumle: str, rotor2_input: list):
        print(f"Rotor 3 Creating.. -> {cls.__new__}")
        instance = super().__new__(cls)
        return instance

    def __init__(self, sifreleme: str, ornek_cumle: str, rotor2_input: list):
        self.position = 0
        self.sifreleme = sifreleme
        self.ornek_cumle = ornek_cumle
        self.sifrelenmis_cumle = ""
        self.rotor2_input = rotor2_input

    def __repr__(self):
        return (self.position, self.sifreleme, self.ornek_cumle, self.sifrelenmis_cumle)

    def __str__(self):
        return (
            f"Rotor 3 - position: {self.position} --> "
            f"Sifrelenmis cumle: {self.sifrelenmis_cumle}"
        )

    def build_mapping(self) -> list:
        liste = []

        sifreleme = rotate_wiring(sifreleme=self.sifreleme, position=self.position)

        rotor_2_sifrelemesi = [tuple[1] for tuple in self.rotor2_input]

        for harf, karsilik in zip(rotor_2_sifrelemesi, sifreleme.lower()):
            liste.append((harf, karsilik))

        return liste

    def encrypt(self) -> tuple:
        for i in self.ornek_cumle:
            liste = self.build_mapping()
            for x, y in liste:
                if i == x:
                    self.sifrelenmis_cumle += y
                    self.position = (self.position + 9) % 26
                    print(self.position)

        return (self.sifrelenmis_cumle, self.position)
