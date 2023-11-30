def order(*drink):
    for i in drink:
        if i == 'Эспрессо' and in_stock["coffee"] >= 1:
            in_stock["coffee"] -= 1
            return i
        elif i == 'Капучино' and in_stock["coffee"] >= 1 and in_stock["milk"] >= 3:
            in_stock['coffee'] -= 1
            in_stock["milk"] -= 3
            return i
        elif i == 'Макиато' and in_stock["coffee"] >= 2 and in_stock["milk"] >= 1:
            in_stock["coffee"] -= 2
            in_stock["milk"] -= 1
            return i
        elif i == 'Кофе по-венски' and in_stock["coffee"] >= 1 and in_stock["cream"] >= 2:
            in_stock["coffee"] -= 1
            in_stock["cream"] -= 2
            return i
        elif i == 'Латте Макиато' and in_stock["coffee"] >= 1 and in_stock["milk"] >= 2 and in_stock["cream"] >= 1:
            in_stock["coffee"] -= 1
            in_stock["milk"] -= 2
            in_stock["cream"] -= 1
            return i
        elif i == 'Кон Панна' and in_stock["coffee"] >= 1 and in_stock["cream"] >= 1:
            in_stock["coffee"] -= 1
            in_stock["cream"] -= 1
            return i
    return 'К сожалению, не можем предложить Вам напиток'

in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))