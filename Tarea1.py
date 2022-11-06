import csv
listaLibros =[]

class Libro:
    def __init__(self, id, titulo, genero, ISBN, editorial, autores) -> None:
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autores = autores
    def entregarDatos(self):
        print(f'Título: {self.titulo} - Género: {self.genero} - ISBN: {self.ISBN} - Editorial: {self.editorial} - Autores: {self.autores}')
    def eliminarDatos(self):
        for x in listaLibros:
            listaLibros.remove(x)
    def __repr__(self):
        return f'\nTítulo: {self.titulo} - Género: {self.genero} - ISBN: {self.ISBN} - Editorial: {self.editorial} - Autores: {self.autores}'
    def editarLibros(self, titulo, genero, ISBN, editorial, autores):
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autores = autores
        print('Los datos se actualizaron exitosamente')

#OPCIÓN 1

def leer_archivo():
    print('\nLeer archivo de disco duro\n')
    with open ('libros.csv') as f:
        lines = f.readlines()[1:4]
        print(lines)
        #reader = csv.reader(f, delimiter=',')
        #for row in reader:
        #    print('Título: {0} | Género: {1} | ISBN: {2} | Editorial: {3} | Autores: {4}'.format(row[0], row[1], row[2], row[3], row[4]))
    
#OPCIÓN 3

def agregar_libro():
    print('\nRegistro de libros\n')
    titulo = input('Ingrese el título del libro: ')
    genero = input('Ingrese el género del libro: ')
    ISBN = int(input('Ingrese el ISBN del libro: '))
    editorial = input('Ingrese la editorial del libro: ')
    autores = input('Ingrese el autor o autores del libro: ')
    objLibro = Libro(id,titulo, genero, ISBN, editorial, autores)
    listaLibros.append(objLibro)
    print('\n¡El libro ha sido agregado con éxito!')

#OPCIÓN 2

def listar_libro():
    print('\nListado de libros\n')
    for objLibro in listaLibros:
        objLibro.entregarDatos()

#OPCIÓN 4

def eliminar_libro():
    print('\nEliminar libro\n')
    eliminado = input('Ingrese el título del libro a eliminar: ')
    for eliminado in listaLibros:
        eliminado.eliminarDatos()
    print('El libro ha sido eliminado')

#OPCIÓN 5

def buscar_por_ISBN_titulo():
    print('\nBuscar por ISBN o por título\n')
    ISBNOT = int(input('Ingrese: \n1 -> ISBN  \n2 -> título: '))
    for objLibro in listaLibros:  
        if ISBNOT == 1:
            dato1 = int(input('Ingrese el ISBN: '))
            if dato1 == objLibro.ISBN:
                objLibro.entregarDatos()
        elif ISBNOT == 2:
            dato2 = input('Ingrese el título del libro: ')
            if dato2.lower() == objLibro.titulo:
                objLibro.entregarDatos()

#OPCIÓN 6

def ordenar_libros():
    print('\nLibros ordenados por título\n')
    listaLibros.sort(key=lambda x:x.titulo)
    print(repr(listaLibros)) 
        
#OPCIÓN 7

def buscar_por_autor_editorial_genero():
    print('\nBuscar por autor, editorial o género\n')
    AEG = int(input('Ingrese: \n1 -> autor \n2 -> editorial \n3 -> género: '))
    for objLibro in listaLibros:
        if AEG == 1:
            dato3 = input('Ingrese el autor del libro: ')
            if dato3.lower() == objLibro.autores:
                objLibro.entregarDatos()
        if AEG == 2:
            dato4 = input('Ingrese la editorial del libro:')
            if dato4.lower() == objLibro.editorial:
                objLibro.entregarDatos()
        if AEG == 3:
            dato5 = input('Ingrese el género del libro: ')
            if dato5.lower() == objLibro.genero:
                objLibro.entregarDatos()

#OPCIÓN 8 NO FUNCIONA

def buscar_num_autores():
    print('\nBuscar por número de autores\n')
    NUM = int(input('Ingrese: \n1 -> 1 autor \n2 -> 2 autores o más: '))
    for objLibro in listaLibros:
        if NUM == 1:
            dato6 = len(objLibro.autores)
            if dato6 == 1:
                objLibro.entregarDatos()
        if NUM == 2:
            dato7 = len(objLibro.autores)
            if dato7 >= 2:
                objLibro.entregarDatos()

#OPCIÓN 9

def modificarDatos():
    print("\nEditar o actualizar datos\n")
    CAMBIAR = input("Ingrese el título del libro a cambiar: ")
    for objLibro in listaLibros:
        if CAMBIAR == objLibro.titulo:
            titulo = input("Ingrese el nuevo título: ")
            genero = input("Ingrese el nuevo género: ")
            ISBN = int(input("Ingrese el nuevo ISBN: "))
            editorial = input('Ingrese la nueva editorial: ')
            autores = input('Ingrese el nuevo o los nuevos autores: ')
            objLibro.editarLibros(titulo, genero, ISBN, editorial, autores)
            objLibro.entregarDatos()

#OPCIÓN 10 NO FUNCIONA

def guardarLibros():
    with open ('libros,csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows()
    print('¡Guardado con éxito!')

while True:
    print('\n')
    print('|**|         Bienvenidos al Menú         |**|')
    print('\n')
    print('Opción 1: Leer archivo de disco duro')
    print('Opción 2: Listar libros')
    print('Opción 3: Agregar libro')
    print('Opción 4: Eliminar libro')
    print('Opción 5: Buscar libro por ISBN o por título')
    print('Opción 6: Ordenar libros por título')
    print('Opción 7: Buscar libros por autor, editorial o género')
    print('Opción 8: Buscar libros por número de autores')
    print('Opción 9: Editar o actualizar datos de un libro')
    print('Opción 10: Guardar libros en archivo de disco duro')
    print('Opcion 11: Salir\n')

# Estructura de opciones

    opcion = int(input('Inserte el número de la opción: '))
    if opcion == 1:
        leer_archivo()
    elif opcion == 2:
        listar_libro()
    elif opcion == 3:
        agregar_libro()
    elif opcion == 4:
        eliminar_libro()
    elif opcion == 5:
        buscar_por_ISBN_titulo()
    elif opcion == 6:
        ordenar_libros()
    elif opcion == 7:
        buscar_por_autor_editorial_genero()
    elif opcion == 8:
        buscar_num_autores()
    elif opcion == 9:
        modificarDatos()
    elif opcion == 10:
        guardarLibros()
    elif opcion == 11:
        break
    else:
        opcion = int(input('Opción equivocada, por favor escriba una opción del 1 al 11: '))