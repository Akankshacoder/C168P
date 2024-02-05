class BookShelf:
    
    def __init__(self, name, author, price, publishing_year):
         self.name = name
         self.author = author
         self.price = price
         self.publishing_year = publishing_year
         
    def addbook(self):
         print("The Book Details are: ")
         print("Book Name : " + self.name)
         print("Book Author : " + self.author)
         print("Book Price : " + str(self.price))
         print("Publishing_Year " + self.publishing_year)
      
        
Book1 = BookShelf("The Candy makers", "Wendy Mass", 768, "5 October 2010")    
Book1.addbook()      