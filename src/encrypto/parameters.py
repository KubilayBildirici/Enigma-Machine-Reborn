from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Parameters:
    test_cumlesi: str = "benim adim kubilay"

    alfabe: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    rotor_1_sifrelemesi: str = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

    rotar_2_sifrelemesi: str = "AJDKSIRUXBLHWTMCQGZNPYFVOE"

    rotor_3_sifrelemesi: str = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

    MORSE: ClassVar[dict] = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }
