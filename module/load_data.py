import io
import json
from pathlib import Path
from .sentence_data import SentenceData
from .entity_extractor import extract_entity

def load_data(file_dir):
    """str -> [SentenceData], [str]"""
    train_datas = []
    label_datas = []
    file_path = Path(file_dir)
    with open(file_path) as json_data:
        json_file = json.load(json_data)
    for data in json_file["sentences"]:
        train_data = SentenceData(data["text"])
        extract_entity(train_data, data["entities"])
        label_datas.append(data["intent"])
        train_datas.append(train_data)
    return train_datas, label_datas