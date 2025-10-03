n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))
apples_students = k // n
results = k % n
print("Каждму школьнику достанется: ", apples_students, "яблок")
print("В корзинке останется: ", results, "яблок")
