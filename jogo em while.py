import random


c=3


while c>0:
    
    
    al=random.randint(1,10)
    ch= int(input("Digite seu chute:"))
   
   
    if ch==al:
    
        print("Parabens vc é incrivel,acertou em cheio",al)
        break
    else:
        c=c-1
        print("errou feio...tente novamente")
        print("Voce tem apenas",c,"chances")
    
else:
     print("Chances esgotadas")
    
    


    
    
    
    
    