from fileinput import filename
import os
lines = []
my_dir = os.getcwd()
for subdir, dirs, files in os.walk(my_dir):
    print(subdir,files)
    for fname in files:
        with open(os.path.join(os.getcwd(),fname), "r", encoding='utf-8', errors='ignore') as fin:
            for line in fin:
                line.strip()
                lines.append(line)

# for e in lines:
#     print(e)
f = open("Okayama.txt","w")
for e in lines:
    f.write(e+"")

