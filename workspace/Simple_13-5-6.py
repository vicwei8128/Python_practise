def function_2():
    product_name = "coffee"
    print("3.\t產品名稱:", product_name)


def function_1():
    product_price = 50
    function_2()
    print("2.\t產品價格:", product_price)


product_price = 100
print("1.\t產品價格:", product_price)
function_1()


def function_1():
    product_price = 50

    def function_2():
        product_name = "coffee"
        print("3.\t產品名稱:", product_name)

    function_2()
    print("2.\t產品價格:", product_price)


product_price = 100
print("1.\t產品價格:", product_price)
function_1()


def function_1():
    product_price = 50
    product_name = "sting"
    def function_2():
        nonlocal product_name
        product_name = "coffee"
        print("3.\t產品名稱:", product_name)

    function_2()
    print("4.\t產品名稱:", product_name)
    print("2.\t產品價格:", product_price)


product_price = 100
product_name = "ABCD"
print("1.\t產品價格:", product_price)
function_1()
print("5.\t產品名稱:", product_name)