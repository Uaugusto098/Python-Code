# variveis globais



carga = float(input('digite hora/mês '))
salario =  float(input('Salario'))
calculo_hora = salario/carga
extra = calculo_hora * 1.5
quant_hora_extra = float(input('Quantidade hora extra: '))
Adcional_notuno_quant = int(input('Horas noturnas'))
hex_n = calculo_hora * 1.2




  


def valorhora():
    print('Horas R$:', round(calculo_hora,2))
    print('Hora extra 50% R$ ', round(extra,2))
    print('Quantidade realizada hora extra:',round(quant_hora_extra,2) )
    print('Hora extra noturna R$',round( hex_n,2))


# RETURN X PRINT



def sistema_de_horas():
    print('Seja bem vindo ao sistema de horas')
    # opcoes = ['','Horas'  ]
    escolha = input('Deseja fazer o calculo de horas? s/n')
    if escolha == 's':
        valorhora() 
    else:
        print('Saindo do sistema...')    



sistema_de_horas()



# def cumprimentar():
#     print('Seja bem vindo ao sistema de horas')


# def valorhora():
#     carga = float(input('digite hora/mês '))
#     salario =  float(input('Salario'))


#     calculo_hora = salario/carga
#     extra = calculo_hora * 1.5
#     quant_hora_extra = float(input('Quantidade hora extra: '))
#     Adcional_notuno_quant = int(input('Horas noturnas'))
#     hex_n = calculo_hora * 1.2



#     print('Horas R$:', round(calculo_hora,2))
#     print('Hora extra 50% R$ ', round(extra,2))
#     print('Quantidade realizada hora extra:',round(quant_hora_extra,2) )
#     print('Hora extra noturna R$',round( hex_n,2))


# # RETURN X PRINT



# def sistema_de_horas():
#     cumprimentar()
#     # opcoes = ['','Horas'  ]
#     escolha = input('Deseja fazer o calculo de horas? s/n')
#     if escolha == 's':
#         valorhora() 
#     else:
#         print('Saindo do sistema...')    



# sistema_de_horas()


# ## ATIVIDADE 2
# aula 9


# Crie um sistema de notas alunos, com as seguintes operações:
# Utilize While(loop é infinito) ou for(finito) 


# - Acesso a conta com condicionais
# - 3 chances de acessar o sistema
# - Após errar 3 x mensagem que diga que a conta bloqueada 
# - Inserir notas 
# - Fazer a média


# notas = {
# 'Ana':0, 
# 'Paulo':0, 
# 'Jessica':0
# }


# cadastrados = {
# 'fernando':'123',
# 'Cardoso':'456',
# 'julia':'789'
# }




# for i in range(1,4):
#     login = input('Digite seu login: ')
#     senha = input('Digite sua senha: ')
#     if login in cadastrados.keys() and senha in cadastrados.values():
#         print('Cadastre as notas dos alunos: ')
#         notas1 = []
#         nomes = []
#         for chave,valores in notas.items():
#             nomes.append(chave)
#             notas1.append(valores)
#             # print(nomes, notas1)    
#             print('Digite as notas:', chave)              
#             nota1 = float(input('Digite a nota1:'))
#             nota2 = float(input('Digite a nota2:'))
#             nota3 = float(input('Digite a nota3:'))
#             notas[chave] = [nota1,nota2,nota3]
#             media = sum(notas[chave])/len(notas[chave])
#             print(media)
         
          


#         else:
#             break     
           


         
#     else:
#         print('Acesso negado')  
         
        





# else:
#     print('Conta bloqueada')




