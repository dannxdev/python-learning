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

    def __init__(self, book_id, book_title, book_author, book_edition, book_category) -> None:
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.book_edition = book_edition
        self.book_category = book_category

    def show_info(self):
        """Muestra en consola la info del libro."""

        print(
            f"ID LIBRO: {self.book_id}\n- Titulo: {self.book_title}\n- Autor: {self.book_author}\n- Edicion: {self.book_edition}\n- ID Categoria: {self.book_category}")


# Creando las categorias:
ciencia = Category('C1', 'Ciencia', 80000)
literatura = Category('C2', 'Literatura', 50000)
tecnologia = Category('C3', 'Tecnologia', 100000)
historia = Category('C4', 'Historia', 60000)

# Anadiendo los libros a las categorias:


# print(literatura.add_book())
# print(literatura.books)
