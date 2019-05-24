from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.createBook("Society of Mind", 12345678)
novel1 = Tome_Rater.createNovel("Alice In Wonderland", 12345, "Lewis Carroll")
novel1.setIsbn(9781536831139)
nonfiction1 = Tome_Rater.createNonFiction("Automate the Boring Stuff", 1929452, "Python", "beginner")
nonfiction2 = Tome_Rater.createNonFiction("Computing Machinery and Intelligence", 11111938, "AI", "advanced")
novel2 = Tome_Rater.createNovel("The Diamond Age", 10101010, "Neal Stephenson")
novel3 = Tome_Rater.createNovel("There Will Come Soft Rains", 10001000, "Ray Bradbury")

#Create users:
Tome_Rater.addUser("Alan Turing", "alan@turing.com")
Tome_Rater.addUser("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.addUser("Marvin Minsky", "marvin@mit.edu", _userBooks=[book1, novel1, nonfiction1])
print()

#Add books to a user one by one, with ratings:
Tome_Rater.addBookToUser(book1, "alan@turing.com", 1)
Tome_Rater.addBookToUser(novel1, "alan@turing.com", 3)
Tome_Rater.addBookToUser(nonfiction1, "alan@turing.com", 3)
Tome_Rater.addBookToUser(nonfiction2, "alan@turing.com", 4)
Tome_Rater.addBookToUser(novel3, "alan@turing.com", 1)

Tome_Rater.addBookToUser(novel2, "marvin@mit.edu", 2)
Tome_Rater.addBookToUser(novel3, "marvin@mit.edu", 2)
Tome_Rater.addBookToUser(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.printCatalog()
Tome_Rater.printUsers()

# print("Most positive user:")
# print(Tome_Rater.most_positive_user())
# print("Highest rated book:")
# print(Tome_Rater.highest_rated_book())
# print("Most read book:")
# print(Tome_Rater.most_read_book())

