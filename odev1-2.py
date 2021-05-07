n=1
while n<6:
    sayiAl = int(input(str(n)+". sayıyı girin :"))
    n=n+1
    if sayiAl > 1:
        for i in range(2, sayiAl):
            if (sayiAl % i) == 0:
                print("Asal Değildir")
                break
        else:
            print(" Asaldır")
    else:
        print("Asal Değil")
