
import random
# Первое число
first_number = random.randint(1, 100)
# Второе число
second_number = random.randint(1, 70)
while second_number > first_number:
    first_number = random.randint(1, 100)
H = (first_number + second_number)
while H > 100:
    first_number = random.randint(1, 100)
    H = (first_number+second_number)
print("Найти сумму чисел")
print( "Первое число",first_number)
print( "Второе число", second_number)
p = (first_number + second_number)
g = int(input("Алиса какой ответ = "))
while g != p:
   g = int(input("Алиса попробуй еще = "))
else:
    g = p
print("Правильно, Умница!!!!")
