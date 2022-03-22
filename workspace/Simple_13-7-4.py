def decorate(func):
    print("Whar is func", func)

    def wrapper():
        pass

    return wrapper


@decorate
def message_name():
    pass


# @decorate
message_name = decorate(message_name)
pass


def decorate(func):
    print("Whar is func", func)

    def wrapper(data):
        print("In wrap:", data)
        data_m = "------------" + data + "------\t好喝"
        return func(data_m)

    return wrapper


@decorate
def message_name(par):
    print(par)


message_name("coffee")
