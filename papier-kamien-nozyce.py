import random

while range(1):

    lista = ["kamien", "papier", "nozyce", "k", "p", "n"]
    
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
    print("a) Normalny - klasyczne papier, kamień, nożyce - do trzech zwycięskich rund")
    print("b) Bez limitu - rozgrywka bez limitu!")

    print(" ")

    while True:
        
        wybor = input("W jakim trybie chcesz zacząć grę? (N/B) ")

        if wybor not in ["n", "b", "N", "B"]:

            print(" ")
            
            print("Taki tryb nie istnieje, wybrałeś poprawnie?")

            print(" ")
            
            continue
        

        else:
            break
    print(" ")

    if wybor == "N" or "n":

        while True:

            potyczka += 1
        

            print("==========================")
            print("Bitwa numer:", potyczka, "| Normalny")
            print("==========================")
            
            print(" ")
            
            x = input("""Wybierz swoją broń: 
            - papier
            - kamien
            - nozyce

            """)
            y = random.randint(0,2)
            z = lista[y]

            print(" ")

            
            if x not in lista:

                potyczka += -1
                
                if x == "koniec":
                    exit()
                else:
                    print("Taka broń nie istnieje! Jesteś pewien wyboru?")
                    break


            if x in lista:

                w = "blad"
                if (x == "k" or "kamien"):
                    w = "kamien"

                if (x == "p" or "papier"):
                    w = "papier"

                if (x == "n" or "nozyce"):
                    w = "nozyce"
                
                if w == "blad":
                    print("Wystąpił błąd (zmienna w).")

                print(f"Komputer wybrał: {lista[y]}, Ty wybrałeś(-aś) {w}")

                if (z == "kamien") and (w == "papier"):
                    #print("Z - kamien + x - papier, gracz +1")
                    gracz += 1

                if (z == "kamien") and (w == "nozyce"):
                    #print("Z - kamien + x - nozyce, komp +1")
                    komputer += 1

                if (z == "papier") and (w == "kamien"):
                    #print("Z - papier + x - kamien, komp +1")
                    komputer += 1

                if (z == "papier") and (w == "nozyce"):
                    #print("Z - papier + x - nozyce, gracz +1")
                    gracz += 1

                if (z == "nozyce") and (w == "kamien"):
                    #print("Z - nozyce + x - kamien, gracz +1")
                    gracz += 1

                if (z == "nozyce") and (w == "papier"):
                    #print("Z - nozyce + x - papier, komp +1")
                    komputer += 1
                
                #print(komputer, gracz)   

                if z == w:
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
        print("Ilość Bitew   |       ", potyczka, "       |")
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
        break

    if wybor == "B" or "b":

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
                
                if x == "koniec":
                    break
                else:
                    print("Taka broń nie istnieje! Jesteś pewien wyboru?")
                    break


            if x in lista:
                print("komputer wybrał:", lista[y])

                if z == "kamien" or "k":
                    if x == "papier" or "p":
                        gracz += 1

                if z == "kamien" or "k":
                    if x == "nozyce" or "n":
                        komputer += 1

                if z == "papier" or "p":
                    if x == "kamien" or "k":
                        komputer += 1

                if z == "papier" or "p":
                    if x == "nozyce" or "n":
                        gracz += 1

                if z == "nozyce" or "p":
                    if x == "kamien" or "k":
                        gracz += 1

                if z == "nozyce" or "n":
                    if x == "papier" or "p":
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

        print(" ")

        print("=================================|")
        print("             WYNIK               |")
        print("---------------------------------|")
        print("              | Gracz | Komputer |")
        print("---------------------------------|")
        print("Liczba punktów|  ", gracz, "  |    ", komputer, "   |")
        print("---------------------------------|")
        print("Ilość Bitew   |       ", potyczka, "       |")
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