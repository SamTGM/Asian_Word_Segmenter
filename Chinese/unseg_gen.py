after = []

def tokenize_syllables():
    with open("/Users/SamuelHu/Desktop/Computational_Linguistics_Research/DataCleaner/Chinese/Erbaugh_Kang_02_gold.txt") as data:
        for lines in data:
            lines = lines.replace('|','.')
            lines = lines.replace('\n','')
            after.append(lines)

def generate_file():
    f = open("Erbaugh_Kang_02_unseg.txt","w")
    for e in after:
        f.write(e+"\n")

if __name__ == "__main__":
    tokenize_syllables()
    generate_file()
