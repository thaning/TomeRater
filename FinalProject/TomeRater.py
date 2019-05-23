class User(object):
    def __init__(self, _name, _email):
        self.name = _name
        self.email = _email
        self.books = {}

    def getEmail(self):
        return self.email

    def changeEmail(self, _address):
        self.email = _address
        print('The user {n} have been updated with a new email: {e}'.format(n=self.name, e=self.email))

    def __repr__(self):
        return 'User: {n}, Email: {e}, have read {no} books'.format(u=self.name, e=self.email, no=len(self.books))

    def __eq__(self, _other):
        if self.name == _other.name and self.email == _other.email:
            return True
        else:
            return False

class Book:
    def __init__(self, _title, _isbn):
        self.title = _title
        self.isbn = _isbn
        self.ratings = []

    def __eq__(self, _other):
        if self.title == _other.title and self.isbn == _other.isbn:
            return True
        else:
            return False

    def getTitle(self):
        return self.title

    def getIsbn(self):
        return self.isbn

    def setIsbn(self, _isbn):
        self.isbn = _isbn        
        print('The book {t} have been updated with a new ISBN: {i}'.format(t=self.title, i=self.isbn))

    def add_rating(self, _rating):
        if _rating >= 0 and _rating <= 4:
            self.ratings += _rating
        else:
            print("Invalid Rating")
        
    
class Fiction(Book):
    def __init__(self, _title, _isbn, _author):
        super().__init__(_title, _isbn)
        self.author = _author

    def __repr__(self):
        return '{t} by {a}'.format(t=self.title, a=self.author)    

    def getAuthor(self):
        return self.author

class NonFiction(Book):
    def __init__(self, _title, _isbn, _subject, _level)    :
        super().__init__(_title, _isbn)
        self.subject = _subject
        self.level = _level
    
    def __repr__(self):
        return '{t}, a {l} manual on {s}'.format(t=self.title, l=self.level, s=self.subject)
    
    def getSubject(self):
        return self.subject

    def getLevel(self):
        return self.level


print('hej')
test = Book('test bog', 123)



test2 = Book('test bog', 123)
print(test==test2)

test.setIsbn(456)
print(test==test2)