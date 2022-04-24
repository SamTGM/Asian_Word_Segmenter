import transprob
import data
import subtractive

def test_get_bestmatch():
    lexicon = {"B AA1 . T AA0":10, "B AA1 . K IY0":5, "B AA1" :5}
    print(subtractive.get_bestmatch({"B AA1 . T AA0", "B AA1"},lexicon))
    print(subtractive.get_bestmatch({"B AA1 . K IY0", "B AA1"},lexicon))
    print(subtractive.get_bestmatch({"yes", "B"},lexicon))

def test_update_lexicon():
    lexicon = {}
    subtractive.update_lexicon(lexicon, "B AA1 . K IY0")
    subtractive.update_lexicon(lexicon, "B AA1 . K IY0")
    subtractive.update_lexicon(lexicon, "B AA1 . K IY0")
    print(lexicon)
    subtractive.update_lexicon(lexicon, "B AA1")
    print(lexicon)


def test_subtract():
    print(subtractive.subtract("B AA1", "B AA1 . T AA0"))
    print(subtractive.subtract("B AA1 . T AA0", "B AA1 . T AA0"))
    print(subtractive.subtract("B AA1 . T AA0", "B AA1 . T AA0 . B AA1 T AA0"))
    print(subtractive.subtract("B AA1 . T AA0", "B AA1 . T AA0 . M AA1 T AA0"))
    print(subtractive.subtract("", "B AA1 . T AA0"))

def test_sub_get_segpoints():
    lexicon = {"B AA1 . T AA0":10, "B AA1 . K IY0":5, "F AA1" :5}
    print(subtractive.get_segpoints(lexicon, ["B AA1 . T AA0 . F AA1 . F AA1", "B AA1 . K IY0"]))

def test_get_tp_sequence():
    train_utts = data.read_file("Brown_train_unseg.txt")
    probdict = transprob.get_bigramprobdict(train_utts)
    tokenized = data.tokenize_syllables(train_utts[59])
    print(tokenized)
    print(transprob.get_tp_sequence(tokenized, probdict))
    

def test_get_local_minima():
    train_utts = data.read_file("Brown_train_unseg.txt")
    probdict = transprob.get_bigramprobdict(train_utts)
    tokenized = data.tokenize_syllables(train_utts[500])
    print(tokenized)
    transprob.get_tp_sequence(tokenized, probdict)
    print(transprob.get_local_minima(transprob.get_tp_sequence(tokenized, probdict)))
    tokenized = data.tokenize_syllables(train_utts[0])
    print(tokenized)
    transprob.get_tp_sequence(tokenized, probdict)
    print(transprob.get_local_minima(transprob.get_tp_sequence(tokenized, probdict)))

def test_get_segpoints():
    train_utts = data.read_file("Brown_train_unseg.txt")
    probdict = transprob.get_bigramprobdict(train_utts)
    tokenizeds = [data.tokenize_syllables(utt) for utt in train_utts[800:810]] 
    print(transprob.get_segpoints(tokenizeds, probdict))


if __name__ == "__main__":
    #test_get_local_minima()
    #test_get_tp_sequence()
    #test_get_segpoints()

    #test_sub_get_segpoints()
    #test_subtract()
    #test_update_lexicon()
    test_get_bestmatch()
