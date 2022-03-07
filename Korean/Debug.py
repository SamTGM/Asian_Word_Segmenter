with open("/Users/SamuelHu/Desktop/Computational_Linguistics_Research/DataCleaner/Korean/Jiwon_020020_unseg.txt") as data:
    for line in data:
        print(line.strip())
        print(line.split('\t'))
        line.split('\t')[1]