import data

def baseline_segs(tokenizeds):
    """Treats each syllable boundary as a segmentation point for each tokenized utterance
    input:
        tokenizeds (list of lists): A list of utterances. Each is a list of syllables
    return:
        (list of sets): a list of segmentation point sets, one for each input utterance
    """
    # Instructor solved this in 4 lines including the return
    list = []
    for tokens in tokenizeds:
        list.append(set([token for token in range(len(tokens)-1)]))
    return list

def main():
    train_utts = data.read_file("Brown_train_unseg.txt")
    train_tokenized = [data.tokenize_syllables(utt) for utt in train_utts]
    baselinesegs_train = baseline_segs(train_tokenized)
 
    test_utts = data.read_file("Brown_test_unseg.txt")
    test_tokenized = [data.tokenize_syllables(utt) for utt in test_utts]
    baselinesegs_test = baseline_segs(test_tokenized)

    goldsegs_train = data.get_goldsegs("Brown_train_gold.txt")
    goldsegs_test = data.get_goldsegs("Brown_test_gold.txt")

    for basesegs, goldsegs, title in ((baselinesegs_train, goldsegs_train, "Training"), (baselinesegs_test, goldsegs_test, "Testing")):
        stats = data.evaluate(goldsegs, basesegs)
        print(title)
        print("P: %s\tR: %s\t\tF1: %s\n" % tuple([round(stat*100, 2) for stat in stats]))
    

if __name__ == "__main__":
    main() 


