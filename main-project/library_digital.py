import json

try:
    with open("book.json", "r") as j:
        library_shop = json.load(j)
        print(library_shop["Libros Disponibles"])
except FileNotFoundError:
    print("El Archivo no Existe")

library_shop = []

# Funcion 1: Agrega un Nuevo Libro
def create_book(name_book, author_book, category_book, year_publish, value_price):
    return {
        "Nombre del Libro": name_book,
        "Autor del Libro": author_book,
        "Categoria del Libro": category_book,
        "Año de Lanzamiento": year_publish,
        "Precio": value_price
    }

def saved_book(library, book_new):
    library.append(book_new)
    return library

# Funcion 2: Busca un Libro en la Libreria por Nombre
def search_book(library, search_book):

    book_availability = False

    for book in library:

        if book["Nombre del Libro"] == search_book:
            book_availability = True
            return book_availability, book
        else:
            print("Libro No Disponible")

# Funcion 3: Muestra Libros por Categoria
def show_category(library, search_category):

    category_exists = False

    for book in library:

        if book["Categoria del Libro"] == search_category:
            category_exists = True
            print(f"Nombre {book["Nombre del Libro"]} | Autor {book["Autor del Libro"]} | Cateogira {book["Categoria del Libro"]}")
            return category_exists

    else:
        print("No hay Libros en Esta Categoria")

# Funcion 4: Compra un Libro
def payment_book(library, name_book):
    books_shops = []

    for book in library:

        if book["Nombre del Libro"] == name_book:
            print(f"El Libro {book['Nombre del Libro']} tiene un valor de {book['Precio']}")

            payment = float(input("Confirmar Pago: "))

            if payment >= book["Precio"]:
                print("Libro comprado")

                books_shops.append(book)
            else:
                print("El pago es Insuficiente")
        
        else:
            print(f"El Libro {book['Nombre del Libro']} No se Encuentra")

books = library_shop

# Menu de Opciones Interactivo
while (True):
    print("BIENVENIDO A LA LIBRERIA DIGITAL TECHBOOK")
    print("1. Agregar Nuevo Libro en Libreria")
    print("2. Buscar un Libro por Nombre o Autor")
    print("3. Mostrar Libros por Categoria")
    print("4. Comprar Libro")

    option_menu = int(input())

    match option_menu:

        # Al seleccionar la Opcion 1 Agregamos un Nuevo Libro en la Libreria
        case 1:
            book_name = input("¿Como se llama el Nuevo Libro que se va Agregar? ")
            author_name = input(f"¿Quien es el Autor del Libro {book_name}? ")
            book_category = input("Indique la Categoria del Libro (Programacion | Inteligencia Artificial | Tecnologia) ")
            launch_year = int(input("Indique el Año de Lanzamiento del Libro "))
            book_price = float(input("¿Cual es el precio de este Libro? "))

            book = create_book(book_name, author_name, book_category, launch_year, book_price)
            library_shop.append(book)
            print("Nuevo Libro a la Venta")

        # Al seleccionar la Opcion 2 se busca un Libro por el Nombre o Autor
        case 2:
            book_search = input("Indique el Nombre del Libro que busca ")
            search = search_book(library_shop, book_search)
            print(search)

        # Al seleccionar la Opcion 3 se muestran Libros de una Categoria
        case 3:
            category_search = input("Indique la Categoria de los Libros que quiere ver (Programacion | Inteligencia Artificial | Tecnologia)")
            category = show_category(library_shop, category_search)
            print(category)

        # Al seleccionar la Opcion 4 el usuario Compra un Libro
        case 4:
            book_name = input("¿Cual es el Libro que va a Comprar? ")
            buys = payment_book(library_shop, book_name)

        case _:
            with open("books.json", 'w', encoding='utf-8') as f:
                json.dump(library_shop, f, indent=4, ensure_ascii=False)