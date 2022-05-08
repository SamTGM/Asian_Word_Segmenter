import numbers
from operator import indexOf
import string
import re
import os

my_dir = os.getcwd()

list= []
before = []
after = []
exclude = '''-{};()[]<>„'"\/@#$^&_~+‡'''


def tokenize_syllables():
    infname = os.path.join(my_dir,"Erbaugh/Erbaugh_train.txt")
    with open(infname, "r") as fin:
        for line in fin:
            if "%mor:" in line and "&DIM" not in line and all(elem not in line for elem in exclude):
                line = line.replace("%mor:\t","")
                words = line.split()
                cleanedline = []
                cleanedline1 = []
                for word in words:
                    therest = word.split("|")[-1]
                    wordform = therest.split("=")[0]
                    basewordform = wordform.split("-")[0]
                    if "1" not in basewordform and "2" not in basewordform and "3" not in basewordform and "4" not in basewordform :
                        if word not in {"poss|de", "sfp|ma", "asp|le", "cleft|de"}:
                            #print(basewordform)
                            continue
                    cleanedline.append(basewordform)
                    basewordform = re.sub(r"([01234])",r"\1.",basewordform).replace(" ",".")
                    if basewordform[-1] == '.':
                        basewordform = basewordform[:-1]
                    basewordform = basewordform.replace(".|","|")
                    cleanedline1.append(basewordform)

                before.append(" ".join(cleanedline))

                list.append("|".join(cleanedline1))

           

        for a,b in zip(before, list):
            after.append(a+"\t"+b)

        # for e in after:
        #     print(e)

def generate_file():
    f = open("Erbaugh/Erbaugh_train_gold.txt","w")
    for e in after:
        f.write(e+"\n")

if __name__ == "__main__":
    tokenize_syllables()
    generate_file()
