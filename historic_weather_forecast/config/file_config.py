import dataclasses
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@dataclasses.dataclass()
class FileConfig:
    train_file_path: str = os.path.join(BASE_PATH, 'data/train.csv')
    validate_file_path: str = os.path.join(BASE_PATH, 'data/validate.csv')
    test_file_path: str = os.path.join(BASE_PATH, 'data/test.csv')
