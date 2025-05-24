import webbrowser

print("\n          Consulta de roupas")
print("\nMarcas disponiveis:Sufgang,Class,Mad,Takeoff\n")
inicio=1
marca=[]
tipo=[]
tamanho=[]

classtm={
    "p":"https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CP",
    "m":"https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CM",
    "g":"https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CG",
    "gg":"https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CGG",
    "egg":"https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CEGG"
}

suftm={
    "pp":"https://streetbusiness.com.br/marca/sufgang/?Tamanho=Pp",
    "p":"https://streetbusiness.com.br/marca/sufgang/?Tamanho=P",
    "m":"https://streetbusiness.com.br/marca/sufgang/?Tamanho=M",
    "g":"https://streetbusiness.com.br/marca/sufgang/?Tamanho=G",
    "gg":"https://streetbusiness.com.br/marca/sufgang/?Tamanho=Gg",
    "exg":"https://streetbusiness.com.br/marca/sufgang/?Tamanho=Exg",
    "exgg":"https://streetbusiness.com.br/marca/sufgang/?Tamanho=Exgg"


    
}


madtm={
     "pp":"https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=Pp",
    "p":"https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=P",
    "m":"https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=M",
    "g":"https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=G",
    "gg":"https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=Gg",
    "exg":"https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=Exg",
    "exgg":"https://streetbusiness.com.br/marca/mad-enlatados/?Tamanho=Exgg"
    

}

takeofftm={
   "p":" https://takeoffcollection.com.br/categorias/?Tamanho=P",
   "m":" https://takeoffcollection.com.br/categorias/?Tamanho=M",
   "g":" https://takeoffcollection.com.br/categorias/?Tamanho=G",
   "gg":" https://takeoffcollection.com.br/categorias/?Tamanho=Gg",
   "xg":" https://takeoffcollection.com.br/categorias/?Tamanho=Xg"



}

def takeoff():

    print("\n---TAKEOFF----")
    print("\n1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG\n5-Tamanho:XG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(takeofftm.get("p"))
              
        case "2":
            webbrowser.open(takeofftm.get("m"))
                 
        case "3":
            webbrowser.open(takeofftm.get("g"))
        
        case "4":
            webbrowser.open(takeofftm.get("gg"))
        
        case "5":
            webbrowser.open(takeofftm.get("xg"))


def mad():

    print("\n---MAD----")
    print("1-Tamanho:PP\n2-Tamanho:P\n3-Tamanho:M\n4-Tamanho:G\n5-Tamanho:GG\n6-Tamanho:EXG\n7-Tamanho:EXGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(madtm.get("pp"))
              
        case "2":
            webbrowser.open(madtm.get("p"))
                 
        case "3":
            webbrowser.open(madtm.get("m"))
        
        case "4":
            webbrowser.open(madtm.get("g"))
        
        case "5":
            webbrowser.open(madtm.get("gg"))

        case "6":
            webbrowser.open(madtm.get("exg"))

        case "7":
            webbrowser.open(madtm.get("exgg"))


def suf():

    print("\n---SUFGANG----")
    print("1-Tamanho:PP\n2-Tamanho:P\n3-Tamanho:M\n4-Tamanho:G\n5-Tamanho:GG\n6-Tamanho:EXG\n7-Tamanho:EXGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(suftm.get("pp"))
              
        case "2":
            webbrowser.open(suftm.get("p"))
                 
        case "3":
            webbrowser.open(suftm.get("m"))
        
        case "4":
            webbrowser.open(suftm.get("g"))
        
        case "5":
            webbrowser.open(suftm.get("gg"))

        case "6":
            webbrowser.open(suftm.get("exg"))

        case "7":
            webbrowser.open(suftm.get("exgg"))


def cls():

    print("\n---CLASS----")
    print("1-Tamanho:P\n2-Tamanho:M\n3-Tamanho:G\n4-Tamanho:GG\n5-Tamanho:EGG")
    c=input("Opção: ")

    match c:

        case "1":
            webbrowser.open(classtm.get("p"))
            
            
        case "2":
            webbrowser.open(classtm.get("m"))
                 

        case "3":
            webbrowser.open(classtm.get("g"))
        

        case "4":
            webbrowser.open(classtm.get("gg"))
        

        case "5":
            webbrowser.open(classtm.get("egg"))
  
print('''-----MARCAS-----
      1-SUFGANG
      2-TAKEOFF
      3-CLASS
      4-MAD ENLATADOS
      ''')
c=input("Opção: ").lower

match c:

    case ("1","sufgang"):
        suf()
    case ("2","takeoff"):
        takeoff()
    case ("3","class"):
        cls()
        
    case ("4","mad enlatados","mad"):
        mad()





       


























# def kit():
#     while inicio==1:
#         escolha=input("\nMarca: ")
#         escolha2=input("\nTipo de roupa: ")
#         escolha3=input("\nTamanho: ")
#         sair=input("Deseja sair?(s/n): ")
#         marca.append(escolha)
#         tipo.append(escolha2)
#         tamanho.append(escolha3)

#         if sair=="s":
#              



# p=c
# m="https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CM"
# g="https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CG"
# gg="https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CGG"
# egg="https://www.wallsgeneralstore.com.br/class?loja=690339&categoria=119&variants%5B%5D=Tamanho%7C%7CEGG"
# classtm=[p,g,gg,egg]


        
    
       

        
    

    














