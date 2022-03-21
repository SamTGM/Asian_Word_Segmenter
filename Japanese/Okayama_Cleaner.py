import re
import string
list = []
before = []
after = []
pindex = -1;
vowel = ['a','e','i','o','u','A','E','I','O','U']
def tokenize_syllables():
    with open("/Users/SamuelHu/Desktop/Computational_Linguistics_Research/DataCleaner/Japanese/Raw Dataset/Okayama/001-2.2-M.cha") as data:
        for lines in data:
            if lines.startswith("*MOT:") and lines.find('[/]') == -1 and lines.find('[+') == -1 and lines.find('(') == -1 and lines.find('[:') == -1:
                lines = lines.replace("*MOT:\t","")
                lines = lines.replace(' \u2021 ',' ')
                for charac in lines:
                    lines = lines.replace(' „ ', ' ')
                    if(charac == ','):
                        lines = lines.replace(' , ',' ')
                        continue
                    if(charac in string.punctuation):
                        pindex = lines.find(charac)
                lines = lines[:pindex]
                lines = lines[:lines.find(':')]
                for c1, c2 in zip(lines, lines[1:]):
                    if c1 == c2:
                        lines = lines.replace(c1+c2,c1.capitalize())
        
                before.append(lines)

                lines = lines.strip()
                lines = re.sub(r"([aeiouAEIOU])",r"\1.",lines).replace(" ","|")
                if lines[-1] == '.':
                    lines = lines[:-1]
                lines = lines.replace(".|","|")
                index = 0
                for e in lines:
                    if(e == 'n' and index!=0 and lines[index-1]=='.'):
                        if( (lines[index] == lines[-1] or (lines[index] != lines[-1] and lines[index+1]=='|'))):
                            lines = lines[:index-1]+lines[index:]
                        elif (lines[index+1] not in vowel):
                            #print(lines[index]+ lines[index+1])
                            lines = lines[:index-1]+lines[index]+'.'+lines[index+1:]
                   # print(lines[-1])
                    index +=1
                
                # nindex = 0
                # for e in lines:
                #     if(e in vowel and lines[nindex] != lines[-2] and lines[nindex] != lines[-1]):
                #         if(lines[nindex+1] == '.' and lines[nindex+2] in vowel):
                #             lines = lines[:nindex]+lines[nindex+2:]
                #     nindex +=1

                
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
