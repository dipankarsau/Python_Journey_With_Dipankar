marks={"science":99,"maths":100,"hindi":43,"history":71,}
# print(marks["science"])
# a=marks.get("science")
# print(a)
subject="history"
ans= marks.get(subject)
if ans is None:

    print("subject not found")
else:
    print(f"marks scored ={ans}")