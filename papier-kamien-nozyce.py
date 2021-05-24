import random

while range(1):

    lista = ["kamien", "papier", "nozyce"]
    komputer = 0
    gracz = 0
    potyczka = 0

    print(" ")

    print("==========================")
    print("Gra w papier kamien nozyce")
    print("==========================")

    print(" ")

    print("Dostępne bronie:")
    print("- papier")
    print("- kamien")
    print("- nozyce")

    print("")

    print("Jeśli chcesz skończyć grę, wpisz \"koniec\"")

    print(" ")
    print("Tryby gry:")
    print("a) Normalny - klasyczne papier, kamien nozyce (bez drugiej szansy)")
    print("b) Bez konca - w normalnej rozgrywce grasz do trzech zwycięskich rund, tutaj w nieskończoność!")

    print(" ")

    while True:
        
        wybor = input("W jakim trybie chcesz zacząć grę? (N/B) ")

        if wybor not in ["N", "B"]:

            print(" ")
            
            print("Nie rozumiem, możesz wpisać ponownie?")

            print(" ")
            
            continue
        
        
        else:
            break
    print(" ")

    if wybor == "N":

        while True:

            potyczka += 1
            
            print("==========================")
            print("Bitwa numer:", potyczka, "| Normalny")
            print("==========================")
            
            print(" ")
            
            x = input("Wybierz swoją broń: ")
            y = random.randint(0,2)
            z = lista[y]

            print(" ")

            
            if x not in lista:

                potyczka += -1
                
                if x[0] == "k":
                    if x != "koniec":
                        print(">Bitwa odwołana. Miałeś na myśli kamien? (niezły wybór). Pozostałe rodzaje broni: papier, nozyce")
                        print(" ")
                                
                if x[0] == "p":
                    print(">Bitwa odwołana. Miałeś na myśli papier? (niezły wybór). Pozostałe rodzaje broni: kamien, nozyce")
                    print(" ")
                                    
                if x[0] == "n":
                    print(">Bitwa odwołana. Miałeś na myśli nozyce? (niezły wybór). Pozostałe rodzaje broni: papier, kamien")
                    print(" ")

                if x[0] != "k":
                    if x[0] != "p":
                        if x[0] != "n":
                            print(">Bitwa odwołana. Niestety, nie wiem o jaką broń ci chodzi. Wybierz kamien, papier albo nozyce")
                            print(" ")

            if x == "koniec":
                break
                
            if x in lista:
                print("komputer wybrał:", lista[y])

                if z == "kamien":
                    if x == "papier":
                        gracz += 1

                if z == "kamien":
                    if x == "nozyce":
                        komputer += 1

                if z == "papier":
                    if x == "kamien":
                        komputer += 1

                if z == "papier":
                    if x == "nozyce":
                        gracz += 1

                if z == "nozyce":
                    if x == "kamien":
                        gracz += 1

                if z == "nozyce":
                    if x == "papier":
                        komputer += 1
                        
                if z == x:
                    print(" ")
                    print("        >>REMIS<<")
                    
                print(" ")
                print("     |-------------|")
                print("     | WYNIK BITEW |")
                print("     |-------------|")
                print("     |  K   |  G   |")
                print("     |-------------|")
                print("     | ", komputer, "  | ", gracz,"  |")
                print("     |-------------|")
                print(" ")
                print(" ")
                        
                if gracz == 3:
                    break
                
                elif komputer == 3:
                    break

        print(" ")

        print("=================================|")
        print("             WYNIK               |")
        print("---------------------------------|")
        print("              | Gracz | Komputer |")
        print("---------------------------------|")
        print("Liczba punktów|  ", gracz, "  |    ", komputer, "   |")
        print("---------------------------------|")
        if potyczka > 9:
            print("Ilość Bitew   |       ", potyczka, "       |")
        else:
            print("Ilość Bitew   |       ", potyczka, "        |")
        print("---------------------------------|")
        if gracz == 3:
            print("Zwycięzca     |      Gracz       |")    
        else:
            print("Zwycięzca     |     Komputer     |")    
        print("---------------------------------|")
        if gracz == 3:
            print("Przewaga      |       ", gracz-komputer, "        |")

        else:
            print("Przewaga      |       ", komputer-gracz, "        |")
        print("=================================|")

            
    if wybor == "B":

        while True:

            potyczka += 1
            
            print("==========================")
            print("Bitwa numer:", potyczka, "| Bez Konca")
            print("==========================")
            
            print(" ")
            
            x = input("Wybierz swoją broń: ")
            y = random.randint(0,2)
            z = lista[y]

            print(" ")

            
            if x not in lista:

                potyczka += -1
                
                if x[0] == "k":
                    if x != "koniec":
                        print(">Bitwa odwołana. Miałeś na myśli kamien? (niezły wybór). Pozostałe rodzaje broni: papier, nozyce")
                        print(" ")
                                
                if x[0] == "p":
                    print(">Bitwa odwołana. Miałeś na myśli papier? (niezły wybór). Pozostałe rodzaje broni: kamien, nozyce")
                    print(" ")
                                    
                if x[0] == "n":
                    print(">Bitwa odwołana. Miałeś na myśli nozyce? (niezły wybór). Pozostałe rodzaje broni: papier, kamien")
                    print(" ")

                if x[0] != "k":
                    if x[0] != "p":
                        if x[0] != "n":
                            print(">Bitwa odwołana. Niestety, nie wiem o jaką broń ci chodzi. Wybierz kamien, papier albo nozyce")
                            print(" ")

            if x == "koniec":
                break
                
            if x in lista:
                print("komputer wybrał:", lista[y])

                if z == "kamien":
                    if x == "papier":
                        gracz += 1

                if z == "kamien":
                    if x == "nozyce":
                        komputer += 1

                if z == "papier":
                    if x == "kamien":
                        komputer += 1

                if z == "papier":
                    if x == "nozyce":
                        gracz += 1

                if z == "nozyce":
                    if x == "kamien":
                        gracz += 1

                if z == "nozyce":
                    if x == "papier":
                        komputer += 1
                        
                if z == x:
                    print(" ")
                    print("        >>REMIS<<")
                    
                print(" ")
                print("     |-------------|")
                print("     | WYNIK BITEW |")
                print("     |-------------|")
                print("     |  K   |  G   |")
                print("     |-------------|")
                if komputer > 9:
                    if gracz < 10:
                        print("     | ", komputer, " | ", gracz,"  |")

                if gracz > 9:
                    if komputer < 10:
                        print("     | ", komputer, "  | ", gracz," |")

                if komputer > 9:
                    if gracz > 9:
                        print("     | ", komputer, " | ", gracz," |")

                else:
                    print("     | ", komputer, "  | ", gracz,"  |")
                    
                print("     |-------------|")
                print(" ")
                print(" ")

        print(" ")

        print("=================================|")
        print("             WYNIK               |")
        print("---------------------------------|")
        print("              | Gracz | Komputer |")
        print("---------------------------------|")
        print("Liczba punktów|  ", gracz, "  |    ", komputer, "   |")
        print("---------------------------------|")
        if potyczka > 9:
            print("Ilość Bitew   |       ", potyczka, "       |")
        else:
            print("Ilość Bitew   |       ", potyczka, "        |")
        print("---------------------------------|")
        if gracz == 3:
            print("Zwycięzca     |      Gracz       |")    
        else:
            print("Zwycięzca     |     Komputer     |")    
        print("---------------------------------|")
        if gracz == 3:
            print("Przewaga      |       ", gracz-komputer, "        |")

        else:
            print("Przewaga      |       ", komputer-gracz, "        |")
        print("=================================|")    
