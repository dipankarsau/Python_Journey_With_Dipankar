import json

l=[1,2,3,4]
with open(" demo.json","w") as f:
    json.dump(l,f)