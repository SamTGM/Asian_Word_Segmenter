from cmath import pi
import numbers
from operator import indexOf
import string
import re

list= []
before = []
after = []


def tokenize_syllables():
    with open("/Users/SamuelHu/Desktop/Computational_Linguistics_Research/DataCleaner/Chinese/Erbaugh/Kang/02.cha") as data:
        for lines in data:
            if lines.startswith("%mor") and lines.find('[/]') == -1 and lines.find('&DIM') == -1:
                lines = lines.replace("%mor:\t","")
                lines = lines.replace(' \u2021 ',' ')
                pindex = 0
                for charac in lines:
                    strings = ''
                    if charac.isdigit():
                        strings = strings + lines[lines.find('|',pindex)+1:lines.find('=',pindex+1)]
                        pindex = lines.find('=')
                        
                    if strings != '':
                        before.append(strings)
                    # list = lines.split()
                    # for word in list:
                    #     for cha in word:
                    #         if cha.isdigit():
                    #             after.append(word)
        print(before)
        #         for charac in lines:
        #             if(charac == ',' or charac == '„'):
        #                 lines = lines.replace(' , ',' ')
        #                 lines = lines.replace(' „ ', ' ')
        #                 continue
        #             pindex = lines.find('\u0015')
        #         lines = lines[:pindex-3]
        #         before.append(lines)
        #         lines = lines.replace(" ","|")
        #         lines ='.'.join(i for i in lines)
        #         lines = lines.replace(".|.","|")
        #         list.append(lines)

        # for a,b in zip(before, list):
        #     after.append(a+"\t"+b)

def generate_file():
    f = open("Erbaugh_Kang_02_gold.txt","x")
    for e in after:
        f.write(e+"\n")

if __name__ == "__main__":
    tokenize_syllables()
    #generate_file()
