def turnover(price, number, discount):
    tot = price * number
    dis_tot = tot * discount
    return tot, dis_tot


product_name = "coffee"
product_price = 100
sales_number = 44
product_discount = 0.9
total, after_discount = turnover(product_price, sales_number, product_discount)
print("產品", product_name, "原價共", total, "元", "打折後共", after_discount, "元")
