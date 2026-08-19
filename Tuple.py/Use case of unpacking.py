# make a function which return min and max a list
def greeet(lst):
    mini=min(lst)
    maxi=max(lst)
    return mini,maxi
ans1,ans2=greeet([5,7,3,67,7,43,1])
print(f"minimum is {ans1}, maximum is {ans2}")
