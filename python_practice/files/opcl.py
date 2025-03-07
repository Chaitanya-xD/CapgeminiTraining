file = open("sample.txt","w")
file.write(f"Hello, this is a sample text\n")
file.close()

file = open("sample.txt","a")
file.write(f"Hello, this is a sample text 2")
file.close()

