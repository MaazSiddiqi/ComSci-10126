with open('file.txt', 'r') as inp, open('myfile.txt', 'w') as out:  # all parameters in open() should be a string
    line = inp.readline()   # must be inp.readline() to read whole line
    words = line.split()
    for word in words:
        print(word)                 # Printing to new line only requires the variable, no need to mannually add a newline character
        out.write(word + "\n")      # need to add new line character in .write() though
