# Q82: World Capitals (HW)
# Create a dictionary mapping five countries to their capital cities. Iterate
# through this dictionary using the items() method and print each pair in
# the format: Country → Capital.






capitals = {
    "India": "New Delhi",
    "France": "Paris",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "Italy": "Rome"
}
# print(capitals.items())
# for i in capitals:
#     print(capitals[i])
for k,v in capitals.items():
    print(k,v)