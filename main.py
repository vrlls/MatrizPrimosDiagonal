#Existen 6 tipos de simbolos representados por un valor numerico: 
#1: -
#2: (
#3: ?
#4: $
#5: !
#0: .
#Una persona estara incertando numeros hasta que digite 3 veces seguidas el valor 0. Al final en una lista deben estar guardados los simbolos en orden de aparicion en las posiciones de la lista
#Ejemplo input
#1
#1
#2
#4
#0
#5
#5
#0
#0
#0
#output lista=["-","-","(","$",".","!","!","."]

def traductor():
  lista=[]
  cont=0
  while True:
    if cont>2:
      break
    else:
      num = int(input())
      if (num == 0):
        if(cont<1):
          lista.append(".")
        cont=cont+1
        print(cont)
      elif(num == 1):
        cont = 0
        lista.append("-")
      elif(num == 2):
        cont = 0
        lista.append("(")
      elif(num == 3):
        cont = 0
        lista.append("?")
      elif(num == 4):
        cont = 0
        lista.append("$")
      elif(num == 5):
        cont = 0
        lista.append("!")
      else:
        return "valor no valido"
  return lista
traductor()
