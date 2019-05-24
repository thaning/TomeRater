class User(object):
    def __init__(self, _name, _email):
        self.name = _name
        self.email = _email
        self.books = {}

    def __repr__(self):
        return 'User: {n}, Email: {e}, have read {no} books'.format(n=self.name, e=self.email, no=len(self.books))

    def __eq__(self, _other):
        if self.name == _other.name and self.email == _other.email:
            return True
        else:
            return False

    #def __hash__(self):
    #    return hash((self.name, self.email))
    
    def getEmail(self):
        return self.email

    def changeEmail(self, _address):
        self.email = _address
        print('The user {n} have been updated with a new email: {e}'.format(n=self.name, e=self.email))

    def readBook(self, _book, _rating=None):
        self.books.update({_book:_rating})

    def getAvgRating(self):
        total = 0        
        for value in self.books.values():
            total += value
        return total / len(self.books)
    

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
    
    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return '{t}'.format(t=self.title) 

    def getTitle(self):
        return self.title

    def getIsbn(self):
        return self.isbn

    def setIsbn(self, _isbn):
        self.isbn = _isbn        
        print('The book {t} have been updated with a new ISBN: {i}'.format(t=self.title, i=self.isbn))

    def addRating(self, _rating):
        if _rating >= 0 and _rating <= 4:
            self.ratings.append(_rating)
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


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def createBook(self, _title, _isbn):
        return Book(_title, _isbn)

    def createNovel(self, _title, _isbn, _author):
        return Fiction(_title, _isbn, _author)

    def createNonFiction(self, _title, _isbn, _subject, _level):
        return NonFiction(_title, _isbn, _subject, _level)

    def addBookToUser(self, _book, _email, _rating=None):
        if _email not in self.users.keys():
            print('No user with email {e}!'.format(e=_email))
        else:
            user = self.users.get(_email)
            
            # call readBook
            user.readBook(_book, _rating)

            # call addRating
            if _rating is not None:
                _book.addRating(_rating)
            if _book not in self.books.keys():
                self.books[_book] = 1
            else:
                self.books[_book] += 1                
       
    def addUser(self, _name, _email, _userBooks=None):
        newUser = User(_name, _email)
        if _email not in self.users.keys():
            self.users.update({_email: newUser})
            print('User {u} created'.format(u=_name))
            if bool(_userBooks):
                for each in _userBooks:
                    self.addBookToUser(each, _email)

    def printCatalog(self):
        print("Printing Catalog:")
        for each in self.books.keys():
            print(each)
        print()

    def printUsers(self):
        print("Printing users:")
        for user in self.users.values():
            print(user)
        print()

#test book functions
#test = Book('test bog', 123)
#test2 = Book('test bog', 123)
#test3 = Book('Biblen', 12313)

#print(test==test2)
#test.setIsbn(456)
#print(test==test2)


##test users funcs
#stefan = User('Stefan Thaning', 'stefan@thaning.org')
#print(stefan)
#stefan.readBook(test, 2)
#stefan.readBook(test3, 0)
#print(stefan)
#print(stefan.getAvgRating())

##test TomeRater
#testTome = TomeRater()
#testTome.addUser('Stefan', 'stefan@thaning.org')
#testTome.addUser('Stefan2', 'stefan@gmail.com')

#for each in testTome.users:
#    print(each)
    
#for key, value in testTome.users.items():
#    print(testTome.users[key])

#testTome.addBookToUser(Book('test bogen', 12), 'stefan@thaning.org', 122)