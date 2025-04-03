xfile = open('text-file-matrix.txt')
files = xfile.read()
xfile.close() 

print('Number of Characters =', len(files))
index = files.find("red pill")

if index != -1:
    print(f'index of red pill: {index}')
    print(f'{files[index:index+8]}')
else:
    print('red pill not found')
