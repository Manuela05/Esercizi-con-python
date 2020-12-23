'''Scrivere un programma che a scelta dell'utente calcoli l'area di un quadrato, rettangolo, triangolo o cerchio.'''

import math

print('''Di quale figura vuoi calcolare l'area?
1. QUADRATO
2. RETTANGOLO
3. TRIANGOLO
4. CERCHIO''')

scelta = input()

if scelta == "1":
    print('''Quale dato conosci?
    1. Lato
    2. Diagonale
    3. Perimetro''')
    dato = input()
    
    if dato == "1":
        l = float(input("Quanto misura il lato? "))
                
    elif dato == "2":
        d = float(input("Quanto misura la diagonale? "))
        l = d/(2**(1/2))
        
    else:
        perimetro = float(input("Quanto misura il perimetro? "))
        l = perimetro/4

    area = round(l**2,1)
    print("L'area del quadrato misura", area)
    
if scelta == "2":
    print('''Quale dato conosci?
    1. Base e altezza
    2. Diagonale e base/altezza
    3. Perimetro e base/altezza''')
    dato = input()
    
    if dato == "1":
        b = float(input("Quanto misura la base? "))
        h = float(input("Quanto misura l'altezza? "))      
        
    elif dato == "2":
        d = float(input("Quanto misura la diagonale? "))
        b = float(input("Quanto misura la base/altezza? "))
        h = (d**2 - b**2)**(1/2)  
    else:
        perimetro = float(input("Quanto misura il perimetro? "))
        b = float(input("Quanto misura la base/altezza? "))
        h = (perimetro - 2*b)/2

    area = round(b*h,1)
    print("L'area del rettangolo misura", area) 
      
if scelta == "3":
    b = float(input("Quanto misura la base? "))
    h = float(input("Quanto misura l'altezza? "))
    
    area = round(b*h/2,1)
    print("L'area del triangolo misura", area)
if scelta == "4":
    print('''Quale dato conosci?
    1. Raggio
    2. Diametro
    3. Circonferenza''')
    dato = input()
    
    if dato == "1":
        r = float(input("Quanto misura il raggio? "))
       
    elif dato == "2":
        d = float(input("Quanto misura il diametro? "))
        r = d/2  
          
    else:
        C = float(input("Quanto misura la circonferenza? "))
        r = C/(2*math.pi)
        
    area = round(math.pi*(r**2),1)
    print("L'area del cerchio misura", area)