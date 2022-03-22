try:
    file_a = open("RRR.txt", "r")
except FileNotFoundError:
    print("please check your file.")
