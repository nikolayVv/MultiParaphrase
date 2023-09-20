import human_eval_framework as hef
import datasets
import random
import sys

uname = "noname"
if len(sys.argv) == 2:
    uname = sys.argv[1]

N_TATOEBA = 20

tatoeba_enen = datasets.load_dataset("Helsinki-NLP/tatoeba_mt", language_pair="eng-eng", split='validation')
sample_ids = random.sample(range(tatoeba_enen.num_rows), N_TATOEBA)
tatoeba_enen_samples = tatoeba_enen.select(sample_ids)

N_PC = 20

model_enen = datasets.load_dataset("csv", data_files="../data/eval_table_multi_enen.csv", split='train')
sample_ids = random.sample(range(model_enen.num_rows), N_PC)
model_enen_samples = model_enen.select(sample_ids)

def tatoeba_to_sentencepairs(item):
    return (item['sourceString'], item['targetString'])

def pc_to_sententepairs(item):
    return (item['Original'], item['Paraphrase'])

tatoeba_sents = list(map(tatoeba_to_sentencepairs, tatoeba_enen_samples.to_list()))
pc_sents = list(map(pc_to_sententepairs, model_enen_samples.to_list()))

sents, corpus_ids = hef.mix_corpora(tatoeba_sents, pc_sents)
scores = hef.eval_cmd(sents, hef.square, hef.square_neg)
hef.store_scores_to_file(sents, scores, corpus_ids, "human_eval_tatoeba-enen_multi_model-enen_"+uname+".txt")