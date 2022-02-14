import string

list= []
before = []
after = []
pindex = -1;
def tokenize_syllables():
    with open("/Users/SamuelHu/Desktop/Computational_Linguistics_Research/DataCleaner/Korean/Raw Dataset/Ko/08/2_A0P01M.cha") as data:
        for lines in data:
            if lines.startswith("*MOT"):
                lines = lines.replace("*MOT:\t","")
                for charac in lines:
                    if(charac == ','):
                        lines = lines.replace(', ','|')
                        continue
                    pindex = lines.find('\u0015')
                lines = lines[:pindex-1]
                before.append(lines)
                lines = lines.replace(" ","|")
                lines ='.'.join(i for i in lines)
                lines = lines.replace(".|.","|")
                list.append(lines)

        for a,b in zip(before, list):
            after.append(a+"    "+b)

        for e in after:
            print(e)

def generate_file():
    f = open("Ko_08_2_A0P01M_gold.txt","x")
    for e in after:
        f.write(e+"\n")

if __name__ == "__main__":
    tokenize_syllables()
    
