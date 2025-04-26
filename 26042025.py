# import random

# nm1=random.randrange(5,10)

# print("\nNumero aleatorio de 5 e 10: ",nm1)



# nm2=random.randrange(1,100)
# nm3=random.randrange(1,100)
# nm4=random.randrange(1,100)
# print("\n3 numeros aleatorios: ")
# print(nm2,nm3,nm4) 


# c=10
# while c>0:
#     print(c)
#     c=c-1
#     print("Fogo")


# npi=int(input("Digite um numero: "))

# for npi in range(npi):
#     if npi%2==0:
#         soma=npi+npi 


# print(soma)
# print("GOAT DO PYTHON")



# multi=int(input("Digite um numero para multiplicar de 1 a 10: "))



# for i in range(1,11):
#     x=multi*i
#     print(f"{multi} x {i} = {x}")






lista=[]

with open('arquivo.txt','r') as arq: 
    conteudo=arq.read()

    print(conteudo)

for n in conteudo:
    lista.append(n)
    print(lista)






