# marks = {
# "akshy": [43, 12, 98, 10, 22],
# "priya": [76, 55, 34, 89, 61],
# "rahul": [20, 45, 67, 30, 88],
# "sneha": [91, 73, 50, 14, 62],
# "karan": [38, 82, 47, 95, 29],
# }
# # ans = dict(sorted(marks.items(), key=lambda x:x[1][-1]))
# # print(ans)

# ans=dict(sorted(marks.items(), key=lambda X :sum(X[1]),reverse=True))
# print(ans)





students = {
"anirudh": {"math": 87, "science": 92, "english": 74},
"priya": {"math": 65, "science": 78, "english": 90},
"rahul": {"math": 55, "science": 60, "english": 48},
"sneha": {"math": 95, "science": 88, "english": 82},
"karan": {"math": 70, "science": 45, "english": 63},
}

# ans = dict(sorted(students.items(), key= lambda x:x[1]["math"]))
# print(ans)

# ans = dict(sorted(students.items(), key= lambda x:x[1]["math"]+x[1]["science"]+x[1]["english"]))
ans=dict(sorted(students.items(), key=lambda X :sum(X[1].values())))
print(ans)