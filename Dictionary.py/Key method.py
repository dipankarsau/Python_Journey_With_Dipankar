maths={
    "science":99,
    "maths":100,
    "comp":88,
    "hindi":43,
    "history":71,
}
total=0
for subject in  maths.keys():
    print(subject,maths[subject])
    total=total+maths[subject]
print(total)