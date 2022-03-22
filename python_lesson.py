a = 100
b = 8.9
c = 'hello'
'{} {} {}'.format(a, b, c)
'{0} {1} {2}'.format(a, b, c)
'{2} {1} {0}'.format(a, b, c)
print('{} {} {}'.format(a, b, c))
print('{0} {1} {2}'.format(a, b, c))
print('{2} {1} {0}'.format(a, b, c))

'Coordinates: {latitude}, {longitude}'.format(latitude='25.019N', longitude='121.54E')
print('Coordinates: {latitude}, {longitude}'.format(latitude='25.019N', longitude='121.54E'))

coord = {'latitude': '25.019N', 'longitude': '121.54E'}
'Coordinates: {latitude}, {longitude}'.format(**coord)
print('Coordinates: {latitude}, {longitude}'.format(**coord))

# ('the complex number {0} contains real part {0.red} and imaginary part {0.imag}').format(a)
# print(('the complex number {0} contains real part {0.red} and imaginary part {0.imag}').format(a))

coord = (8, 9)
'X:{0[0]}; Y: {0[1]}'.format(coord)
print('X:{0[0]}; Y: {0[1]}'.format(coord))

'{0:10d} {1:10f} {2:10s}'.format(a, b, c)
# 10=預留10個空白 D=decimal 十進位
# f=浮點數 s=string字串
print('{0:10d} {1:10f} {2:10s}'.format(a, b, c))
'{0:>10d} {1:<10f} {2:^10s}'.format(a, b, c)
# >往右靠 <往左靠 ^置中
print('{0:>10d} {1:<10f} {2:^10s}'.format(a, b, c))

'int:{0:d}; bin:{0:b}; oct:{0:o}; hex:{0:x}'.format(99)
print('int:{0:d}; bin:{0:b}; oct:{0:o}; hex:{0:x}'.format(99))
'int:{0:#d}; bin:{0:#b}; oct:{0:#o}; hex:{0:#x}'.format(99)
# b二進位 o八進為 x十六進位 前面加#強調他是甚麼進位
print('int:{0:#d}; bin:{0:#b}; oct:{0:#o}; hex:{0:#x}'.format(99))

'{:,}'.format(1234567890)
print('{:,}'.format(1234567890))
# 用逗號代表每三位數自動加一次逗號

a = 33
b = 19
'percentage = {:.2%}'.format(b / a)
print('percentage = {:.2%}'.format(b / a))
# 顯示百分比顯示小數點後兩位

import datetime

d = datetime.datetime(2020, 1, 1, 12, 33, 43)
'{:%Y-%m-%d %H:%M:%S}'.format(d)
# Y年 m月 d日 H小時 M分鐘 S秒
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

import re

txt = "Go Go PowerRanger!"
x = re.search('Go', txt)
print(x)
print(type(x))

b = re.search('ef', 'abcdef')
print(b.group())


def requiredArg(name, grade):
    print(name + "'s math grade is: %s" % grade)


requiredArg('Marc', 98)


def defaultArg(name, msg='Morning~'):
    print(msg + name)


defaultArg('Celine')


def varnumArg(*meals):
    # 當函數值不確定有多少可以用*表示
    for meal in meals:
        print(meal)


varnumArg('Pie', 'Ramen', 'Pasta')


def dinner(**kwargs):
    # 兩個**代表吃dictionary
    print('keyword argument:', kwargs)


dinner(wine='cave', entree='lamb', dessert='tiramisu')


def returnExample():
    a = 'Hi'
    b = 'Hello'
    c = 'Hey'
    return a, b, c


returnExample()
print(returnExample())

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = list(filter(lambda x: (x % 3), my_list))
odd_list = list(filter(lambda x: (x % 2 == 1), my_list))
# %符號是取餘數 list == 0 所以不會顯示
print(list2)
print(odd_list)

sqrt_list = list(map(lambda x: x ** 2, my_list))
print(sqrt_list)

from functools import reduce

my_list = [5, 8, 10, 20, 50, 100]
reduce_result = reduce(lambda x, y: x + y, my_list)
print(reduce_result)


def square(x):
    return x ** 2


print(list(map(square, [1, 2, 3, 4, 5])))


# 費氏數列
def F(n):
    if n == 0 or n == 1:
        return n
    else:
        return F(n - 1) + (n - 2)


print(F(6))


def fibonacciVal(n):
    memo = [None] * (n + 1)
    memo[0], memo[1] = 0, 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    print(memo)
    return memo[n]


print(fibonacciVal(8))


class Banks():
    title = 'Taiwan Bank'

    def __init__(self, uname, money):
        self.name = uname
        self.balance = money
        # self.__balance = money 加__私有化，無法透過外部修改

    def save_money(self, money):
        self.balance += money
        print("存款", money, "完成")

    def withdraw_money(self, money):
        self.balance -= money
        print("提款", money, "完成")

    def get_balance(self):
        print(self.name, "目前餘額:", self.balance)
        # calling self defined instance


user_action = Banks('Python', 1000)
user_action.get_balance()
user_action.save_money(500)
user_action.get_balance()
user_action.withdraw_money(300)
user_action.get_balance()


# print(user_action.name.title(), 'has:', user_action.get_balance())

class Banks():
    def __init__(self, uname):
        self.__name = uname
        self.__balance = 0
        self.__bankname = "Taipei Bank"
        print("HI", self.__name)


