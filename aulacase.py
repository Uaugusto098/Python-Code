# print("\nVerificar se o numero é impar ou par ")


# variav=int(input("\nDigite um numero: "))


# match variav%2:

#     case 0:
#         print("O numero é par")
    
#     case _:
#         print("Este numero é impar")


# print("\nVerificar se o numero é negativo,positivo ou zero")


# verif=float(input("Digite um numero para a verificação: "))


# match verif:
    

#     case verif if verif<0:
#         print("Este numero é negativo")

#     case verif if verif>0:
#         print("Este numero é positivo")

#     case verif if verif==0:
#         print("Este numero é nulo")
    
#     case _:
#         print("Numero invalido,reinicie o sistema")




# Vazio=input("Digite algo")



# match Vazio:        


#     case Vazio if Vazio=="":
#         print("Essa string é vazia")

#     case _:
#         print("Esssa string contem algum dado")





    
# num=int(input("Digite um numero para a comparação "))

# match num:

#     case num if num>10:
#         print("Este numero é maior que 10")
#     case num if num<10:
#         print("Este numero é menor que 10")
    
#     case num if num==10:
#         print("Este numero é igual que 10")

idade=int(input("Informe sua idade: "))


match idade:

    case idade if idade<=12:
        print("Classificação: infantil")
    case idade if idade<=17:
        print("Classificação: Adolescente")
    case idade if idade<=35:
        print("Classificação: Jovem")
    case idade if idade>65:
        print("Classificação: Idoso")
    case _:
        print("Classificação: Adulto")


