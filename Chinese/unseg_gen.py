import os
my_dir = os.getcwd()

train_list = []
test_list = []
def tokenize_syllables():
    with open(os.path.join(my_dir,"Tsay/Tsay_train_gold.txt")) as train:
        for lines in train:
            lines = lines.replace('|','.')
            lines = lines.replace('\n','')
            train_list.append(lines)
    
    with open(os.path.join(my_dir,"Tsay/Tsay_test_gold.txt")) as test:
        for lines in test:
            lines = lines.replace('|','.')
            lines = lines.replace('\n','')
            test_list.append(lines)


def generate_train_file():
    f = open("Tsay/Tsay_train_unseg.txt","w")
    for e in train_list:
        f.write(e+"\n")


def generate_test_file():
    g = open("Tsay/Tsay_test_unseg.txt","w")
    for e in test_list:
        g.write(e+"\n")

if __name__ == "__main__":
    tokenize_syllables()
    generate_train_file()
    generate_test_file()
