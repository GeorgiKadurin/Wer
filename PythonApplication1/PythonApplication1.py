from math import*
from random import*

#0
while True:
    print("Tere Tulemast")
    try:
        print("Latte,2.50 euro. ")
        print("Espresso,2 euro. ")
        print("Cappuccino,3 euro. ")
        print("Kakao,2.20 euro. ")
        s=float(input("Sisestaga summa: "))
        
        if s<2 or s>3: break
        m=input("Valiga makseviis: " )
        if m.lower()=="sularaha":
            print("anna raha")

        if m.lower()=="kaardiga":
            n=int(input("Sisestaga kaardi number: "))
            print(n,"selle kaardiga on tehtud maksa. ")

    except:
        print("")


#1
while True:
     try:
        nimi=input("Palun sisesta oma nimi: ")
        if nimi=="SIIM":
            n=int(input("Palun sisesta mitu korda soovid tervitus saada: "))
        for i in range(1, n+1):
            print(f"Ole tervitatud, {nimi}, {i}, korda. ")
        else:
         break
     except:
         print()


#
katsed=0
answer=""
while answer.lower()!="komm":
    answer=input("Taham kommi!")
    katsed+=1
print(f"Katsed: {katsed}")
print()


#22
print("Ma tahan komm. ")
katsed=0
while True:
    answer=input("Tahan komi!")
    katsed+=1
    if answer.lower()!="komm":
        print(f"Teit kommid kirjutakse kulus {katsed} katse.")
        break


   
#0
p=0
while True:
    number = int(input("Sisestage number suurem kui 10:"))
    p+=1
    if number >=10: 
        print("Õigesti")
        break 
    else:
        print("Arv on liiga väike")
print("katsed", p)

#11
print("Arvuti mõstatab numbrit 1-10 ja sina üritad seda ära arvut. ")
a=randint (1,10)
vastus=int(input("mis arv on mõistatud arvutit? "))
k=p=1
while vastus!=a:
    print("Ära sa ei arvanud ära, proovi uuesti! ")
    vastus=int(input("Sisesta vastus. "))
    k+=1
    p+=1
    if k>2:
        print("Püüdlused on lõppenud.  ")
        b=input("Kas proovi veel kord.  ")
        if b.upper()=="JÄH":
            k=0
            continue
        else:
            break 
if vastus==a:
    print("Palju õnne, sa arvasid ära!" ,p)
    
print()
