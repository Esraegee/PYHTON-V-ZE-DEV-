
def yemeklistesi():
    with open("liste.txt","r") as yemekdosya:
        for yemekadi in yemekdosya:
            print(yemekadi)

def yemekyaz():
    yemekadi=input("bir yemek adı giriniz:")
    with open("liste.txt","x")as yemekdosya:
        yemekdosya.write(yemekadi + '/n')

def malzemeyaz():
    malzemeler=input('Gereken malzemeleri yazınız :')

    with open("liste.txt","x")as yemekdosya:
        yemekdosya.write(malzemeler + '/n')
 
        while True:
            yemek=input('1:yemeklistesi /n  2:yemekyaz /n  3:malzemeyaz /n  4:bitiş /n')
            if yemek=='1':
                yemeklistesi()
            elif yemek=='2':
                yemekyaz()
            elif yemek=='3':
                malzemeyaz()
            else:
                break
