from abc import ABC, abstractmethod


def rotate_wiring(sifreleme: str, position: int) -> str:
    return sifreleme[position:] + sifreleme[:position]


class Rotor(ABC):
    """
    Temel Rotor mekanizmasidir.
    Her 3 rotor da bu mekanizmaya uyacak sekilde yazilmalidir.
    """

    @abstractmethod
    def build_mapping(self):
        """
        pozisyon her arttiginda guncel olan harf - sifreleme mapping ini dondurur
        """
        pass

    @abstractmethod
    def encrypt(self):
        """
        mapping e gore girdiyi sifreler
        """
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
