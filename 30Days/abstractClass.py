#Write MyBook class
class MyBook(Book):
    def __init__(self,t,a,p):
        self.price = p
        super(MyBook, self).__init__(t,a)
    
    def display(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Price: {}".format(self.price))