isaacbank = Banks('isaac')


# print(isaacbank.__name) 因為__無法做修改

class Banks():
    def __init__(self, uname):
        self.__name = uname
        self.__balance = 0
        self.__bankname = "Taipei Bank"
        print("HI", self.__name)


class Shilin_Banks(Banks):
    pass


isaacbank = Banks('isaac')


# Write a Python class named Circle construsted by a radius
# and two methods which will compute the area and the perimeter
# of a circle
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14


NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())


# Write a Python class which has two methods
# get_String and print_String.get_String accept
# a string from the user and print_String print
# the string in upper case.
class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("請輸入(小寫轉大寫):")

    def print_String(self):
        print(self.str1.upper())


str1 = IOString()
str1.get_String()
str1.print_String()


# Define a class called Songs, it will show the
# lyrics of a song. Its init() method should have
# two arguments: self and lyrics(a list).
# Inside your class create a method called
# "sing_me_a_song" that prints each element of
# lyrics on his own Line. Define a varible.
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["May god bless you,",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])
happy_bday.sing_me_a_song()


# We have a class defined for vehicles. Create two
# new vehicles called car1 and car2. Set car1 to
# be a red(color) convertible(kind) worth 60,000(value)
# with a name of Fer(name), and car2 to be a blue(color)
# van(kind) named Jump(name) worth 10,000(value)
class Vehicle():
    name = ""
    kind = "car"
    color = ""
    value = 100

    def description(self):
        desc_str = "{} is a {} {} worth {}".format(self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000

print(car1.description())
print(car2.description())


# Create a Temperature class. Make two methods:
# 1.convertFahrenheit - it will take celsius and
# will print into Fahrenheit
# 2.convertCelsius - It will take Fahrenheit and
# will convert it into Celsius

class Temperature():
    def covertFahrenheit(self, celsius):
        return (celsius * (9 / 5)) + 32

    def covertCelsius(self, fahrenhiet):
        return (fahrenhiet - 32) * (5 / 9)


t = Temperature()
print(t.covertCelsius(0))
print(t.covertFahrenheit(0))


# Create a Time class and initialize it with hours and minutes.
# 1.Make a method addTime which should take two
# time object and add them.
# E.g.-(2 hour and 50 min)+(1hr and 20 min)is
# (4hr and 10 min)
# 2.Make a method displayTime which should print the time
# 3.Make a method DisplayMinute which should display
# the total minutes in the Time
# E.g.-(1hr2min)should display 62 min
class Time():
    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins

    def addTime(self, t1, t2):
        t3 = Time(0, 0)
        if t1.mins + t2.mins > 60:
            t3.hours = t3.hours + t1.hours + t2.hours + (t1.mins + t2.mins) // 60
            t3.mins = t3.mins + t1.mins + t2.mins - 60
        else:
            t3.hours = t3.hours + t1.hours + t2.hours
            t3.mins = t3.mins + t1.mins + t2.mins
        return t3

    def displayTime(self):
        print("Time is " + str(self.hours) + "hours and " + str(self.mins) + "minutes.\n")

    def displayMinute(self):
        print("Time is " + str(self.hours * 60) + str(self.mins) + "mins")


a = Time(2, 59)
b = Time(1, 20)
c = a.addTime(a, b)
c.displayTime()
c.displayMinute()


# Please define a Shape class as following and
# define Circle Class and Rectangle Class to inherit
# from Shape. In Circle and Rectangle Class, please
# add function cal_area to calculate area and
# add function cal_perimeter to calculate perimeter.
class Shape():
    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled

    def cal_area():
        pass

    def cal_perimeter():
        pass

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self, filled):
        set.__filled = filled


class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.__r = r

    def cal_area(self):
        return self.__r * self.__r * 3.14

    def cal_perimeter(self):
        return 2 * self.__r * 3.14


class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__()

        self.__width = width
        self.__height = height

    def cal_area(self):
        return self.__height * self.__width

    def cal_perimeter(self):
        return 2 * (self.__height + self.__width)


c1 = Circle(10)
print(c1.cal_area())
print(c1.cal_perimeter())
print(c1.get_color())
c1.set_color('white')
print(c1.get_color())
print('==============')
r1 = Rectangle(2, 5)
print(r1.cal_area())
print(r1.cal_perimeter())
print(r1.get_color())
r1.set_color('yellow')
print(r1.get_color())


## Write a Python prograrm that takes a text file
## as input and returns the number of word.txt
# with open('words.txt') as f:
#     data = f.read()
#     data.replace(",", " ")
#     print(len(data.split(" ")))

## Write a Python program to count the number
## of lines in a text file.
# def file_lengthy(fname):
#     f = open(fname, "r")
#     contents = f.readlines()
#     return len(contents)
#
#
# print("Number of lines in the file: ", file_lengthy("englis_new.txt"))

## Write a Python program to write a list content to a file.
# color = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
# with open('color_write.txt', "w") as my_list:
#     for c in color:
#         my_list(c+"\n")

## Write a python program to find the longest words.
# def longest_word(filename):
#     max_long = 0
#     max_word = ''
#     with open(filename, 'r') as f:
#         contents = f.read().replace('\n', ' ')
#         words_list = contents.split(' ')
#         for i in words_list:
#             if len(i) > max_long:
#                 max_long = len(i)
#                 max_word = i
#     return max_word
#
#
# print(longest_word('english_new.txt'))


