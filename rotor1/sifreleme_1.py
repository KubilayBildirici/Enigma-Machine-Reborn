
ornek_cumle = "benim adim kubilay"
alfabe = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotar_1_sifrelemesi = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotar_2_sifrelemesi = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    

    
def position_check(sifreleme: str, position: int) -> str:
    return sifreleme[position:] + sifreleme[:position]


def rotar(position: int, sifreleme: str) -> list:
    liste = []
    sifreleme = position_check(sifreleme=sifreleme, position=position)
    
    for harf, karsilik in zip(alfabe.lower(), sifreleme.lower()):
        liste.append((harf, karsilik))
    
    return liste


def sifreleme_1(ornek_cumle: str) -> str:   
    position = 0
    sifrelenmis_cumle = ""
        
    
    for i in ornek_cumle:
        liste = rotar(position, rotar_1_sifrelemesi)
        for x, y in liste:
            if i == x:
                sifrelenmis_cumle += y
                position += 1                

    return sifrelenmis_cumle


def sifreleme_2(ornek_cumle: str) -> str:
    position = 0
    sifrelenmis_cumle_2 = ""
    for i in ornek_cumle:
        liste = rotar(position, rotar_2_sifrelemesi)
        for x,y in liste:
            if i == x:
                sifrelenmis_cumle_2 += y
                position = (position + 6) % 26
    
    return sifrelenmis_cumle_2

        

dongu_1 = sifreleme_1(ornek_cumle)
dongu_2 = sifreleme_2(dongu_1)
print(dongu_1)



