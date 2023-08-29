s = ["txt", "pdf", "docx", "xlsx"]
name = input().split(".")
print(name[-1] in s)
