# Q82: World Capitals (HW)
# Create a dictionary mapping five countries to their capital cities. Iterate through this
# dictionary using the items() method and print each pair in the format: Country -+
# Capital
countries = {
    "India": "New Delhi",
    "France": "Paris",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "Italy": "Rome"
}
for i in countries.items():
    print(i[0], "-", i[1])