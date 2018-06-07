infile = open("Sample2.txt", 'r')
line1 = infile.readlines()
file = open("answer.txt", "w")
count = 0
for line in line1:
    with open('Sample2.txt', 'r') as f:
        for line in f:
            for word in line.split():
                print(word)

