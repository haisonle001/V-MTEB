import logging

import numpy as np
import tqdm

from ..evaluation.evaluators import ClusteringEvaluator
from .AbsTask import AbsTask

logger = logging.getLogger(__name__)


class AbsTaskClustering(AbsTask):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _add_main_score(self, scores):
        if self.description["main_score"] in scores:
            scores["main_score"] = scores[self.description["main_score"]]
        else:
            logger.warn(f"main score {self.description['main_score']} not found in scores {scores.keys()}")
            
    def evaluate(self, model, split="test", **kwargs):
        if not self.data_loaded:
            self.load_data()

        if self.is_multilingual:
            scores = {}
            for lang in self.dataset:
                logger.info(f"\nTask: {self.description['name']}, split: {split}, language: {lang}. Running...")
                scores[lang] = self._evaluate_monolingual(model, self.dataset[lang], split, **kwargs)
                self._add_main_score(scores[lang])
        else:
            logger.info(f"\nTask: {self.description['name']}, split: {split}. Running...")
            scores = self._evaluate_monolingual(model, self.dataset, split, **kwargs)
            self._add_main_score(scores)
        
        return scores
    
    def _evaluate_monolingual(self, model, dataset, split="test", **kwargs):
        v_measures = []
        for cluster_set in tqdm.tqdm(dataset[split], desc="Clustering"):
            evaluator = ClusteringEvaluator(cluster_set["sentences"], cluster_set["labels"], **kwargs)
            metrics = evaluator(model)
            v_measures.append(metrics["v_measure"])

        v_mean = np.mean(v_measures)
        v_std = np.std(v_measures)
        return {"v_measure": v_mean, "v_measure_std": v_std}
