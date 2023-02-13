per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

print(per_cent)

count = int(input('Введите ссумму вклада:'))

income = [float(count + count * 0.056), float(count + count * 0.059), float(count + count * 0.0428), float(count + count * 0.04)]

print(income)

print("Максимальная сумма, которую вы можете заработать —", max(income))