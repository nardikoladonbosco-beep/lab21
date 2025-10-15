from B_methods import Book, Member

class Book(Book):
    @classmethod
    def from_string(cls, data):
        try:
            isbn, title, author, price = data.split(";")
            return cls(isbn, title, author, float(price))
        except Exception:
            raise ValueError("Formati i të dhënave nuk është i vlefshëm.")

class Member(Member):
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

    @classmethod
    def anonymous(cls):
        return cls(0, "Anonim", "anonim@shkolla.al")
