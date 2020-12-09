import math

print("Di quale figura vuoi calcolare l'area?")
print("1. QUADRATO")
print("2. RETTANGOLO")
print("3. TRIANGOLO")
print("4. CERCHIO")

scelta = input()

if scelta == "1":
    print("Quale dato conosci? ")
    print("1. Lato")
    print("2. Diagonale")
    print("3. Perimetro")
    dato = input()
    
    if dato == "1":
        l = int(input("Quanto misura il lato? "))
        l = float(l)
                
    elif dato == "2":
        d = int(input("Quanto misura la diagonale? "))
        l = d/(2**(1/2))
        
    else:
        perimetro = int(input("Quanto misura il perimetro? "))
        l = perimetro/4

    area = round(l**2,1)
    print("L'area del quadrato misura", area)
    
if scelta == "2":
    print("Quale dato conosci? ")
    print("1. Base e altezza")
    print("2. Diagonale e base/altezza")
    print("3. Perimetro e base/altezza")
    dato = input()
    
    if dato == "1":
        b = int(input("Quanto misura la base? "))
        h = int(input("Quanto misura l'altezza? "))      
        
    elif dato == "2":
        d = int(input("Quanto misura la diagonale? "))
        b = int(input("Quanto misura la base/altezza? "))
        h = (d**2 - b**2)**(1/2)  
    else:
        perimetro = int(input("Quanto misura il perimetro? "))
        b = int(input("Quanto misura la base/altezza? "))
        h = (perimetro - 2*b)/2

    area = round(b*h,1)
    print("L'area del rettangolo misura", area) 
      
if scelta == "3":
    b = int(input("Quanto misura la base? "))
    h = int(input("Quanto misura l'altezza? "))
    
    area = round(b*h/2,1)
    print("L'area del triangolo misura", area)
if scelta == "4":
    print("Quale dato conosci?")
    print("1. Raggio")
    print("2. Diametro")
    print("3. Circonferenza")
    dato = input()
    
    if dato == "1":
        r = int(input("Quanto misura il raggio? "))
       
    elif dato == "2":
        d = int(input("Quanto misura il diametro? "))
        r = d/2  
          
    else:
        C = int(input("Quanto misura la circonferenza? "))
        r = C/(2*math.pi)
        
    area = round(math.pi*(r**2),1)
    print("L'area del cerchio misura", area)