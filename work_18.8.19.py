ticket = int(input("Введите количество билетов:"))
price = 0
if ticket > 0:
    for i in range(ticket):
        age = int(input("Введите возраст посетителя:"))
        if 18 <= age <25:
            price += 990
            print("Цена билета  990 р.")
        elif age >= 25:
            price += 1390
            print("Цена билета 1390 р.")
        elif 0 <= age <18:
            price += 0
            print("Цена билета 0 р.")
        else:
            print("Ошибка, введено отрицательное значение возраста!")
            break
else:
    print("Ошибка, введно отрицательное колличество билетов!")
if ticket > 3:
    discount =  price - price / 10
    print(f"Цена билетов со скидкой {discount} от полной цены {price}!")
else:
    print(f"Цена билетов: {price}")