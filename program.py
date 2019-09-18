import pymongo

import db_operations


conn_str = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn_str)

db = client.bookstore_example

# insert books (python dictionary)
if db.books.count() == 0:
    print("Inserting books...")
    db.books.insert_one({'title': 'Book 1', 'isbn': '0000000000001'})
    db.books.insert_one({'title': 'Book 2', 'isbn': '0000000000002'})
    db.books.insert_one({'title': 'Book 3', 'isbn': '0000000000003'})
    db.books.insert_one({'title': 'Book 4', 'isbn': '0000000000004'})
    db.books.insert_one({'title': 'Book 5', 'isbn': '0000000000005'})
    print("Done")
else:
    print("Books already inserted.")


db_operations.make_favorite_for_user(11, '0000000000001', db)
db_operations.check_book_by_isbn('0000000000001', db)

