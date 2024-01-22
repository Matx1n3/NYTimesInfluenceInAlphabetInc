import requests
import json
from api_key import api_key
from config import percentage


class StockPrice:
    """
        Clase para trabajar con datos de precios de acciones utilizando la API de Alpha Vantage.

        Atributos:
            api_key (str): Clave de API para acceder a Alpha Vantage.
            url (str): URL de la API de Alpha Vantage para obtener datos de precios diarios de acciones.
            percentage (int): Porcentaje utilizado para determinar las clases de cambio de precio.

        Métodos:
            __init__(self, download: str)
                Inicializa la clase. Descarga datos de precios si download es 'true' y los almacena en un archivo JSON.

            get_close_prices_in_series(self, day: str) -> tuple or str:
                Obtiene los precios de cierre de dos días consecutivos a partir de una fecha específica.

            get_class(self, day: str) -> int:
                Determina la clase del cambio de precio para un día específico, según ciertos criterios de porcentaje.

        Clases:
            0: Precio disminuido al menos un 2%
            1: Precio mantenido dentro de ±2%
            2: Precio aumentado al menos un 2%
    """

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOGL&outputsize=full&apikey=' + api_key

    def __init__(self, download):
        """
        Inicializa la clase StockPrice.

        Parámetros:
            download (str): Si es 'true', descarga los datos de precios y los guarda en un archivo JSON.
        """
        if download == 'true':
            r = requests.get(self.url)
            self.data = r.json()
            with open('../data/stock_data.json', 'w') as file:
                json.dump(self.data, file)
        else:
            with open('../data/stock_data.json') as file:
                self.data = json.load(file)

    def get_close_prices_in_series(self, day):
        """
        Obtiene los precios de cierre de dos días consecutivos a partir de una fecha específica.

        Parámetros:
            day (str): Fecha para la cual se obtendrán los precios de cierre.

        Devoluciones:
            tuple or str: Una tupla con los precios de cierre de dos días consecutivos o un mensaje de error.
        """
        if "Time Series (Daily)" not in self.data:
            return "No se encontró la serie temporal"

        time_series = self.data["Time Series (Daily)"]

        if day not in time_series:
            return "No hay datos para este día"

        series_dates = list(time_series.keys())
        day_index = series_dates.index(day)

        if day_index + 1 >= len(series_dates):
            return "No hay día siguiente disponible"

        next_day = series_dates[day_index + 1]

        return time_series[day]['4. close'], time_series[next_day]['4. close']

    def get_class(self, day):
        """
        Determina la clase del cambio de precio para un día específico, según ciertos criterios de porcentaje.

        Parámetros:
            day (str): Fecha para la cual se determinará la clase del cambio de precio.

        Devoluciones:
            int: La clase del cambio de precio (0, 1, o 2).
        """
        try:
            p_day0, p_day1 = self.get_close_prices_in_series(day)
            p_day0 = float(p_day0)
            p_day1 = float(p_day1)

        except:
            return -1

        if p_day1 > p_day0 + p_day0 * percentage * 0.01:
            return 2
        elif p_day1 < p_day0 - p_day0 * percentage * 0.01:
            return 0
        else:
            return 1
