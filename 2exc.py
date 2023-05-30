number = int(input(""))
if number == 0 or number < 0:
    print('неправильный номер')
elif number % 2 == 0 and number <= 36:
    print('верхнее')
elif number % 2 != 0 and number <=36:
    print("нижнее")
elif number % 2 == 0 and number > 36:
    print('верхнее боковое')
else:
    print('нижнее боковое')