# Create a class Product with properties name, price, and quantity. 
# Create a child class Book that inherits from Product and adds a property 
# author and a method called read that prints information about the book.


class Product:
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__ (self, name, price, quantity, author):
        super().__init__(name,price,quantity)
        self.author = author

    def read(self):
        print (f'Book - {self.name}\nPrice - {self.price}\nQuantity - {self.quantity}\nAuthor - {self.author} ')
    
book = Book("The Great Gatsby", 15.99, 50, "F. Scott Fitzgerald")
book.read()