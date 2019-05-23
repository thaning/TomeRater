class User(object):
    def __init__(self, _name, _email):
        pass

    def get_email(self):
        pass

    def change_email(self, _address):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other_user):
        pass




class Book:
    def __init__(self, _title, _isbn):
        self.title = _title
        self.isbn = _isbn
        self.ratings = []

    def getTitle(self):
        return self.title

    def getIsbn(self):
        return self.isbn

    def setIsbn(self, _isbn):
        self.isbn = _isbn        
        print('The book {t} have a new ISBN: {i}'.format(t=self.title, i=self.isbn))





print('hej')
test = Book('test bog', 123)
test.setIsbn(456)