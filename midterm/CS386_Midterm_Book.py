class Book:
    def __init__(self, title, pages, year):
        self.title = title
        self.pages = pages
        self.year = year # 3


    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def get_pages(self):
        return self.pages

    def set_pages(self, new_pages):
        # 4
        if new_pages >= 0:
            self.pages = new_pages


    # 3
    def get_year(self):
        return self.year

    def set_year(self, new_year):
        self.year = new_year

    # 3
    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}, Year {self.year}"
    
# -- main --
bible = Book( "RSV Holy Bible", 990, 1991)
pi = Book( "Raspberry Pi for Dummies", 516, 2023)

print( bible )
print( pi )
print()

pi.set_pages( -99 )
print( pi )
pi.set_pages( 623 )
print( pi )
print()

pi.set_title("Pi for Dummies")
pi.set_year( 2024 )
print( pi )
print()

print( pi.get_title() )
print( pi.get_pages() )
print( pi.get_year() )
print()














