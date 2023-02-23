import csv

def sales():
    with open('sales.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
sales()


def salespermonth():
    with open('sales.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            month_sales = row[1] + "    " + row[2]
            print(month_sales)
salespermonth()

import csv
import operator


with open("sales.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

monthly_sales = {}


for row in data:
    month = row["month"]
    sales = float(row["sales"])
    if month in monthly_sales:
        monthly_sales[month] += sales
    else:
        monthly_sales[month] = sales


sorted_sales = sorted(monthly_sales.items(), key=operator.itemgetter(1), reverse=True)


print("The month with the highest sales is", sorted_sales[0][0])
print("The month with the lowest sales is", sorted_sales[-1][0])
