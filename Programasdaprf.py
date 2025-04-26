# # variveis globais



# carga = float(input('digite hora/mês '))
# salario =  float(input('Salario'))
# calculo_hora = salario/carga
# extra = calculo_hora * 1.5
# quant_hora_extra = float(input('Quantidade hora extra: '))
# Adcional_notuno_quant = int(input('Horas noturnas'))
# hex_n = calculo_hora * 1.2




  


# def valorhora():
#     print('Horas R$:', round(calculo_hora,2))
#     print('Hora extra 50% R$ ', round(extra,2))
#     print('Quantidade realizada hora extra:',round(quant_hora_extra,2) )
#     print('Hora extra noturna R$',round( hex_n,2))


# # RETURN X PRINT



# def sistema_de_horas():
#     print('Seja bem vindo ao sistema de horas')
#     # opcoes = ['','Horas'  ]
#     escolha = input('Deseja fazer o calculo de horas? s/n')
#     if escolha == 's':
#         valorhora() 
#     else:
#         print('Saindo do sistema...')    



# sistema_de_horas()



# # def cumprimentar():
# #     print('Seja bem vindo ao sistema de horas')


# # def valorhora():
# #     carga = float(input('digite hora/mês '))
# #     salario =  float(input('Salario'))


# #     calculo_hora = salario/carga
# #     extra = calculo_hora * 1.5
# #     quant_hora_extra = float(input('Quantidade hora extra: '))
# #     Adcional_notuno_quant = int(input('Horas noturnas'))
# #     hex_n = calculo_hora * 1.2



# #     print('Horas R$:', round(calculo_hora,2))
# #     print('Hora extra 50% R$ ', round(extra,2))
# #     print('Quantidade realizada hora extra:',round(quant_hora_extra,2) )
# #     print('Hora extra noturna R$',round( hex_n,2))


# # # RETURN X PRINT



# # def sistema_de_horas():
# #     cumprimentar()
# #     # opcoes = ['','Horas'  ]
# #     escolha = input('Deseja fazer o calculo de horas? s/n')
# #     if escolha == 's':
# #         valorhora() 
# #     else:
# #         print('Saindo do sistema...')    



# # sistema_de_horas()


# # ## ATIVIDADE 2
# # aula 9


# # Crie um sistema de notas alunos, com as seguintes operações:
# # Utilize While(loop é infinito) ou for(finito) 


# # - Acesso a conta com condicionais
# # - 3 chances de acessar o sistema
# # - Após errar 3 x mensagem que diga que a conta bloqueada 
# # - Inserir notas 
# # - Fazer a média


# # notas = {
# # 'Ana':0, 
# # 'Paulo':0, 
# # 'Jessica':0
# # }


# # cadastrados = {
# # 'fernando':'123',
# # 'Cardoso':'456',
# # 'julia':'789'
# # }




# # for i in range(1,4):
# #     login = input('Digite seu login: ')
# #     senha = input('Digite sua senha: ')
# #     if login in cadastrados.keys() and senha in cadastrados.values():
# #         print('Cadastre as notas dos alunos: ')
# #         notas1 = []
# #         nomes = []
# #         for chave,valores in notas.items():
# #             nomes.append(chave)
# #             notas1.append(valores)
# #             # print(nomes, notas1)    
# #             print('Digite as notas:', chave)              
# #             nota1 = float(input('Digite a nota1:'))
# #             nota2 = float(input('Digite a nota2:'))
# #             nota3 = float(input('Digite a nota3:'))
# #             notas[chave] = [nota1,nota2,nota3]
# #             media = sum(notas[chave])/len(notas[chave])
# #             print(media)
         
          


# #         else:
# #             break     
           


         
# #     else:
# #         print('Acesso negado')  
         
        





# # else:
# #     print('Conta bloqueada')



# # def display1(nome):
# #     print('Olá seja bem vindo', nome)


# # def carrinho(produtos):
# #     lista_prod = ['a','b','c']
# #     meu_carrinho = []
# #     valores = [10,20,30]
# #     meu_total = []
# #     print(produtos)
# #     p =  input('Deseja fazer o pedido? s/n')
# #     while p == 's':
# #         pedido = int(input('Digite seu produto:> '))
# #         meu_carrinho.append(lista_prod[pedido])
# #         print(meu_carrinho)
# #         meu_total.append(valores[pedido])
# #         soma_total = sum(meu_total) 
# #         # print('R$', soma_total)
# #         p =  input('Deseja fazer o pedido? s/n')
# #         print('Total do pedido  - R$',soma_total )    
# #     return meu_carrinho







# # import statistics


# # # soma(obj, obj)
# # def soma(a,b):
# #     return a + b


# # def sub(a,b):
# #     return a - b


# # def mult(a,b):
# #     return a * b


# # def div(a,b):
# #     return a / b



# # def mediana(lista):
# #     mediana1 = statistics.median(lista)
# #     print(mediana1)  









# # import funcoes


# # def mercado():
# #     nome = input('Digite seu nome: ')
# #     funcoes.display1(nome)
# #     produtos = ['a','b','c']
# #     m =  funcoes.carrinho(produtos)
# #     print(m)
# # mercado()




























# # Com parametro e return


# def calculo_hora(carga,salario):
#     return salario/carga


# def calculo_extra_50(hora):
#     return hora * 1.5


# def calculo_hora_noturna(hora):
#     return hora * 1.2    


# def cumprim(nome):
#     print('Olá', nome)     


# def sistema_de_horas():
#     nome = input('Nome: ')
#     cumprim(nome)
#     escolha = int(input('Valor/hora - 1 Extra 50% - 2 Adicional noturno 20% - 3'))
#     if escolha == 1:
#        carga = float(input('Carga de trabalho mês: '))
#        salario =  float(input('Digite o salario: ')) 
#        print('R$', round(calculo_hora(carga,salario),2))
#     elif escolha == 2:
#          carga = float(input('Carga de trabalho mês: '))
#          salario =  float(input('Digite o salario: ')) 
#          valor_hora  =  calculo_hora(carga,salario)
#          print('extra 50%:',round(calculo_extra_50(valor_hora),2))  
#     elif escolha == 3:
#          carga = float(input('Carga de trabalho mês: '))
#          salario =  float(input('Digite o salario: ')) 
#          valor_hora  =  calculo_hora(carga,salario)
#          print('adicional noturno extra 20%:',round(calculo_hora_noturna(valor_hora),2))   



#     else:
#         print('Digite algo valido')    



def soma():
    try:
        n1=input(">>")
        n2=int(input(">>"))
        soma=n1+n2
        print(soma)

    except TypeError:
        print("dado não pode ser somado")
    

    
