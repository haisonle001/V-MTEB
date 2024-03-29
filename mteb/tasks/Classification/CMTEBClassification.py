from ...abstasks import AbsTaskClassification

class TNews(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'TNews',
            'hf_hub_name': 'C-MTEB/TNews-classification',
            'description': 'Short Text Classification for News',
            "reference": "https://www.cluebenchmarks.com/introduce.html",
            'type': 'Classification',
            'category': 's2s',
            'eval_splits': ['validation'],
            'eval_langs': ['zh'],
            'main_score': 'accuracy',
            'samples_per_label': 32,
            'revision': '317f262bf1e6126357bbe89e875451e4b0938fe4',
        }


class IFlyTek(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'IFlyTek',
            'hf_hub_name': 'C-MTEB/IFlyTek-classification',
            'description': 'Long Text classification for the description of Apps',
            "reference": "https://www.cluebenchmarks.com/introduce.html",
            'type': 'Classification',
            'category': 's2s',
            'eval_splits': ['validation'],
            'eval_langs': ['zh'],
            'main_score': 'accuracy',
            'samples_per_label': 32,
            'n_experiments': 5,
            'revision': '421605374b29664c5fc098418fe20ada9bd55f8a',
        }


class MultilingualSentiment(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'MultilingualSentiment',
            'hf_hub_name': 'C-MTEB/MultilingualSentiment-classification',
            'description': 'A collection of multilingual sentiments datasets grouped into 3 classes -- positive, neutral, negative',
            "reference": "https://github.com/tyqiangz/multilingual-sentiment-datasets",
            'category': 's2s',
            'type': 'Classification',
            'eval_splits': ['validation'],
            'eval_langs': ['zh'],
            'main_score': 'accuracy',
            'samples_per_label': 32,
            'revision': '46958b007a63fdbf239b7672c25d0bea67b5ea1a',       
        }



class JDReview(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'JDReview',
            'hf_hub_name': 'C-MTEB/JDReview-classification',
            'description': 'review for iphone',
            'category': 's2s',
            'type': 'Classification',
            'eval_splits': ['test'],
            'eval_langs': ['zh'],
            'main_score': 'accuracy',
            'samples_per_label': 32,
            'revision': 'b7c64bd89eb87f8ded463478346f76731f07bf8b',
        }


class OnlineShopping(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'OnlineShopping',
            'hf_hub_name': 'C-MTEB/OnlineShopping-classification',
            'description': 'Sentiment Analysis of User Reviews on Online Shopping Websites',
            'category': 's2s',
            'type': 'Classification',
            'eval_splits': ['test'],
            'eval_langs': ['zh'],
            'main_score': 'accuracy',
            'samples_per_label': 32,
            'revision': 'e610f2ebd179a8fda30ae534c3878750a96db120',
        }


class Waimai(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'Waimai',
            'hf_hub_name': 'C-MTEB/waimai-classification',
            'description': 'Sentiment Analysis of user reviews on takeaway platforms',
            'category': 's2s',
            'type': 'Classification',
            'eval_splits': ['test'],
            'eval_langs': ['zh'],
            'main_score': 'accuracy',
            'samples_per_label': 32,
            'revision': '339287def212450dcaa9df8c22bf93e9980c7023',
        }
