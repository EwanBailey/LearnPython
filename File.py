fhand = open('text-file-mail-short.txt')
count = 0  

for line in fhand:
    count += 1 
    print(line.strip())

print('Line Count:', count)
