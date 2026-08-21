marks = {"math": 85, "science": 92, "english": 60, "hindi": 78}

ans = dict(sorted(marks.items(), key=lambda x: x[1]))

print(ans)