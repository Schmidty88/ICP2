infile = open("sample.txt", 'r')
line1 = infile.readlines()
file = open("answer.txt", "w")
for line in line1:
    length = len(line)
    file.write("The Frequency is: ")
    file.write(str(length))
    file.write(" ")
    file.write(line)
file.close()


