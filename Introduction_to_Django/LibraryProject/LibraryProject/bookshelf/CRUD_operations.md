 create.md
 >>> book = Book(title='1984', author='George Orwell', publication_year='1949')
>>> book.save()
  retrieve.md
  >>> book = Book.objects.get(id=1)
>>> print(book.title, book.author, book.publication_year)
1984 George Orwell 1949
  update.md
   book = Book.objects.get(id=1)
>>> book.title = 'Nineteen Eighty-Four' 
>>> book.save()
>>> print(book.title, book.author, book.publication_year)
Nineteen Eighty-Four George Orwell 1949
delete.md
>>> Book.objects.filter(id=1).delete()
(1, {'bookshelf.Book': 1})