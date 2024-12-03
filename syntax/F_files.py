# write to file

with open('output.txt', 'w') as f:
    f.write("Hello, File!\n")

#reading from a file
with open('input.txt', 'r') as f:
    for line in f:
        print(line.strip()) 