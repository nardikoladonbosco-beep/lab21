from A_models import Book, Member

class Book(Book):
    def apply_discount(self, percent):
        if not (0 <= percent <= 50):
            raise ValueError("Zbritja duhet të jetë midis 0 dhe 50%.")
        discounted = self.price * (1 - percent / 100)
        return round(discounted, 2)

    def _format_money(self, value):
        return f"{value:.2f} L"


class Member(Member):
    def change_email(self, new_email):
        if "@" not in new_email or "." not in new_email:
            raise ValueError("Email i ri nuk është i vlefshëm.")
        self.email = new_email
