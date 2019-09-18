def make_favorite_for_user(user_id, isbn_str, db):
    """
    Make book (isbn_str) favorite for (user_id)
    :param user_id:
    :param isbn_str:
    :param db:
    :return:
    """
    db.books.update({'isbn': isbn_str}, {'$addToSet': {'favorite': user_id}})


def check_book_by_isbn(isbn_str, db):
    book = db.books.find_one({'isbn': isbn_str})
    print(book)
