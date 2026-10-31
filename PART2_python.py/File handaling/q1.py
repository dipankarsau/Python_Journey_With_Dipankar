import json

l = ["apple", "mango", "banna", "ewfbhfbuw"]

# Write JSON file
with open("parctic2.json", "w") as f:
    json.dump(l, f)

# Read JSON file
with open("parctic2.json", "r") as f:
    print(json.load(f))


# Return final element
def get_final_line(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)
        return data[-1]


print(get_final_line("parctic2.json"))