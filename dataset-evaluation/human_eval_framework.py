from typing import List, Tuple
import pandas as pd
import random

def square(x):
    return x**2


def square_neg(x):
    return -1*((x-1)**2)+1


def validate_inp(inp: str):
    try:
        x = float(inp)
    except ValueError:
        return False
    if x < 0 or x > 10:
        return False
    return x


def mix_corpora(*corpora):
    # pass a list of sentencs pairs to this function
    # return: a mixed sentence pair list and corpus ids to pass to store_scores_to_file
    corpora_with_id = list(zip(corpora, range(1,len(corpora)+1)))
    c_with_sentence_cid = list(map(lambda c: list(map(lambda sp: (sp, c[1]), c[0])), corpora_with_id))
    sps_with_cid = sum(c_with_sentence_cid, [])
    random.shuffle(sps_with_cid)
    sents = list(map(lambda spid: spid[0], sps_with_cid))
    corpus_ids = list(map(lambda spid: spid[1], sps_with_cid))
    return sents, corpus_ids


def corpus_scores(scores: List[float], corp_ids: List[int]):
    corp_scores = []
    for c in sorted(set(corp_ids)):
        cscores = [scores[i] for i in range(len(scores)) if corp_ids[i] == c]
        corp_scores.append(sum(cscores) / len(cscores))
    return corp_scores


def store_scores_to_file(
        sents: List[Tuple[str, str]], 
        scores: List[float], 
        corp_ids: List[int]=None,
        fname: str="eval.txt"):
    if not corp_ids:
        corp_ids = [1]*len(sents)
    corp_scores = corpus_scores(scores, corp_ids)
    with open('results/'+fname, 'w', encoding="utf-8") as f:
        f.write('# Corpus scores\n')
        for i, corp_score in enumerate(corp_scores):
            f.write(f'{i+1}: {corp_score:.3f}\n')
        f.write('# Paraphrase scores\n')
        for i in range(len(sents)):
            f.write(f'{corp_ids[i]}: {scores[i]:.3f} {sents[i][0]} ||| {sents[i][1]}\n')


def eval_cmd(sents: List[Tuple[str, str]], sim_wfunc=None, div_wfunc=None) -> List[float]:
    scores = []
    n = len(sents)
    for i, spair in enumerate(sents):
        s1, s2 = spair
        print(f'Sentence pair {i}/{n}')
        print('1.', s1)
        print('2.', s2)
        sim = False
        while sim is False:
            sim = validate_inp(input('Semantic similarity [0-10]: '))
        div = False
        while div is False:
            div = validate_inp(input('Lexical divergence [0-10]: '))
        sim /= 10
        if sim_wfunc:
            sim = sim_wfunc(sim)
        div /= 10
        if div_wfunc:
            div = div_wfunc(div)
        scores.append(sim*div)
    return scores


if __name__ == '__main__':
    pass
    # NUM_SENTENCES = 15
    # LANGUAGE = input("Choose language (en, sl, cs, de): ")

    # if LANGUAGE == 'sl':
    #     df = pd.read_csv('../data/paraphrases_sl.csv')
    # elif LANGUAGE == 'cs':
    #     df = pd.read_csv('../data/paraphrases_cs.csv')
    # elif LANGUAGE == 'de':
    #     df = pd.read_csv('../data/paraphrases_de.csv')
    # else:
    #     df = pd.read_csv('../data/paraphrases_en.csv')

    # df_list = list(zip(df['Original'].tolist(), df['Parahprase'].tolist()))
    # df_list = list(zip(df.index.tolist(), df_list))

    # indexes = random.sample(range(1, len(df_list)), NUM_SENTENCES)
    # sents = [df_list[index][1] for index in indexes]
    # corp_ids = [df_list[index][0] for index in indexes]

    # scores = eval_cmd(sents, square, square_neg)
    # store_scores_to_file(sents, scores, corp_ids)


    # a = [('s11a', 's12a'), ('s21a', 's22a'), ('s31a','s32a')]
    # b = [('s11b', 's12b'), ('s21b', 's22b'), ('s31b','s32b'), ('s41b', 's42b')]
    # c = [('s11c', 's12c'), ('s21c', 's22c'), ('s31c','s32c'), ('s41c', 's42c')]
    # sents, cids = mix_corpora(a, b, c)
    # print(sents)
    # print(cids)