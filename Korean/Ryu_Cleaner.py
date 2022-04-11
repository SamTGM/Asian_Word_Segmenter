import string
import os

my_dir = os.getcwd()

list= []
before = []
after = []
pindex = -1
def tokenize_syllables():
    with open(os.path.join(my_dir,"Ryu/Ryu_train.txt")) as data:
        for lines in data:
            if lines.startswith("*MOT") and lines.find('[/]') == -1:
                lines = lines.replace("*MOT:\t","")
                for charac in lines:
                    if(charac == ','):
                        lines = lines.replace(' , ',' ')
                        continue
                    pindex = lines.find('\u0015')
                lines = lines[:pindex-3]
                before.append(lines)
                lines = lines.replace(" ","|")
                lines ='.'.join(i for i in lines)
                lines = lines.replace(".|.","|")
                list.append(lines)

        for a,b in zip(before, list):
            after.append(a+"\t"+b)

def generate_file():
    f = open("Ryu/Ryu_train_gold.txt","w")
    for e in after:
        f.write(e+"\n")

if __name__ == "__main__":
    tokenize_syllables()
    generate_file()
