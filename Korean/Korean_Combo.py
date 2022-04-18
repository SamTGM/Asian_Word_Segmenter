from fileinput import filename
import os
trainG = []
my_dir = os.getcwd()
with open(os.path.join(os.getcwd(),'Jiwon/Jiwon_train_gold.txt'), "r", encoding='utf-8', errors='ignore') as fin:
    for line in fin:
        if line.strip():
            trainG.append(line)

with open(os.path.join(os.getcwd(),'Ryu/Ryu_train_gold.txt'), "r", encoding='utf-8', errors='ignore') as fin:
    for line in fin:
        if line.strip():
            trainG.append(line)

with open(os.path.join(os.getcwd(),'Ko/Ko_train_gold.txt'), "r", encoding='utf-8', errors='ignore') as fin:
    for line in fin:
        if line.strip():
            trainG.append(line)

# for e in lines:
#     print(e)

f = open("Korean_train_gold.txt","w")
for e in trainG:
    f.write(e)



trainU = []
with open(os.path.join(os.getcwd(),'Jiwon/Jiwon_train_unseg.txt'), "r", encoding='utf-8', errors='ignore') as fin:
    for line in fin:
        if line.strip():
            trainU.append(line)

with open(os.path.join(os.getcwd(),'Ryu/Ryu_train_unseg.txt'), "r", encoding='utf-8', errors='ignore') as fin:
    for line in fin:
        if line.strip():
            trainU.append(line)

with open(os.path.join(os.getcwd(),'Ko/Ko_train_unseg.txt'), "r", encoding='utf-8', errors='ignore') as fin:
    for line in fin:
        if line.strip():
            trainU.append(line)

f = open("Korean_train_unseg.txt","w")
for e in trainU:
    f.write(e)



testG = []
with open(os.path.join(os.getcwd(),'Jiwon/Jiwon_test_gold.txt'), "r", encoding='utf-8', errors='ignore') as fin:
    for line in fin:
        if line.strip():
            testG.append(line)

with open(os.path.join(os.getcwd(),'Ryu/Ryu_test_gold.txt'), "r", encoding='utf-8', errors='ignore') as fin:
    for line in fin:
        if line.strip():
            testG.append(line)

with open(os.path.join(os.getcwd(),'Ko/Ko_test_gold.txt'), "r", encoding='utf-8', errors='ignore') as fin:
    for line in fin:
        if line.strip():
            testG.append(line)

# for e in lines:
#     print(e)

f = open("Korean_test_gold.txt","w")
for e in testG:
    f.write(e)



testU = []
with open(os.path.join(os.getcwd(),'Jiwon/Jiwon_test_unseg.txt'), "r", encoding='utf-8', errors='ignore') as fin:
    for line in fin:
        if line.strip():
            testU.append(line)

with open(os.path.join(os.getcwd(),'Ryu/Ryu_test_unseg.txt'), "r", encoding='utf-8', errors='ignore') as fin:
    for line in fin:
        if line.strip():
            testU.append(line)

with open(os.path.join(os.getcwd(),'Ko/Ko_test_unseg.txt'), "r", encoding='utf-8', errors='ignore') as fin:
    for line in fin:
        if line.strip():
            testU.append(line)

f = open("Korean_test_unseg.txt","w")
for e in testU:
    f.write(e)

