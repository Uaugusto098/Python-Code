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

        if log=="Pedro" and senha=="prof123":
          break
    
    else:
        print("\nConta bloqueada")
        break

    
    

    
while log =="Pedro" and senha =="prof123":

    aluno=input("Digite o nome do aluno: ")

    for l in range(1,4):
        nota=int(input("Digite as notas do aluno:  "))
        notas.append(nota)
      
    media=(notas[0] + notas[1] +notas[2] )/len(notas)

    print(f"Nota média do aluno: {aluno} \n é de: \n{media}  ")

    
    




