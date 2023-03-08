class time:
    def __init__(self, soat):
        self.soat = soat
        try:
            if int(self.soat.split(':')[0]) < 24 and int(self.soat.split(':')[1])<60 and int(self.soat.split(':')[2])<60:
                self.so = int(self.soat.split(':')[0])
                self.mi = int(self.soat.split(':')[1])
                self.se = int(self.soat.split(':')[2])
            if int(self.soat.split(':')[0]) == 24:
                self.so = 0
            else:
                self.so = int(self.soat.split(':')[0])
            if int(self.soat.split(':')[1]) == 60:
                self.mi = 0
            else:
                self.mi = int(self.soat.split(':')[1])
            if int(self.soat.split(':')[2]) == 60:
                self.se = 0
            else:
                self.se = int(self.soat.split(':')[2])

        except:
            pass
    def tek(self):
        if len(str(self.so))==1:
            self.so = f"0{self.so}"
        if len(str(self.mi))==1:
            self.mi = f"0{self.mi}"
        if len(str(self.se))==1:
            self.se = f"0{self.se}"
        self.soat = f"{self.so}:{self.mi}:{self.se}"
        print(self.soat)
    def hour(self):
        try:
            self.so = int(self.soat.split(':')[0])
            if self.so+5 == 24:
                self.so = 0
            elif self.so+5 > 24:
                self.so = self.so-19
            else: 
                self.so=self.so+5
            self.tek()
        except: print("Siz xato ma'lumot kiritingiz")
    def minut(self):
        try:
            self.mi = int(self.mi)
            if self.mi +5 == 60:
                self.so= int(self.so)+1
                self.mi = 0
            elif self.mi +5 > 60:
                self.so= int(self.so)+1
                self.mi = self.mi - 55
            else: 
                self.mi+=5
            if int(self.so) == 24:
                self.so = 0
            elif int(self.so) > 24:
                self.so = self.so-23
            self.tek()
        except: print("Siz xato ma'lumot kiritingiz")
    def sekund(self):
        try:
            self.se = int(self.se)
            if self.se+5 == 60:
                self.se = 0
                self.mi= int(self.mi) + 1
                if self.mi == 60:
                    self.so= int(self.so)+1
                    self.mi = 0
                elif self.mi  > 60:
                    self.so= int(self.so)+1
                    self.mi = self.mi - 55
                if self.so == 24:
                    self.so = 0
                elif self.so > 24:
                    self.so = self.so-23
            elif self.se+5 >60:
                self.se = self.se - 55
                self.mi= int(self.mi) + 1
                
                if self.mi == 60:
                    self.so= int(self.so)+1
                    self.mi = 0
                elif self.mi  > 60:
                    self.so= int(self.so)+1
                    self.mi = self.mi - 55
                
                
                if self.so == 24:
                    self.so = 0

            else:
                    self.se = self.se +5
            self.tek()
        except:print("Siz xato ma'lumot kiritingiz")
vaqt = time('23:59:60')
vaqt.hour()
vaqt.minut()
vaqt.sekund()