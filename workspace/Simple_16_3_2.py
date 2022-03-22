import csv
file_a = open("file_name.csv", "w", newline="")

write_f = csv.writer(file_a)
write_f.writerow(["產品名稱", "產品價格"])

file_a.close()

file_a = open("file_name.csv", "a", newline="")

write_f = csv.writer(file_a)
write_f.writerows([["coffee", 100], ["tea", 90]])

file_a.close()

file_a = open("file_name.csv", "a", newline="")

write_f = csv.writer(file_a)
data = {"juice": 70, "milk": 60}
for i in data:
    write_f.writerow([i, data[i]])

file_a.close()
