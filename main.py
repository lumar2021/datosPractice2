
class Node:
   def __init__(self, data, numero):
      self.left = None
      self.right = None
      self.data = data
      self.numero = numero

   def insert(self, data, numero):
       if self.data:
           if data < self.data:
               if self.left is None:
                   self.left = Node(data , numero)
               else:
                   self.left.insert(data , numero)
           elif data > self.data:
               if self.right is None:
                   self.right = Node(data , numero)
               else:
                   self.right.insert(data , numero)
       else:
           self.data = data
           self.numero = numero


# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      if self.data != "":
        print('\033[4;1m'+self.data+'\033[0m'),
        print("✓ "+str(self.numero)),
      if self.right:
         self.right.PrintTree()




archivoEstudiantes = open("C:\\Users\\luisa\\OneDrive\\Documentos\\Txt\\Datos.txt")
contenidoPorLineas = archivoEstudiantes.readlines()


root = Node("",0)
subtemas = []
i = 0
txt=""
while (i < len(contenidoPorLineas)):
    lineaEstudiante = contenidoPorLineas[i].strip()

    numero=[]
    texto=""
    numeroTemporal = []
    textosSub = []
    textoTemporal = ""

    for j in lineaEstudiante:
        if (lineaEstudiante[0] == "m"):
            if(j.isdigit()==True):
                numero.append(j)
            else:
                 texto+=j
                 txt=texto
        elif (lineaEstudiante[0]== "s"):

            if(j.isdigit() == True):
                numeroTemporal.append(j)
            else:
                    textoTemporal += j

    numeroTemporal.sort()



    textosSub = [ txt , textoTemporal+str(numeroTemporal)]
    subtemas.append(textosSub)






    numero.sort()
    root.insert(texto, numero)





    i+=1

print("\n" + "\033[;36m" + "Listado de los términos generales del libro con sus paginas" + "\033[0m"+  "\n")
root.PrintTree()
subtemas.sort()

print("\n" + "\033[;36m" + "Listado de los subtérminos con sus páginas" + "\033[0;m"+  "\n")

k=0
temptext=[]
while k < len(subtemas):
    if(subtemas[k][1] != '[]'):
        print("\033[1m|Tema: "+subtemas[k][0]+'\033[0m' )
        print("\t \033[4m* Subtema con sus páginas ordenadas:\033[0m "+ subtemas[k][1])

    k += 1