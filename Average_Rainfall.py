years = int(input("Enter the number of years: "))
while years <= 0:
    print("Enter a value greater than 0: ")
    years = int(input("Enter the number of years: "))
totalRainfall = 0
totalMonths = 0
for year in range(1, years + 1):
    print(f"\nYear {year}")
    for month in range(1, 13):
        rainfall = float(input(f"Enter rainfall for month {month} (in inches): "))
        while rainfall < 0:
            print("Error: rainfall cannot be negative")
            rainfall = float(input(f"Enter rainfall for month {month} (in inches): "))
        totalRainfall += rainfall
        totalMonths += 1
averageRainfall = totalRainfall / totalMonths
print("\nRainfall Summary")
print(f"Total months: {totalMonths}")
print(f"Total rainfall: {totalRainfall:.2f} inches")
print(f"Average rainfall per month: {averageRainfall:.2f} inches")