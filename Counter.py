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
pNameG = "Korean/Korean_train_gold.txt"
pNameU = "Korean/Korean_train_unseg.txt"
with open(os.path.join(my_dir,pNameU)) as data:
    for lines in data:
        total_lines +=1
        num_syll += lines[lines.find('\t')+1:].count('.')+1
        #print(lines[lines.find('\t')+1:])
        sylls_in_line = set([syll.strip() for syll in lines[lines.find('\t')+1:].split(".")])

        # for syll in lines[lines.find('\t')+1:].split("."):
        #     print(syll.strip())
        #     sylls_in_line = set([syll.strip()])
        unique_syll = unique_syll.union(sylls_in_line)
    print(unique_syll)
    #print()

with open(os.path.join(my_dir,pNameG)) as data:
    for lines in data:
        num_words += lines[lines.find('\t')+1:].count('|')+1
        words_in_line = set([word.strip() for word in lines[lines.find('\t')+1:].split("|")])
        unique_words = unique_words.union(words_in_line)
    #print(unique_words)
    

for e in unique_words:
    num_syll_in_words += e.count('.')+1
    list.append(e.count('.')+1)

for num in list:
    total_num_of_syll_in_unique_words += num
#print(len(list), num_syll_in_words)

# for a,b in zip(list, unique_words):
#     if(a == 1):
#         print(b,a)


print("Total lines: ",total_lines,
"\nNum syllables: ",num_syll, 
"\nUnique syllables: ", len(unique_syll)-1, 
"\nNum words: ",num_words,
"\nUnique words: ",len(unique_words)-1,
"\nTotal syllables in unique words: ",total_num_of_syll_in_unique_words, 
"\nMean utterance length in syllable: ",num_syll/total_lines,
"\nMean utterance length in words: ",num_words/total_lines,
"\nMean word length in syllable: ", total_num_of_syll_in_unique_words/len(unique_words))

print(
num_syll, 
len(unique_syll)-1, 
num_words,
len(unique_words)-1,
num_syll/total_lines,
num_words/total_lines,
total_num_of_syll_in_unique_words/len(unique_words))

#Korean dataset contains chinese and japanese characters
