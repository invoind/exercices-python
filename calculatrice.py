recommencer = True

def mul(n1, n2):
    return n1 * n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    if n2 == 0:
        print("pas de division par zéro!")
    else:
        return n1 / n2

def add(n1, n2):
    return n1 + n2

while recommencer == True:
    n1 = int(input("écris un nombre stp ! : "))
    op = input("maintenant précise l'opération que tu veux effectuer (+, -, /, *)")
    n2 = int(input("et maintenant donne un deuxième nombre! : "))

    addition = add(n1, n2)
    soustraction = sub(n1, n2)
    multiplication = mul(n1, n2)
    division = div(n1, n2)

    if op == '+':
        print("le résultat est", addition, "!!")
    elif op == '-':
        print("le résultat est", soustraction, "!!" )
    elif op == '/':
        print("le résultat est", division, "!!")
    elif op == '*':
        print("le résultat est", multiplication, "!!")
    elif len(op) >= 1:
        print("calcul impossible, recommence!")

    reponse = int(input("veux tu réaliser une autre opération? 1. oui 2. non"))

    if reponse == "2":
        print("ok bye!"); break
