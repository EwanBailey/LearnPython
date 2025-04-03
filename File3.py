xfile = open('text-file-mail-very-short.txt")
for line in xfile:
  line=line.rstrip()
  if (line.startswith("From:")):
      print(line)
