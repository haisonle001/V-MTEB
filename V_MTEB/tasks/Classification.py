from mteb import AbsTaskClassification

class Vietnamese_Student_Sentiment(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'Vietnamese_Student_Sentiment',
            'hf_hub_name': 'another-symato/VMTEB-vietnamese_students_feedback_sentiment',
            'description': 'Sentiment Analysis of student reviews',
            'category': 's2s',
            'type': 'Classification',
            'eval_splits': ['validation', 'test'],
            'eval_langs': ['vie'],
            'main_score': 'accuracy',
            "n_experiments": 10,
            'samples_per_label': 32,
        }
class Vietnamese_Student_Topic(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'Vietnamese_Student_Topic',
            'hf_hub_name': 'another-symato/VMTEB-vietnamese_students_feedback_topic',
            'description': 'Sentiment Analysis of student reviews',
            'category': 's2s',
            'type': 'Classification',
            'eval_splits': ['validation', 'test'],
            'eval_langs': ['vie'],
            'main_score': 'accuracy',
            "n_experiments": 10,
            'samples_per_label': 32,
        }