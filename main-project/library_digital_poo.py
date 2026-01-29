from abc import ABC, abstractmethod
import json

library_shop = []
try:
    with open("books.json", "r", encoding="utf-8") as j:
        library_shop = json.load(j)
except FileNotFoundError:
    print("books.json No Encontrado")
except json.JSONDecodeError:
    print("books.json Invalido")

# Crea el Nuevo Libro y lo Agrega en la Libreria
class NewBook(ABC):
    def add_book(self, name_book, author_book, category_book, year_publish, value_book):
        self.name_book = name_book
        self.author_book = author_book
        self.category_book = category_book
        self.year_publish = year_publish
        self.value_book = value_book

        return {
            "Nombre del Libro": name_book,
            "Autor del Libro": author_book,
            "Categoria del Libro": category_book,
            "Año de Lanzamiento": year_publish,
            "Precio": value_book
        }

    @abstractmethod
    def saved_book(self):
        pass

# Se Guarda Libro en la Libreria
class BookSaved(NewBook):
    def saved_book(self, library, book_new):
        library.append(book_new)
        return library

# SRP implementado para Relacion de Clases y Sub-Clases
# Clase con enfoque en Busqueda de Libros
class Searcheable(ABC):
    @abstractmethod
    def search_book(self):
        pass

# Clase con enfoque en Mostrar Categorias
class Categoryzable(ABC):
    @abstractmethod
    def show_category(self):
        pass

# Clase con enfoque en Compra
class Purchable(ABC):
    @abstractmethod
    def payment_book(self):
        pass

# Busqueda de Libro por Nombre
class SearchedLibrary(Searcheable):
    def search_book(self, library, search_book, search_author):
        book_availability = False

        for book in library:

            if book["Nombre del Libro"] == search_book:
                book_availability = True
                print(f"Libro disponible {book_availability}")
                return book

            elif book["Autor del Libro"] == search_author:
                book_availability = True
                print(f"Libro disponible {book_availability}")
                return book

            else:
                print("Libro No Disponible")

# Mostrar Libros por Categoria, principales: Programacion, IA o Tecnologia
class CategoryLibrary(Categoryzable):
    def show_category(self, library, search_category):
        category_exists = False

        for book in library:

            if (book["Categoria del Libro"] == search_category):
                category_exists = True
                print(f"Nombre {book['Nombre del Libro']} | Autor {book['Autor del Libro']} | Categoria {book['Categoria del Libro']}")
                return category_exists

        else:
            print("No hay Libros en Esta Categoria")

# Compra Libro de la Libreria
class BuyLibrary(Purchable):
    def payment_book(self, library, name_book):
        books_shop = []

        for book in library:
            
            if book["Nombre del Libro"] == name_book:
                print(f"El Libro {book['Nombre del Libro']} tiene un valor de {book['Precio']}")

                payment = float(input("Confirmar Pago: "))

                if payment >= book["Precio"]:
                    print("Libro comprado")

                    books_shop.append(book)

                else:
                    print("El pago es Insuficiente")

        else:
            print(f"El Libro {book['Nombre del Libro']} No Se Encuenta")


while (True):
    # Opciones Interactivas
    print("BIENVENIDO A LA LIBRERIA DIGITAL TECHBOOK")
    print("1. Agregar Nuevo Libro en la Libreria")
    print("2. Buscar un Libro por Nombre o Autor")
    print("3. Mostrar Libros por Categoria")
    print("4. Comprar un Libro")
    print("5. Salir")

    option_menu = int(input())

    match option_menu:

        # Agrega Nuevo Libro en la Libreria
        case 1:
            created = BookSaved()

            book_name = input("¿Como se llama el Nuevo Libro que se va Agregar? ")
            author_name = input(f"¿Quien es el Autor del Libro {book_name}? ")
            book_category = input("Indique la Categoria del Libro (Programacion | Inteligencia  Artificial | Tecnologia) ")
            launch_year = int(input("Indique el Año de Lanzamiento del Libro "))
            book_price = float(input("¿Cual es el precio de este Libro? "))

            book_new = (book_name, author_name, book_category, launch_year, book_price)
            book = created.saved_book(library_shop, book_new)
            library_shop.append(book)
            print("Nuevo Libro a la Venta")

        # Busca Libro por el Nombre o Autor
        case 2:
            searched = SearchedLibrary()

            book_search = input("Indique el Nombre del Libro que busca ")
            author_search = input("¿Como se Llama el Autor del Libro? ")
            search = searched.search_book(library_shop, book_search, author_search)
            print(search)

        # Muestra Libros por Categoria
        case 3:
            categories = CategoryLibrary()

            category_searched = input("Indique la Categoria que busca (Programacion | Inteligencia  Artificial | Tecnologia) ")
            category = categories.show_category(library_shop, category_searched)

        # Comprar un Libro de la Libreria
        case 4:
            buying = BuyLibrary()

            book_named = input("¿Cual es el Libro que va a Comprar?")
            buy = buying.payment_book(library_shop, book_named)

        # Salir del programa
        case 5:
            with open("books.json", 'w', encoding='utf-8') as f:
                json.dump(library_shop, f, indent=4, ensure_ascii=False)
            print("Datos guardados. ¡Hasta luego!")
            break

        case _:
            print("Opción no válida, intente de nuevo")