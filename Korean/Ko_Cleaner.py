import string

list= []
before = []
after = []
pindex = -1
exclude = ['ads','@','[/]','(','x','<','[','=']
alpha = string.ascii_lowercase + string.ascii_uppercase
punc = '''!-{};:'"\./?@#$?%^&_~�'''
def tokenize_syllables():
    with open("/Users/SamuelHu/Desktop/Computational_Linguistics_Research/DataCleaner/Korean/Ko/Ko_train.txt") as data:
        for lines in data:
            if lines.startswith("*MOT") and all(elem not in lines for elem in exclude) and alpha not in lines:
                lines = lines.replace("*MOT:\t","")
                for charac in lines:
                    if(charac == ','):
                        lines = lines.replace(', ','|')
                        continue
                    if charac in punc:
                        lines = lines.replace(charac,"")
                    pindex = lines.find('\u0015')
                lines = lines[:pindex-1]
                if string.punctuation in lines:
                    print(lines.find(string.punctuation))
                    lines = lines[:lines.find(string.punctuation)]
                before.append(lines)
                lines = lines.replace(" ","|")
                lines ='.'.join(i for i in lines)
                lines = lines.replace(".|.","|")
                list.append(lines)

        for a,b in zip(before, list):
            after.append(a+"\t"+b)

        # for e in after:
        #     print(e)

def generate_file():
    f = open("Ko/Ko_train_gold.txt","w")
    for e in after:
        f.write(e+"\n")

if __name__ == "__main__":
    tokenize_syllables()
    generate_file()
    
