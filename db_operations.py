def make_favorite_for_user(user_id, isbn_str, db):
    """
    Error: The same user can be added few times
    :param user_id:
    :param isbn_str: 
    :param db:
    :return:
    """
    book = db.books.find_one({'isbn': isbn_str})
    # noinspection PyBroadException
    try:
        book['favorite'].append(user_id)
    except:
        book['favorite'] = []  # make new field
        book['favorite'].append(user_id)
    finally:
        db.books.update({'_id': book.get('_id')}, book)


def check_book_by_isbn(isbn_str, db):
    book = db.books.find_one({'isbn': isbn_str})
    print(book)
