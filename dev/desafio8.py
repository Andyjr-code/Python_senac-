import os

op = int(input("Digite um mes: "))
match op:
    case 1: print("jan")
    case 2: print("fev")
    case 3: print("mar")
    case 4: print("abr")
    case 5: print("mai")
    case 6: print("jun")
    case 7: print("jul")
    case 8: print("ago")
    case 9: print("set")
    case 10: print("out")
    case 11: print("nov")
    case 12: print("dez")
    case _: print("invalido")

os.system("pause")
os.system('cls')