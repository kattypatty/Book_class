class Book:
  def __init__(self, publisher, author, genre):
    self.publisher = publisher
    self.__author = author
    self.genre = genre

  def get_publisher(self):
    return self.publisher
  
  def get_author(self):
    return self.__author
  
  def get_genre(self):
    return self.genre
  
  def set_publisher(self, new_publisher):
    self.publisher = new_publisher
    print(self.publisher)

  def set_author(self, new_author):
    self.__author = new_author
    print(self.__author)

  def set_genre(self, new_genre):
    self.genre = new_genre
    print(self.genre)

  def print_book(self):
    return f"{self.publisher} {self.__author} {self.genre}"
  
class Fiction(Book):
  def __init__(self, publisher, author, genre, subgenre, num_pages):
    super().__init__(publisher, author, genre)
    self.subgenre = subgenre
    self.num_pages = num_pages

  def print_fiction_book(self):
    return f"{self.publisher} {self.get_author()} {self.subgenre}"

  def get_subgenre(self):
    return self.subgenre
  
  def get_num_pages(self):
    return self.num_pages
  
  def set_num_pages(self, new_num_pages):
    self.num_pages = new_num_pages
    print(self.num_pages)

class Fantasy(Fiction):
  def __init__(self, publisher, author, genre, subgenre, num_pages, publication_year):
    super().__init__(publisher, author, genre, subgenre, num_pages)
    self.publication_year = publication_year

  def print_fantasy_book(self):
    return f"{self.subgenre} {self.publication_year}"
  
  def get_fantasy_subgenre(self):
    return self.subgenre
  
  def get_publication_year(self):
    return self.publication_year
  
  def set_publication_year(self, new_publication_year):
    self.publication_year = new_publication_year
    print(self.publication_year)

# class Book
book1 = Book("Wiley", "Stephen King", "Horror")
print(book1.print_book())
print(book1.genre)
print(book1.get_author())
book1.get_publisher = "Scholastic"
book1.set_author = "J.K.Rowling"
book1.set_genre = "Thriller"
print(book1.print_book())
print(book1.__dict__)

# class Fiction
fictionBook = Fiction("Macmillan", "Franz Kafka", "Fiction", "Mystery", 287)
print(fictionBook.print_fiction_book())
print(fictionBook.get_author())
print(fictionBook.get_subgenre())
print(fictionBook.get_num_pages())
print(fictionBook.set_num_pages(344))
print(fictionBook.__dict__)

# class Fantasy
fantasyBook = Fantasy("Coffee House Press", "Umberto Eco", "Fantasy", "Urban Fantasy", 342, 1988)
print(fantasyBook.print_fantasy_book())
print(fantasyBook.get_fantasy_subgenre())
print(fantasyBook.set_publication_year(1994))
fantasyBook.get_fantasy_subgenre = "Low Fantasy"
print(fantasyBook.__dict__)





