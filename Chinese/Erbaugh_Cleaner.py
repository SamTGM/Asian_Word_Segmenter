from cmath import pi
from distutils.command.clean import clean
import numbers
from operator import indexOf
import string
import re

list= []
before = []
after = []


def tokenize_syllables():
    infname = "/Users/SamuelHu/Desktop/Computational_Linguistics_Research/DataCleaner/Chinese/Erbaugh/Kang/02.cha"
    with open(infname, "r") as fin:
        in_MOT = False
        for line in fin:
    #        print(line.strip())
            if "*MOT:" in line:
                in_MOT = True
            elif in_MOT and "%mor:" in line and "&DIM" not in line:
                line = line.replace("%mor:\t","")
                words = line.split()
                cleanedline = []
                cleanedline1 = []
                for word in words:
                    therest = word.split("|")[-1]
                    wordform = therest.split("=")[0]
                    basewordform = wordform.split("-")[0]
                    if "1" not in basewordform and "2" not in basewordform and "3" not in basewordform and "4" not in basewordform:
                        if word not in {"poss|de", "sfp|ma", "asp|le", "cleft|de"}:
                            #print(basewordform)
                            continue
                    cleanedline.append(basewordform)
                    basewordform = re.sub(r"([1234])",r"\1.",basewordform).replace(" ",".")
                    if basewordform[-1] == '.':
                        basewordform = basewordform[:-1]
                    basewordform = basewordform.replace(".|","|")
                    cleanedline1.append(basewordform)

                before.append(" ".join(cleanedline))

                in_MOT = False

                list.append("|".join(cleanedline1))

            else:
                in_MOT = False

        for a,b in zip(before, list):
            after.append(a+"\t\t"+b)

        # for e in after:
        #     print(e)

def generate_file():
    f = open("Erbaugh_Kang_02_gold.txt","x")
    for e in after:
        f.write(e+"\n")

if __name__ == "__main__":
    tokenize_syllables()
    generate_file()
