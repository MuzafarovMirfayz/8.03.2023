from datetime import date
def sana(sana1:list, sana2:list):
    if date(int(sana1[0]), int(sana1[1]), int(sana1[2])) < date(sana2[0], sana2[1], sana2[2]):print(f"{((date(sana1[0], sana1[1], sana1[2]) - date(sana2[0], sana2[1], sana2[2])).days)*(-1)} kun")
    else:print(f"{((date(sana1[0], sana1[1], sana1[2]) - date(sana2[0], sana2[1], sana2[2])).days)} kun") 
sana([2005, 9, 10], [2023, 2, 16])