print(" Calculadora em Python")


print("\n")



c=(input("Digite qual operação realizar: "))
a=float(input("\nDigite o primeiro numero: "))
b=float(input("\nDigite o segundo numero: "))


if c=="+":
    
    d=a+b
    
    print ("\nO resultado da soma é de: ",d)
    
elif c=="-":
    
    d=a-b
    
    print ("\nO resultado da subtração é de: ",d)
    
elif c=="*":
    
    d=a*b
    
    print ("\nO resultado da multiplicação é de: ",d)
    
    
elif c=="/":
    
   d=a/b
    
    
    
   print ("\nO resultado da divisão é de: ",d)
   
   
else:
    print("\nDigite uma operação existente")
    
