recommencer = True

while recommencer == 1:
    n1 = int(input("donne moi un numéro! : "))
    op = input("ok maintenant dis moi quelle opération tu veux faire (+, /, -, *)")
    n2 = int(input("maintenant donne moi un second numéro : "))

    if op == '+':
        print("le résultat est", n1 + n2,"!!!!")
    elif op == '-':
        print("le résultat est", n1 - n2, "!!!")
    elif op == '/':
        print("le résultat est", n1 / n2, "!!!")
    elif op == '+':
        print("le résultat est", n1 + n2, "!!!")
    recommencer = int(input("veux tu faire un autre calcul? 1. oui 2. non"))
    if recommencer == 2:
        print("ok bye bye!!"); break 