n = int(input("Quante parole si vogliono inserire? "))
A = []
B = []
print("Dopo aver digitato ogni parola premere invio")
for i in range(n):
    parola = input()
    A.append(parola)
    B.append(len(parola))
print(B)


