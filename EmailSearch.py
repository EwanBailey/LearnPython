email_list = []

emails = open("text-file-mail-short.txt")

for line in emails:
    if "@" in line:
        line = line.strip()
        words = line.split()
        for word in words:
            if "@" in word:
                email_list.append(email)
for email in email_list:
    print(email)
