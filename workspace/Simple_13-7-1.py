def turnover(price, number, discount):
    tot = price * number
    dis_tot = tot * discount
    return tot, dis_tot


product_name = "coffee"
product_price = 100
sales_number = 44
product_discount = 0.9
t_o = turnover
print("t_o的資料型態", type(t_o))
total, after_discount = t_o(product_price, sales_number, product_discount)
print("產品:", product_name, total, "元", "打折後共:", after_discount, "元")
