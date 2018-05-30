import json
from token import Token

class TrainingData(object):
    """Bertanggung jawab dalam memuat dan memproses data training."""

    def __init__(self, training_data):
        self.training_data = training_data if training_data else []