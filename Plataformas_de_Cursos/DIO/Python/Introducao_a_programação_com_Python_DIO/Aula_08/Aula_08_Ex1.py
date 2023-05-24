class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 1

    def power(self):
        if self.ligada: # Ele ja subentende que é == True / Caso queira colocar false use if not self.ligada
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        self.canal +=1

    def diminui_canal(self):
        self.canl -=1

if __name__ == '__main__':
    tv = TV()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)

    tv.aumenta_canal()
    tv.aumenta_canal()
    tv.diminui_canal()