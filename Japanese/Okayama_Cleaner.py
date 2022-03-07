import string
list = []
before = []
after = []
pindex = -1;
vowel = ['a','e','i','o','u','A','E','I','O','U']
def tokenize_syllables():
    with open("/Users/SamuelHu/Desktop/Computational_Linguistics_Research/DataCleaner/Japanese/Raw Dataset/Okayama/001-2.2-M.cha") as data:
        for lines in data:
            if lines.startswith("*MOT:") and lines.find('[/]') == -1:
                lines = lines.replace("*MOT:\t","")
                lines = lines.replace(' \u2021 ',' ')
                for charac in lines:
                    if(charac == ','):
                        lines = lines.replace(' , ',' ')
                        continue
                    if(charac in string.punctuation):
                        pindex = lines.index(charac)
                lines = lines[:pindex-1]
                for c1, c2 in zip(lines, lines[1:]):
                    if c1 == c2:
                        lines = lines.replace(c1+c2,c1.capitalize())
                before.append(lines)
                lines = lines.strip()
                # for cha in lines:
                #     if cha in vowel:
                #         lines = lines.replace(cha,cha+'.')
                lines = lines.replace(" ","|")
                lines = lines.replace(".|.","|")
                list.append(lines)

        for a,b in zip(before, list):
            after.append(a+"\t"+b)

        for e in after:
            print(e)
        

def generate_file():
    f = open("Jiwon_020020_gold.txt","w")
    for e in after:
        f.write(e+"\n")

if __name__ == "__main__":
    tokenize_syllables()
    #generate_file();

