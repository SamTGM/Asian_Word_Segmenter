from fileinput import filename
import os
import string
lines = []
exclude = ['ads','@','[/]','(','x','<','[','=', "'", '{']
alpha = string.ascii_lowercase
punc = '''!-{};:'"\./?@#$%^&*_~'''
my_dir = os.getcwd()
for subdir, dirs, files in os.walk(my_dir):
    for fname in files:
        with open(os.path.join(os.getcwd(),fname), "r", encoding='utf-8', errors='ignore') as fin:
            for line in fin:
                line.strip()
                if line.startswith("*MOT") and all(elem not in line for elem in exclude) and all(elem not in line[line.find('MOT')+1:] for elem in alpha):
                    lines.append(line)

# for e in lines:
#     print(e)
f = open("Jiwon_train.txt","w")
g = open("Jiwon_test.txt","w")

eighty = (int)(len(lines)*0.8)

for e in lines[:eighty]:
    f.write(e+"")

for e in lines[eighty:]:
    g.write(e+"")

