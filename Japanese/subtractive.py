import data
import re

def build_lexicon(utts):
    """The core lexicon-building algorithm. Returns a dictionary of words with their scores"""
    lexicon = {}
    for utt in utts:
        # Subtraction loop
        remainder = utt
        while remainder:
            # Get all the possible subtractions
            matchedwords = set()
            syllindices = [i for i, syllseg in enumerate(remainder) if syllseg == "."]
            for i in syllindices:
                candidate = remainder[:i].strip()
                if candidate in lexicon:
                    matchedwords.add(candidate)
            # Do subtraction and lexicon updating
            if matchedwords: # If at least one subtraction is found
                # Get the best one
                beststartword = get_bestmatch(matchedwords, lexicon)
                # Do the subtraction
                remainder = subtract(beststartword, remainder)
                # Update the subtracted word in the lexicon
                update_lexicon(lexicon, beststartword)
            else: # No subtraction was found
                # Update the lexicon with the remained and move to the next word
                update_lexicon(lexicon, remainder)
                break
    return lexicon


def get_utt_segpoints(lexicon, utt):
    """Actually segments an utterance given the lexicon. 
    Returns the segmented utterance and a set of segmentation points"""
    remainder = utt
    wordseq = []
    # Loop to subtract utterance-initial words
    while remainder:
        syllindices = [i for i, syllseg in enumerate(remainder) if syllseg == "."]
        found = False
        for i in syllindices:
            candidate = remainder[:i].strip()
            # Subtract the shortest possible word
            if candidate in lexicon:
                # Do the subtraction
                remainder = subtract(candidate, remainder)
                # Add
                wordseq.append(candidate)
                found = True
                break
        # Give up when nothing left can be subtracted
        if not found:
            wordseq.append(remainder)
            break
    # Reconstitute the utterance with word boundaries
    joined = " | ".join(wordseq)
    return joined, data.get_boundary_indices(joined)


###
### YOUR FUNCTIONS
###


def get_bestmatch(matchedwords, lexicon):
    """Given a set of words that matched the start of the utterance,
    returns the one with the highest score
    input:
        matchedwords (set): a set of words from the lexicon
        lexicon (dict str:int): a dictionary of words and scores
    return:
        (str): return the word from matchedwords with the best score in the lexicon.
               If two words are tied for best score, return the one with the fewest syllables"""
    # Instructor solved this in 16 lines including the return

    max = ""
    first = list(matchedwords)[0]
    for words in matchedwords:
        if words in lexicon.keys():
            if lexicon.get(words)>lexicon.get(first):
                max = words
            elif lexicon.get(words)==lexicon.get(first):
                max = words if words.count('.')<max.count('.') else first
    return max



def update_lexicon(lexicon, word):
    """Updates the lexicon with a word. Add it with score=1 if it's new, increment score if not new
    input:
        lexicon (dict str:int): dictionary of words and scores
        word (str): word to update lexicon with
    return:
       (none): lexicon is updated by reference"""
    # Instructor solved this in 3 lines including the return
    lexicon.update({word:lexicon.get(word)+1}) if word in lexicon.keys() else lexicon.update({word:1})
    return 


def subtract(beststartword, utt):
    """Removes word from beginning of utterance. Returns the remainder. Remember to remove any extra periods or whitespace from the ends
    input:
        beststartword (str): word to remove from start of utt
        utt (str): utterance to remove beginning of
    return:
        (str): utterance with beststartword removed from the beginning. Remove any extra period or space from the ends"""
    # Instructor solved this in 3 lines including the return
    new = re.sub("^"+beststartword+" . ", "",utt) if beststartword != utt else re.sub("^"+beststartword, "",utt)
    return new


def get_segpoints(lexicon, utts):
    """Segments each utterance using the lexicon. Returns a segmented copy of each utterance and a set of segmentation points for each utterance
    input:
        lexicon (dict str:int): dictionary of words and scores
        utts (list of str): list of utterances
    return:
        (list of str): list of segmented utterances (. replaced with | on word boundaries)
        (list of set): list of sets of segmentation point indices"""
    # Instructor solved this in 7 lines including the return
    ulist = []
    slist = []
    for utt in utts:
        ulist.append(get_utt_segpoints(lexicon, utt)[0])
        slist.append(get_utt_segpoints(lexicon, utt)[1])
    return ulist, slist


def build_lexicon_usc(utts):
    """See Extra Credit in Writeup"""
    return 


def build_lexicon_recursive(utts):
    """See Extra Credit in Writeup"""
    return 


def main():
    train_utts = data.read_file("Okayama/Okayama_train_unseg.txt")
    lexicon = build_lexicon(train_utts[:])

    test_utts = data.read_file("Okayama/Okayama_test_unseg.txt")
    goldsegs_train = data.get_goldsegs("Okayama/Okayama_train_gold.txt")
    goldsegs_test = data.get_goldsegs("Okayama/Okayama_test_gold.txt")

    for utts, goldsegs, title in ((train_utts, goldsegs_train, "Training"), (test_utts, goldsegs_test, "Testing")):
        joineds, segs = get_segpoints(lexicon, utts)
        stats = data.evaluate(goldsegs, segs)
        print(title)
        print("P: %s\tR: %s\t\tF1: %s\n" % tuple([round(stat*100, 2) for stat in stats]))


if __name__ == "__main__":
    main()


