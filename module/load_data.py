import io
import json
from pathlib import Path
from training_data import TrainingData

def load_data(file_dir):
    file_path = Path(file_dir)
    with open(file_path) as json_data:
        json_file = json.load(json_data)
    #print(json_file['sentences'])
    return TrainingData(json_file)