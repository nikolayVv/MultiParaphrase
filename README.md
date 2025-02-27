# Multillingual paraphrasing of sentences

This project explores monolingual and multilingual paraphrasing across English, German, Czech, and Slovene, evaluating whether multilingual training improves paraphrase generation. Due to the lack of paraphrase datasets for low-resource languages, we generated monolingual datasets via back-translation and trained mT5 models both monolingually and multilingually.

Our results show that monolingual models performed best in their respective languages (Parascore: 0.89–0.96), while multilingual models balanced performance across languages—improving Slovene but slightly reducing English accuracy. Human evaluation confirmed that our datasets offer better lexical diversity than Tatoeba but include more noise.

## Data

The repository doesn't collect any new dataset. Instead, we have decided to leverage the already existing ones.
We use the [ParaCrawl](https://opus.nlpl.eu/ParaCrawl.php) dataset which consists of lots of sentences in different languages. We use maching translation models from [huggingface](https://huggingface.co/) to create paraphrase data from this translation dataset. While other multilingual parallel datasets include sentence pairs within a language (i.e. paraphrases), they include only few if any of these paraphrase sentence pairs in medium resource languages like Slovene. With our approach we create similarly sized paraphrase datasets for different languages including medium resource languages by leveraging translation data, which is more widely available than paraphrase data.

Our generated data can be accessed on huggingface:
- [ParaCrawl-enen](https://huggingface.co/datasets/yawnick/para_crawl_enen)
- [ParaCrawl-dede](https://huggingface.co/datasets/yawnick/para_crawl_dede)
- [ParaCrawl-slsl](https://huggingface.co/datasets/yawnick/para_crawl_slsl)
- [ParaCrawl-cscs](https://huggingface.co/datasets/yawnick/para_crawl_cscs)
- [ParaCrawl-multi_all](https://huggingface.co/datasets/yawnick/para_crawl_multi_all)
- [ParaCrawl-multi_small](https://huggingface.co/datasets/yawnick/para_crawl_multi_small)

### Dataset Evaluation

We evaluate the quality of our monolingual datasets via human evaluation of a dataset sample and in direct comparison to other popular paraphrase datasets. We evaluate semantic similarity and lexical divergence and calculate a score base on their combination. The human evaluation results of the 4 generated monolingual datasets are shown in the following table:

| Language | Our dataset | Tatoeba |
| -------- | ----------- | ------- |
| en-en    | 0.256       | 0.307   |
| de-de    | 0.291       | 0.588   |
| sl-sl    | 0.271       | 0.015   |
| cs-cs    | 0.189       | 0.210   |


## Models

We train 6 different [mt5 models](https://huggingface.co/google/mt5-base), one for each of the datasets we have created. We refer to these models as mono- and multilingual models, even though they are originally multilingual mt5 models, because we train them on the generated mono- and multilingual datasets.

Our trained models can be accessed on huggingface:
- [MT5_small-enen](https://huggingface.co/yawnick/mt5-small-paracrawl-enen)
- [MT5_small-dede](https://huggingface.co/yawnick/mt5-small-paracrawl-dede)
- [MT5_small-slsl](https://huggingface.co/yawnick/mt5-small-paracrawl-slsl)
- [MT5_small-cscs](https://huggingface.co/yawnick/mt5-small-paracrawl-cscs)
- [MT5_small-multi_all](https://huggingface.co/yawnick/mt5-small-paracrawl-mutli-all)
- [MT5_small-multi_small](https://huggingface.co/yawnick/mt5-small-paracrawl-multi-small)

### Model Evaluation

We used the Parascore metric to evaluate all models. The Parascore evaluation results of the 4 monolingual trained models are shown in the following table:

| Language | Parascore score|
| -------- | -------------- |
| en-en    | 0.961          |
| de-de    | 0.925          |
| sl-sl    | 0.890          |
| cs-cs    | 0.922          |

The Parascore evaluation results of the 2 multilingual trained models are shown in the following table, which also shows the average scores for each of the 4 different language subparts of the test split of the multilingual dataset:

| Language       | Score multi-small | Score multi-all |
| -------------- | ----------------- | --------------- |
| whole test set | 0.925             | 0.925           |
| English part   | 0.938             | 0.939           |
| German part    | 0.926             | 0.925           |
| Slovene part   | 0.915             | 0.914           |
| Czech part     | 0.922             | 0.922           |


## Authors
* Nikolay Vasilev
* Jannik Weiß (YAWNICK)
* Jan Jenicek (hjeni)
