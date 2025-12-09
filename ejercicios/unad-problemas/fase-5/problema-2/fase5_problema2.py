import os

os.system('cls')


class Library:

    def __init__(self) -> None:
        self.categories = []

    def add_category(self, category):
        """Añade una categoria a la biblioteca."""

        if isinstance(category, Category):
            if not category in self.categories:
                self.categories.append(category)
                return True
        return False

    def add_book_to_category(self, category_id, book):
        """
        Añade libros a la biblioteca"""

        if isinstance(book, Book):
            for category in self.categories:
                if category_id == category.category_id:
                    return category.add_book(book)
        return False

    def show_all_books(self):
        """Muestra todos los libros de la biblioteca."""

        for category in self.categories:
            print(f"\n{category.category_name}\n")

            if len(category.books) > 0:
                for book in category.books:
                    book.show_info()

            else:
                print('Vacio')


class Category:

    def __init__(self, category_id, category_name, category_price) -> None:
        self.category_id = category_id
        self.category_name = category_name
        self.category_price = float(category_price)
        self.books = []

    def add_book(self, book):
        """Añade un libro a la categoria."""

        if isinstance(book, Book):
            if not book in self.books:
                self.books.append(book)
                return True
        return False


class Book:

    def __init__(self, book_id, book_title, book_author, book_edition) -> None:
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.book_edition = book_edition

    def show_info(self):
        """Muestra en consola la info del libro."""

        print(
            f"ID LIBRO: {self.book_id}\n- Titulo: {self.book_title}\n- Autor: {self.book_author}\n- Edicion: {self.book_edition}")


# creando a la biblioteca:
mi_biblioteca = Library()

# Creando las categorias:
ciencia = Category('C1', 'Ciencia', 80000)
literatura = Category('C2', 'Literatura', 50000)
tecnologia = Category('C3', 'Tecnologia', 100000)
historia = Category('C4', 'Historia', 60000)

# Anadiendo las categorias a la biblioteca:
mi_biblioteca.add_category(ciencia)
mi_biblioteca.add_category(literatura)
mi_biblioteca.add_category(tecnologia)
mi_biblioteca.add_category(historia)

# Creando los libros:
libro_1 = Book('B1', 'Cien años de soledad', 'Gabriel G. Marquez', 1969)
libro_2 = Book('B2', 'Crimen y castigo', 'Fiodor Dostoviesky', 1869)
libro_3 = Book('B3', 'Las 48 leyes del poder', 'Robert Greene', 1998)

# Anadiendo libros a la biblioteca:
mi_biblioteca.add_book_to_category('C2', libro_1)
mi_biblioteca.add_book_to_category('C1', libro_3)

mi_biblioteca.show_all_books()
