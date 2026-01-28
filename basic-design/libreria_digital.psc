Algoritmo LibreriaDigitalTech
	Definir book_name, author_name, book_category, book_search, category_search Como Texto
	Definir launch_year, menu_option, library, book_purchased, i Como Entero
	Definir book_price, buy_book Como Real
	Definir have_subcategory, book_availability, category_exists Como Logico
	
	i = 1
	library = 1
	
	Dimension book_name[5], author_name[5], book_category[5], launch_year[5], book_price[5]
	
	// Menu de Opciones para funcionalidades de la Libreria
	Repetir
		Escribir "BIENVENIDO A LA LIBRERIA TECHBOOK"
		Escribir "1. Agregar Nuevo Libro en Libreria"
		Escribir "2. Buscar un Libro por Nombre o Autor"
		Escribir "3. Mostrar Libros por Categoria"
		Escribir "4. Comprar Libro"
		
		Leer menu_option
		
		Segun menu_option Hacer
			
			// Opcion N°1: Agrega un Nuevo Libro en la Libreria (Inicialmente se ve en la parte Backend)
			Caso 1:
				
				Escribir "¿Como se llama el Nuevo Libro que se va agregar? "; Leer book_name[library]
				Escribir "¿Quien es el autor del Libro ", book_name[library],"? "; Leer author_name[library]
				Escribir "Indique la Categoria del Libro (Programacion | Inteligencia Artificial | Tecnologia) "; Leer book_category[library]
				Escribir "Indique el Año de Lanzamiento del Libro "; Leer launch_year[library]
				Escribir "¿Cual es el Precio de este Libro? "; Leer book_price[library]
				
				library = library + 1
				Escribir "Nuevo Libro a la Venta"
				
			// Opcion N°2: Busca un Libro en la Libreria por el Nombre
			Caso 2:
				
				Escribir "Indique el Nombre del Libro que busca "; Leer book_search
				
				book_availability = Falso
				
				Para i = 1 Hasta library Con Paso 1 Hacer
					
					Si book_search = book_name[i] Entonces
						book_availability = Verdadero
						Escribir "Libro ", book_name[i], " Disponible"
					FinSi
					
				FinPara
				
				Si book_availability = Falso Entonces
					Escribir "Libro No Disponible"
				FinSi
				
			// Opcion N°3: Muestra Libros disponibles por Categoria (Lenguaje, Tecnologia, IA)
			Caso 3:
				
				Escribir "Indique la Categoria de Libros que quiere ver "; Leer category_search
				
				category_exists = Falso
				
				Para i = 1 Hasta library Con Paso 1 Hacer
					
					Si category_search = book_category[i] Entonces
						category_exists = Verdadero
						Escribir "Categoria ", book_category[i], " Existe"
						Escribir "Nombre ", book_name[i], " | Autor ", author_name[i], " | Categoria ", book_category[i]
					FinSi
					
				FinPara
				
				Si category_exists = Falso Entonces
					Escribir "Categoria No Existe"
				FinSi	
				
			// Opcion N°4: Compra un Libro de la Libreria
			Caso 4:
				Escribir "¿Cual es el Libro que va a Comprar? "; Leer book_search
				
				Para i = 1 Hasta library Con Paso 1 Hacer
					
					Si book_search = book_name[i] Entonces
						Escribir "El precio del Libro ", book_name[i], " es ", book_price[i]
						
						Leer buy_book
						
						Si buy_book >= book_price[i]
							Escribir "Libro comprado"
							library = library - 1
							books_purchased = books_purchased + 1
							Escribir books_purchased
						SiNo
							Escribir "Pago Insuficiente"
						FinSi
					FinSi
					
				FinPara
				
			De Otro Modo:
				Escribir " "
		FinSegun
	Hasta Que (menu_option == 5)
FinAlgoritmo