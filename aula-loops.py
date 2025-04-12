print("---Sistema de notas de alunos para professores---")
notas=[]
nomes=[]




log=input("Digite o usuario: ")
senha=input("Digite sua senha: ")


while log!="Pedro" and senha!="prof123":

    for i in range(1,4):
        print(f"Tentivas: {i}")
        log=input("\nDigite o usuario novamente: ")
        senha=input("\nDigite a senha novamente: ")

    
    print("\nConta bloqueada")
    break 





if log =="Pedro" and senha =="prof123":

    for l in range(1,4):
        nota=int(input("Digite as notas:  "))
        notas.append[nota]





