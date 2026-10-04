## TEST MERKAZI --> demo
from RotorSystem.Rotor_1 import Rotor1
from RotorSystem.Rotor_2 import Rotor2
from RotorSystem.Rotor_3 import Rotor3
from parameters import Parameters

"""
test_1 = Rotor1(sifreleme=Parameters.rotor_1_sifrelemesi, ornek_cumle=Parameters.test_cumlesi)
sifrelenmis_cumle, position = test_1.encrypt()
print(sifrelenmis_cumle)
"""


## Test 2
rotor_1_girdisi = Rotor1(sifreleme=Parameters.rotor_1_sifrelemesi, ornek_cumle=Parameters.test_cumlesi)
sifrelenmis_cumle, position, liste = rotor_1_girdisi.encrypt()
print(f"Rotor 1 ile sifrelenmis cumle --> {sifrelenmis_cumle}, Position --> {position}, liste --> {liste}")

rotor_2_girdisi = Rotor2(sifreleme=Parameters.rotar_2_sifrelemesi, ornek_cumle=sifrelenmis_cumle, rotor1_input=liste)
sifrelenmis_cumle2, position2, liste = rotor_2_girdisi.encrypt()
print(f"Rotor 2 ile sifrelenmis cumle --> {sifrelenmis_cumle2}, Position --> {position2}, liste --> {liste}")

rotor_3_girdisi = Rotor3(sifreleme=Parameters.rotor_3_sifrelemesi, ornek_cumle=sifrelenmis_cumle, rotor2_input=liste)
sifrelenmis_cumle3, position3 = rotor_3_girdisi.encrypt()
print(f"Rotor 3 ile sifrelenmis cumle --> {sifrelenmis_cumle3}, Position --> {position3}")

