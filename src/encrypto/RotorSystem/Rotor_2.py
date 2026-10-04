"""
ROTOR - 2 --> MEKANIZMASI
rotor 1 girdinisi donusturur.
* Pozisyon her seferinde 6 artar.
"""

from RotorSystem.rotor import Rotor, rotate_wiring


class Rotor2(Rotor):
    def __new__(cls, sifreleme: str, ornek_cumle: str, rotor1_input: list):
        print(f"Rotor 2 Creating.. --> {cls.__name__}")
        instance = super().__new__(cls)
        return instance

    def __init__(self, sifreleme: str, ornek_cumle: str, rotor1_input: list) -> None:
        self.position = 0
        self.sifreleme = sifreleme
        self.ornek_cumle = ornek_cumle
        self.sifrelenmis_cumle = ""
        self.rotor1_input = rotor1_input

    def __repr__(self):
        return (
            f"Rotor2(position={self.position}, "
            f"sifreleme={self.sifreleme!r}, "
            f"ornek_cumle={self.ornek_cumle!r}, "
            f"sifrelenmis_cumle={self.sifrelenmis_cumle!r})"
        )

    def __str__(self):
        return (
            f"Rotor 2 - position: {self.position} "
            f"--> Sifrelenmis cumle: {self.sifrelenmis_cumle}"
        )

    def build_mapping(self) -> list[tuple[str, str]]:
        liste = []

        sifreleme = rotate_wiring(sifreleme=self.sifreleme, position=self.position)

        rotor_1_sifrelemesi = [tuple[1] for tuple in self.rotor1_input]

        for harf, karsilik in zip(rotor_1_sifrelemesi, sifreleme.lower()):
            liste.append((harf, karsilik))

        return liste

    def encrypt(self) -> tuple[str, int, list[tuple[str, str]]]:
        for i in self.ornek_cumle:
            liste = self.build_mapping()
            for x, y in liste:
                if i == x:
                    self.sifrelenmis_cumle += y
                    self.position = (self.position + 6) % 26
                    print(self.position)

        return (self.sifrelenmis_cumle, self.position, liste)
