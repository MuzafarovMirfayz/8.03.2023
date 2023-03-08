def Mikrob():
    n, doim, minut, soat, kun = int(input('N= ')), 1, 0, 0, 0
    while True:
        doim*=2
        minut+=1
        if n < doim*2:
            break
    if minut >= 60:
        soat = minut // 60
        minut = minut % 60
    if soat >= 24:
        kun = soat // 24
        soat = soat % 24
    if kun > 0:
        print(f"{kun}-kun", end=" ")
    if soat > 0:
        print(f"{soat}-soat", end=" ")
    if minut > 0:
        print(f"{minut}-minut")
Mikrob()