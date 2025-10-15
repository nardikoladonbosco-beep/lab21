from C_factories import Book, Member

books = [
    Book("97899943", "Python Bazë", "A. Hoxha", 1200.0),
    Book("97822222", "Programim Web", "E. Lika", 800.0),
]

try:
    books.append(Book.from_string("97811111;Algoritme;B. Dervishi;900"))
except ValueError as e:
    print("Gabim:", e)

try:
    books.append(Book.from_string("gabim;pa;format"))
except ValueError as e:
    print("Gabim:", e)

members = [
    Member(12, "Arta Kola", "arta.kola@shkolla.al"),
    Member(15, "Blerina Dema", "blerina.dema@shkolla.al"),
    Member.anonymous()
]

print("\nLIBRAT:")
count_over_1000 = 0
for b in books:
    base = b._format_money(b.price)
    discounted = b._format_money(b.apply_discount(20))
    print(f'- {b} | Bazë: {base} | -20%: {discounted}')
    if b.price > 1000:
        count_over_1000 += 1

print("\nANËTARËT:")
for m in members:
    print(f'- {m}')

print(f"\nTot > 1000 L: {count_over_1000}")
