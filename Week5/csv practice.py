import csv

region_units = {}
region_revenue = {}
regions = {}

current_region = ""
current_units = 0
current_revenue = 0


f = open("region_input.csv", 'rt')

reader = csv.reader(f)

#Below will skip header in the CSV
my_header = next(reader)

# Read the input file
for row in reader:


    # Get the current row values
    current_region = row[0]
    current_units = row[1]
    current_revenue = row[2]

    if not current_region in region_units:
        region_units[current_region] = current_units
    else:
        region_units[current_region] = int(region_units[current_region]) + int(current_units)

regions = list(region_units.keys())

print(regions)

print("All the regions found are: ", end="")
for r in regions:
    print(r, end = ", ")
print()

print("Totals per region")

for r in regions:
    print(r)
    print("Total units for region: " + str(region_units[r]))
    print()



