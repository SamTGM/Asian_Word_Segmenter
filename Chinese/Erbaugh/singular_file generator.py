from fileinput import filename
import os
lines = []
my_dir = os.getcwd()
for subdir, dirs, files in os.walk(my_dir):
    print(subdir,files)
    for fname in files:
        with open(os.path.join(subdir,fname), "r", encoding='utf-8', errors='ignore') as fin:
            for line in fin:
                line.strip()
                in_MOT = False
                for line in fin:
                    if "*MOT:" in line:
                        in_MOT = True
                    elif in_MOT and "%mor:" in line and "&DIM" not in line:
                        lines.append(line)
                        in_MOT = False
                    else:
                        in_MOT = False

# for e in lines:
#     print(e)
f = open("Erbaugh_train.txt","w")
g = open("Erbaugh_test.txt","w")

eighty = (int)(len(lines)*0.8)
for e in lines[:eighty]:
    f.write(e+"")

for e in lines[eighty:]:
    g.write(e+"")

