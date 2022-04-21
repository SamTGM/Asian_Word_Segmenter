import os


unique_syll = set()
unique_words = set()
total_lines = 0
num_syll = 0
num_words = 0
num_syll_in_words = 0
list = []
total_num_of_syll_in_unique_words = 0

my_dir = os.getcwd()
pNameG = "Japanese/Okayama/Okayama_train_gold.txt"
pNameU = "Japanese/Okayama/Okayama_train_unseg.txt"
with open(os.path.join(my_dir,pNameU)) as data:
    for lines in data:
        total_lines +=1
        num_syll += lines[lines.find('\t'):].count('.')+1
        sylls_in_line = set([syll.strip() for syll in lines[lines.find('\t'):].split(".")])
        unique_syll = unique_syll.union(sylls_in_line)
    #print(unique_syll)


with open(os.path.join(my_dir,pNameG)) as data:
    for lines in data:
        num_words += lines[lines.find('\t'):].count('|')+1
        words_in_line = set([word.strip() for word in lines[lines.find('\t'):].split("|")])
        unique_words = unique_words.union(words_in_line)
    #print(unique_words)

for e in unique_words:
    num_syll_in_words += e.count('.')+1
    list.append(e.count('.')+1)

for num in list:
    total_num_of_syll_in_unique_words += num
#print(len(list), num_syll_in_words)

for a,b in zip(list, unique_words):
    if(a == 1):
        print(b,a)


# print("Total lines: ",total_lines,"\nUnique syllables: ", len(unique_syll), "\nNum syllables: ",num_syll, "\nUnique words: ",len(unique_words), "\nNum words: ",num_words,"\n",)