import pygame 


pygame.init()# iniciando
tela  =  pygame.display.set_mode((500,500))
pygame.display.set_caption('Título')

run = True

while run == True:
     for evento in pygame.event.get():
          if evento.type  ==   pygame.QUIT:
               run = False
               quit()

          tela.fill('Chocolate') 
          pygame.draw.rect(tela,(0,255,255),(100,250,50,50)) 
          pygame.draw.polygon(tela,(0,255,0),[(120,120),(150,120),(140,130)], width=50) 
          pygame.draw.ellipse(tela,('red'),(100,450,50,50)) 
          pygame.draw.circle(tela,(0,0,0),(350,350),(80)) 


          # cicle


          # poligono
          # ellipse 

          pygame.display.flip()

              


               
          




              


               
          



