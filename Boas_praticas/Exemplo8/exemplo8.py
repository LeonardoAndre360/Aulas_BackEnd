from pydantic import BaseModel, ValidationError

class Book(BaseModel):
# Book: Define um modelo de dados para um livro, 
# com campos para título, autor e número de páginas, 
# utilizando a tipagem avançada do Pydantic.
    title: str
    author: str
    pages: int

try:
# try: Tenta criar uma instância do modelo Book com dados válidos. 
# Se os dados não corresponderem aos tipos definidos, uma exceção ValidationError será lançada
    book = Book(title="Clean Code", author="Robert C. Martin", pages=464)
    print(book)
# print(book): Se a validação for bem-sucedida, o objeto book é impresso, mostrando que os dados foram validados corretamente.
except ValidationError as e:
    print(e)