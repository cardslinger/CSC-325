import os

dir = "C:/Users/omega/PycharmProjects/CleaningScript/dirty"
cleandir = "C:/Users/omega/PycharmProjects/CleaningScript/clean"

for file in os.listdir(dir):
    filename = dir + "/" + str(file)
    cleanfile = cleandir + "/" + str(file)
    output = ""
    if str(filename).endswith(".txt"):
        file = open(filename)
        for line in file:
            splitline = line.split(",")
            if len(splitline[1]) == 0 or len(splitline[2]) == 0 or len(splitline[3]) == 0 or len(splitline[4]) == 0:
                continue
            output += line
        outfile = open(cleanfile, 'w')
        outfile.write(output)
        outfile.close()
        file.close()

