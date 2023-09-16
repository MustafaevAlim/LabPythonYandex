name = input()
price, weight, money = map(int,input().split())

first_string = f"{'Чек' :=^35}"
last_string = '=' * 35

name_string = f"Товар:{name : >29}"

price_substring = f"{weight}кг * {price}руб/кг"
price_string = f"Цена:{price_substring : >30}"
final_string_price = f"Итого: {weight * price : >28}"

money_given_string = f"Внесено:{money : >24}руб"

change_string = f"Сдача:{money - weight*price : >26}руб"

print(first_string)
print(name_string)
print(final_string_price)
print(money_given_string)
print(change_string)
print(last_string)