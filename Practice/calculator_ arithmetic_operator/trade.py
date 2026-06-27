buy_price = float(input("Enter your buy price : "))
sell_price = float(input("Enter your sell price :"))
quantity = int(input("Enter total qiantity you bought :"))

total_invested = buy_price*quantity
total_returned = sell_price*quantity
profit_loss = total_returned - total_invested
change = (profit_loss) / (total_invested) *10

# print(f"Your buy price is : {buy_price}")
# print(f"Your sell price is : {sell_price}")
# print(f"The quantity is : {quantity}")
print(f"--------------------------")
print(f"Trade summary :")
print(f"Your buy price is : {buy_price}")
print(f"Your sell price is : {sell_price}")
print(f"The quantity is : {quantity}")
print(f"--------------------------")
print(f"Your total total invested is : {total_invested}")
print(f"Your total returned is : {total_returned}")
print(f"The profit/loss is : {profit_loss}")
print(f"The change is : {change}")