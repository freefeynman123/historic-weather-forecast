import pandas as pd

from typing import Tuple
from historic_weather_forecast.config.file_config import FileConfig

file_config = FileConfig()


def get_data_from_path(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data


def get_model_data() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    data_train, data_validate, data_test = get_data_from_path(file_config.train_file_path), get_data_from_path(
        file_config.validate_file_path), get_data_from_path(file_config.test_file_path)
    return data_train, data_validate, data_test
