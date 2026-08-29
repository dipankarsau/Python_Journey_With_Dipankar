# Q85: Dictionary Merge Function
# Write a Python function named merge_dicts(d1, d2) that accepts two
# dictionaries (d1 and d2) as arguments and returns a new dictionary
# formed by merging them using the update() method. Ensure d1 remains
# unchanged.

def merge_dict(dict1,dict2):
    new={}
    new.update(dict1)
    new.update(dict2)
    return new
d1={"a":1,"b":2,"c":3}
d2={"d":4,"e":5,"f":6}
print(merge_dict(d1,d2))