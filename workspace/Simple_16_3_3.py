import csv
file_a = open("file_name.csv", "r", newline="")

read_f = csv.reader(file_a)
print("read_f:", read_f)
for i in read_f:
    print(i)

file_a.close()
