from get_links import get_links
from get_stock_price import *
from get_wordbag import get_wordbag_and_date
from csv_manager import *
from config import *

# Obtención de enlaces
print("Getting links...")
links = get_links(min_amount)
CSVManager = CSVManager()   # Instancia de la clase CSVManager para gestionar los datos

# Descarga de precios de acciones
if download_stock_data:
    print("Downloading stock prices...")
stockPrice = StockPrice(download_stock_data)


# Iteración a través de los enlaces
print("Iterating through links...")
i = 0
for link in links:
    print("Link " + str(i) + "\n")
    wordbag, date = get_wordbag_and_date(link)
    # Agrega los datos al CSVManager, incluyendo el conjunto de datos y su clase de cambio de precio
    CSVManager.add_datum(wordbag, stockPrice.get_class(date))
    i += 1

# Almacena los datos en un archivo CSV
CSVManager.store_en_csv(dataset_filename)

print("Done!")
