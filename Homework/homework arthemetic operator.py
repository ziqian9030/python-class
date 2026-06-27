price1 = float(input("Enter you price for item 1 : "))
qty1 = int(input("Enter how many you bought for item 1 : "))

price2 = float(input("Enter you price for item 2 : "))
qty2 = int(input("Enter how many you bought for item 2 : "))

price3 = float(input("Enter you price for item 3 : "))
qty3 = int(input("Enter how many you bought for item 3 : "))

total1 = price1 * qty1
total2 = price2 * qty2
total3 = price3 * qty3
total_all = total1+total2+total3

print(f"Shopping bill : ")
print(f"Item 1 : {total1}")
print(f"Item 2 : {total2}")
print(f"Item 3 : {total3}")
print("-------------------")
print(f"Total is {total_all}")  