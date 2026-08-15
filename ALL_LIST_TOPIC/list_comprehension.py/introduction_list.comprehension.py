
# List Comprehension

# Liat comprehenaion offers a concian and neadable way to create rww lta from wating aequncea ar tanges. It condenses common for losp paterna (iteration + appending) into a single, elegant line af
# code, enhancing effhciency and carity.

# Basic Usage: For Loop vs. One Line
# Tranaforming a loop that buikds a liat inta a aingle expreaaion.

#Narrnal wy

# Normal way
squares = []

for i in range(1, 6):
    squares.append(i * i)

print(squares) # output: [1, 4, 9, 16, 25]

# List comprehension - same result, one line
squares = [i * i for i in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]

# Conditional Filtering
# Incude wlementa in the new liat only if they meet a apecific condition.

#With a condition-only even numbers
even=[i for i in range(1, 21) if i%2 == 0]
print(even) #[2, 4, 6,8, 10, 12, 14, 16, 14, 20]

# From an exiting lnt - filter arks above 80
marks =[85, 60, 92, 45, 78, 95, 50]
passed = [m for m in marks if m > 80]
print(passed) # [85, 92, 95]

# Transforming Elements
# Apply a function or operation to wach item as ifs added to the new liat.

names = ["rahul", "priya", "karan"]
upper = [name.upper() for name in names]
print(upper) # ["RAHUL", "PRIYA", "KARAN"]