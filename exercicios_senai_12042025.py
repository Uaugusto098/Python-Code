#  ***1*** 

#  ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***


# def comparar():
#     x=int(input("Digite um numero: "))

#     y=int(input("Digite um numero"))

#     if x %2==0:

#         print(f"O primeiro numero {x} é par ")
#     else:

#         print(f"O primeiro numero {x} é impar")

#     if y%2==0:
#         print(f"O segundo numero {y} é par ")

#     else:
        
#         print(f"O segundo numero {y} é impar")

# comparar()



# ***2***

# ***CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***



# def multi():
#     lista=[]

#     for i in range(1,4):
#         i=int(input("Digite um numero: "))
#         lista.append(i)
#     conta=(lista[0]*lista[1]*lista[2])

#     print(conta)





# multi()


# ***3***

# ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***


# def elevado():

#     z=int(input("Digite um numero: "))
#     c=int(input("Digite o segundo numero: "))

#     conta=z**c
#     print(f"O numero base é {z}")
#     print(f"O numero elevado é {c}") 
#     print(f"Resultado: {conta}")

# elevado()

#**4**

# CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.



# def identificador(x):

#     if x==18:
#         print("Esta pessoa tem 18 anos !! ")


# usuario=input("Digite seu nome ")

# idade=int(input("Digite sua idade: "))

# identificador(idade)

# print(f"\nFicha de cadastro: \n{usuario} \n{idade} anos")

# if idade==18:
#     print("\n---Cadastro validado---")
# else:
#     print("Cadastro inválido")



# **5**

# ***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***


def idade(anon,anoa):

    return anoa-anon


nascimento=int(input("Digite seu ano de nascimento: "))

atual=int(input("Digite o ano atual: "))



print(f"\nIdade atual: {idade(nascimento,atual)}") 
        



    















    






