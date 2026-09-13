# with open("new txt","w") as f:
#     f.write("good bye\n")
#     f.write(" hello world")


lines = ['first line\n', 'abcd\n', 'dwgyddwdwdwdvdv\n']
with open("new.text","w") as f:
    f.writelines(lines)

   