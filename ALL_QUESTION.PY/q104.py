# Q101. File Type Check

# Take a filename as input (like report.pdf). Check if it ends with .pdf, .docx,
# or .txt and print the file type.

filename = "report.pdf"
if filename.endswith(".pdf") or filename.endswith (".jpg") or  filename.endswith(".txt"):
    print("valid file")
else:
    print("please enter a valid file")
