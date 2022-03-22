def fee(a, b, c, parking_fee=10, cleaning_fee=5, severice_fee=5):
    print("fee a", a, "fee b", b, "fee c", c)
    print("停車費", parking_fee, end="\t")
    print("清潔費", cleaning_fee, end="\t")
    print("服務費", severice_fee)
    print("Total:", parking_fee + cleaning_fee + severice_fee)


fee(10, 20, 30)


def fee(a, b, c, parking_fee=10, cleaning_fee=5, severice_fee=5):
    print("fee a", a, "\tfee b", b, "\tfee c", c)
    print("停車費", parking_fee, end="\t")
    print("清潔費", cleaning_fee, end="\t")
    print("服務費", severice_fee)
    print("Total:", a + b + c + parking_fee + cleaning_fee + severice_fee)


fee(10, 20, 30, 40, 50, 60)


def fee(a, b, c, parking_fee=10, cleaning_fee=5, severice_fee=5):
    print("fee a", a, "\tfee b", b, "\tfee c", c)
    print("停車費", parking_fee, end="\t")
    print("清潔費", cleaning_fee, end="\t")
    print("服務費", severice_fee)
    print("Total:", a + b + c + parking_fee + cleaning_fee + severice_fee)


fee(10, 20, 30, cleaning_fee=50)


def fee(a, b, c, parking_fee=10, cleaning_fee=5, severice_fee=5):
    print("fee a", a, "\tfee b", b, "\tfee c", c)
    print("停車費", parking_fee, end="\t")
    print("清潔費", cleaning_fee, end="\t")
    print("服務費", severice_fee)
    print("Total:", a + b + c + parking_fee + cleaning_fee + severice_fee)


fee(10, 20, 30, cleaning_fee=50, parking_fee=60)


def function_sample(*args):
    print("初讀進來的資料:", args)
    print("初讀進來的資料型態:", type(args))


function_sample(31, 21, 54, 61)
