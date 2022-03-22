#Data input from keyboard
product_name = input("Please enter product name:")
product_price = int(input("Please enter product price:"))
sale_number = int(input("Please enter count:"))

#Calculate
total_price = product_price * sale_number

#print to screen
print(product_name, "\t價格", product_price, "元/單位")
print("銷售金額:", sale_number, "單位")
print("總金額:", total_price, "元")

#錯誤示範
num_1 = input("Please enter first number:")
num_2 = input("Please enter second number:")

#Calculate
total_number = num_1 + num_2

#print to screen
print("總數為:", total_number)