import re

syll_rx = re.compile(r"[\.\|]")

def tokenize_syllables(utterance):
    """Tokenizes syllables in the input"""
    return [syll.strip() for syll in syll_rx.split(utterance)]

def get_boundary_indices(utterance):
    """Gets the boundary indices from gold data"""
    boundaries = "".join([c for c in utterance if c in {".","|"}])
    return set([i.start() for i in re.finditer("\|", boundaries)])

def read_file(fname):
    """Reads a data file and returns the syllabified utterances"""
    with open(fname, "r") as fin:
        return [line.strip().split("\t")[1] for line in fin if line.strip()]

def get_goldsegs(goldfname):
    """Returns segmentation points for each utterance in a gold file.
    The segmentation points for each utterance are a list of ints"""
    train_utts = read_file(goldfname)
    return [get_boundary_indices(utt) for utt in train_utts]

def apply_boundaries(tokenized, segpoints):
    """Takes a tokenized utterance and segmentation points
    reconstitutes a string in the same format as the gold data
    with . for syll boundaries and | for word boundaries"""
    reconstituted = []
    for i, syll in enumerate(tokenized):
        reconstituted.append(syll)
        if i in segpoints:
            reconstituted.append("|")
        else:
            reconstituted.append(".")
    return " ".join(reconstituted[:-1]) 



###
### YOUR FUNCTIONS
###


def get_precision(allgoldsegs, allpredsegs):
    """Given parallel lists of gold segmentation sets and predicted
    segmentation sets, this computes precision
    input:
        allgoldsegs (list of sets): list of gold seg points, one set per utterance
        allgoldsegs (list of sets): list of predicted seg points, one set per utterance
    return:
        (float): Precision calculated as the TP/(TP+FP) of the entire corpus
                 returns 0 if the denominator is 0"""    
    # Instructor solved this in 6 lines including the return
    TP=0 
    FP=0
    for g,p in zip(allgoldsegs,allpredsegs): 
        TP += len(p.intersection(g)) 
        FP += len(p.difference(g)) 
    return 0 if TP+FP == 0 else TP/(TP+FP)
    

def get_recall(allgoldsegs, allpredsegs):
    """Given parallel lists of gold segmentation sets and predicted
    segmentation sets, this computes recall
    input:
        allgoldsegs (list of sets): list of gold seg points, one set per utterance
        allgoldsegs (list of sets): list of predicted seg points, one set per utterance
    return:
        (float): Recall calculated as the TP/(TP+FN) of the entire corpus
                 returns 0 if the denominator is 0"""    
    # Instructor solved this in 6 lines including the return
    TP=0
    FN=0
    for g,p in zip(allgoldsegs,allpredsegs): 
        TP += len(p.intersection(g)) 
        FN += len(g.difference(p)) 
    return 0 if TP+FN == 0 else TP/(TP+FN)

def get_f1score(P, R):
    """Computes f1 score given a precision and recall
    input:
        P (float): precision
        R (float): recall
    returns:
        (float): F1 score. Returns 0 if precision and recall are both 0"""
    # Instructor solved this in 1 line including the return
    return (2*P*R)/(P+R)


def evaluate(allgoldsegs, allpredsegs):
    """Computes precision, recall, and f1 from lists of segmentation sets
    input:
        allgoldsegs (list of sets): list of gold seg points, one set per utterance
        allgoldsegs (list of sets): list of predicted seg points, one set per utterance
    return:
        (float): Precision
        (float): Recall
        (float): F1-Score
    """
    # Instructor solved this in 4 lines including the return
    P = get_precision(allgoldsegs,allpredsegs)
    R = get_recall(allgoldsegs,allpredsegs)
    F = get_f1score(P,R)
    return (P,R,F)


