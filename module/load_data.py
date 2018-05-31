import io
import json
from pathlib import Path
from .training_data import TrainingData

def load_data(file_dir):
    train_datas = []
    file_path = Path(file_dir)
    with open(file_path) as json_data:
        json_file = json.load(json_data)
    for data in json_file["sentences"]:
        train_data = TrainingData(data["text"], data["intent"], data["entities"])
        train_datas.append(train_data)
    return train_datas