import re
import string
list = []
before = []
after = []
pindex = -1;
vowel = ['a','e','i','o','u','A','E','I','O','U']
#lowercase all te capital letters

def tokenize_syllables():
    with open("/Users/SamuelHu/Desktop/Computational_Linguistics_Research/DataCleaner/Japanese/Okayama/Okayama_train.txt") as data:
        for lines in data:
            # if 'wanwan' not in lines:
            #     continue
            if lines.startswith("*MOT:") and lines.find('[/]') == -1 and lines.find('[+') == -1 and lines.find('(') == -1 and lines.find('[:') == -1 and lines.find('[?]') == -1 and lines.find('@') == -1:
                lines = lines.replace("*MOT:\t","")
                lines = lines.replace(' \u2021 ',' ')
                lines = lines.replace('mb','nb')
                lines = lines.replace('mp','np')
                lines = lines.replace('“','')
                lines = lines.replace('”','')
                for charac in lines:
                    lines = lines.replace(' „ ', ' ')
                    if(charac == ','):
                        lines = lines.replace(' , ',' ')
                        continue
                    if(charac in string.punctuation):
                        pindex = lines.find(charac)
                lines = lines[:pindex]
                lines = lines[:lines.find(':')]
                
        
                before.append(lines)

                lines = lines.strip()
                lines = re.sub(r"([aeiouAEIOU])",r"\1.",lines).replace(" ","|")
                if len(lines)>0 and lines[-1] == '.':
                    lines = lines[:-1]
                lines = lines.replace(".|","|")

                c1index = 0
                for c1, c2 in zip(lines, lines[2:]):
                    if c1 == c2 and (c1 in vowel or c2 in vowel) and c1index != len(lines)-1:
                        #print('executed')
                        lines = lines.replace(c1+'.'+c2, c1+c2)     

                index = 0
                # print(index, lines[index], lines)
                while index<len(lines):
                    n = lines[index]
                    # print(index, len(lines))
                    if(n == 'n' and index!=0 and lines[index-1]=='.'):
                        if index < len(lines)-1 and lines[index+1]=='|':
                            lines = lines[:index-1]+lines[index:]
                            index -=1
                            #print("found1")
                            continue
                        elif index == len(lines)-1:
                            lines = lines[:index-1]+lines[index:]
                            #print("found2")
                            continue
                        elif (lines[index+1] not in vowel):
                            #print(lines[index]+ lines[index+1])
                            lines = lines[:index-1]+lines[index]+'.'+lines[index+1:]
                            #print("found3")
                            continue
                    # print(index,n, lines[index-1:index+2], lines)
                    # print(lines[-1])
                    index +=1
                 
                list.append(lines)
                #print("something")
                
                

        for a,b in zip(before, list):
            after.append(a+"\t"+b)

        # for e in after:
        #     print(e)
    #print(list)
        

def generate_file():
    f = open("Okayama/Okayama_train_gold.txt","w")
    for e in after:
        f.write(e+"\n")

if __name__ == "__main__":
    tokenize_syllables()
    generate_file();

#Satchan tabesashite ageru kara hayaku tabenasai	Sa.tchan|ta.be.sa.shi.te|a.ge.ru|ka.ra|ha.ya.ku|ta.be.na.sa.i
#dakara Okaasan itta desho tabete wa ikemasen to	da.ka.ra|O.kaa.san|i.tta|de.sho|ta.be.te|wa|i.ke.ma.se.n|to
#wanwan ga oru naa	wan.wa.n|ga|o.ru|naa
#Oneechan konna kiree no motte haru no	O.nee.chan|ko.nna|ki.ree|no|mo.tte|ha.ru|no
#Fukuchan Obaachan ni moota no to Oneechan ni itta no	Fu.ku.chan|O.baa.cha.n|ni|moo.ta|no|to|O.nee.cha.n|ni|i.tta|no
