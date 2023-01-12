from sklearn.metrics import mean_absolute_percentage_error
from statsmodels.tsa.arima.model import ARIMA

from historic_weather_forecast.data_preparation import get_model_data


def train_arima_model() -> float:
    data_train, data_validate, data_test = get_model_data()
    model = ARIMA(endog=data_train['temp'], dates=data_train['datetime'], freq='D', order=(1, 0, 1))
    model_fitted = model.fit()
    results = model_fitted.predict(start=0, end=len(data_validate) - 1)
    mape_validation_value = mean_absolute_percentage_error(data_validate['temp'].values, results.values)
    return mape_validation_value

