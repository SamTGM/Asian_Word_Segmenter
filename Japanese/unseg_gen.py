after = []
def tokenize_syllables():
    with open("/Users/SamuelHu/Desktop/Computational_Linguistics_Research/DataCleaner/Japanese/Okayama_gold.txt") as data:
        for lines in data:
            lines = lines.replace('|','.')
            lines = lines.replace('\n','')
            after.append(lines)

def generate_file():
    f = open("Okayama_unseg.txt","x")
    for e in after:
        f.write(e+"\n")

if __name__ == "__main__":
    tokenize_syllables()
    generate_file()
