#Data 
sales = [14434.65, 21222.61, 16554.34, 15445.32, 16054.52, 19005.23, 22222.22, 17466.29, 11345.21, 14333.43, 14444.45, 21222.10]
profit = [1222, -500, 1343, 2222, 2122, 3122, 1000, 5330, 2123, 4332, 2221, 3213]




#Solution
#Calculate Profit ratio As The factor of Sales And Profit
profitratio = []

for i in range (0, len(sales)):
    profitratio.append(profit[i] / sales[i])
profitratio


#Calculate mean sales and profit
mean_sales = sum(sales) / len(sales)
mean_sales

mean_profit = sum(profit) / len(profit)
mean_profit



#Find The Months With Above-Mean Profit 
good_months = []
for i in range (0, len(profit)):
    good_months.append(profit[i] > mean_profit)
good_months


#Bad Months Are The Opposite Of Good Months!
bad_months = []
for i in range (0, len(profit)):
    bad_months.append(profit[i]< mean_profit)
bad_months


#The Best Month Is Where Profit Was Equal To The Maximum
best_month = []
for i in range (0, len(profit)):
    best_month.append(profit[i] == max(profit))
best_month


#The Worst Month Is Where Profit Was Equal To The Minimum
worst_month = []
for i in range (0, len(profit)):
    worst_month.append(profit[i] == min(profit))
worst_month



