<h1 align="center">Vietnamese Massive Text Embedding Benchmark</h1>
<p align="center">
    <a href="https://www.python.org/">
        <img alt="Build" src="https://img.shields.io/badge/Made with-Python-red">
    </a>
</p>

<h4 align="center">
    <p>
        <a href=#installation>Installation</a> | 
        <a href=#evaluation>Evaluation</a>  |
        <a href="#leaderboard">Leaderboard</a> |
        <a href="#tasks">Tasks</a> |
        <a href="#acknowledgement">Acknowledgement</a> |
    <p>
</h4>


## Installation
V-MTEB is devloped based on [MTEB](https://github.com/embeddings-benchmark/mteb). 

Clone this repo and install as editable
```
git clone https://github.com/haisonle001/V-MTEB.git
cd V-MTEB
pip install -e .
```

## Evaluation

### Evaluate reranker
```bash
python eval_cross_encoder.py --model_name_or_path BAAI/bge-reranker-base
```
 
### Evaluate embedding model
* **With scripts** 
Scripts will be updated soon.

* **With sentence-transformers** 
 
You can use V-MTEB easily in the same way as [MTEB](https://github.com/embeddings-benchmark/mteb).

```python
from mteb import MTEB
from V_MTEB import *
from sentence_transformers import SentenceTransformer

# Define the sentence-transformers model name
model_name = "fill-your-model-name"

model = SentenceTransformer(model_name)
evaluation = MTEB(task_langs=['vi'])
results = evaluation.run(model, output_folder=f"vi_results/{model_name}")
```


* **Using a custom model**  
To evaluate a new model, you can load it via sentence_transformers if it is supported by sentence_transformers.
Otherwise, models should be implemented like below (implementing an `encode` function taking as input a list of sentences, and returning a list of embeddings (embeddings can be `np.array`, `torch.tensor`, etc.).): 

```python
class MyModel():
    def encode(self, sentences, batch_size=32, **kwargs):
        """ Returns a list of embeddings for the given sentences.
        Args:
            sentences (`List[str]`): List of sentences to encode
            batch_size (`int`): Batch size for the encoding

        Returns:
            `List[np.ndarray]` or `List[tensor]`: List of embeddings for the given sentences
        """
        pass

model = MyModel()
evaluation = MTEB(tasks=["Vietnamese_Student_Topic"])
evaluation.run(model)
```


## Leaderboard

Will be updated soon.

## Tasks

An overview of tasks and datasets available in MTEB-chinese is provided in the following table:

| Name |  Hub URL | Description | Type | Category |  Test #Samples | 
|-----|-----|---------------------------|-----|-----|-----|
<!--
| [T2Retrieval](https://arxiv.org/abs/2304.03679) | [C-MTEB/T2Retrieval](https://huggingface.co/datasets/C-MTEB/T2Retrieval) |  T2Ranking: A large-scale Chinese Benchmark for Passage Ranking | Retrieval | s2p | 24,832 | 
| [MMarcoRetrieval](https://github.com/unicamp-dl/mMARCO) | [C-MTEB/MMarcoRetrieval](https://huggingface.co/datasets/C-MTEB/MMarcoRetrieval) | mMARCO is a multilingual version of the MS MARCO passage ranking dataset | Retrieval | s2p | 7,437 | 
| [DuRetrieval](https://aclanthology.org/2022.emnlp-main.357.pdf) | [C-MTEB/DuRetrieval](https://huggingface.co/datasets/C-MTEB/DuRetrieval) | A Large-scale Chinese Benchmark for Passage Retrieval from Web Search Engine | Retrieval | s2p | 4,000 |
| [JDReview](https://huggingface.co/datasets/kuroneko5943/jd21) |  [C-MTEB/JDReview-classification](https://huggingface.co/datasets/C-MTEB/JDReview-classification) | review for iphone | Classification | s2s |  533  |
--> 

## Acknowledgement

We thank the great tool from [Massive Text Embedding Benchmark](https://github.com/embeddings-benchmark/mteb)  and the open-source datasets from Vietnam NLP community.


## Citation

If you find this repository useful, please consider citation this repo.
