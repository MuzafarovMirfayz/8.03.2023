def harf_raqam():
    ism1, ism2, raqam1, raqam2 = input("Birinchi ismni kiriting-> ").lower(), input("Ikkinchi ismni kiriting-> ").lower(), "", ""
    al = {'a':1, "b":2, 'c':3, "d":4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, "q":17, "r":18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    for i in range(len(ism1)):
        raqam1 = raqam1 + str(al[ism1[i]])
    for i in range(len(ism2)):
        raqam2 = raqam2 + str(al[ism2[i]])
    print(f"{raqam1} + {raqam2} = {int(raqam1)+int(raqam2)}")
harf_raqam()