import csv
from relevant_words import *


class CSVManager:
    """
    Clase para gestionar la creación y escritura de datos en un archivo CSV.

    Atributos:
        data (list): Lista que almacena los datos a ser escritos en el archivo CSV.

    Métodos:
        __init__(self)
            Inicializa la clase CSVManager.

        add_datum(self, wordbag: dict, w_class: int)
            Agrega un conjunto de datos y su clase correspondiente a la lista de datos.

        store_en_csv(self, filename: str)
            Almacena los datos en un archivo CSV con el nombre de archivo proporcionado.

    Uso:
        csv_manager = CSVManager()
        csv_manager.add_datum(wordbag, w_class)
        csv_manager.store_en_csv('archivo.csv')
    """
    def __init__(self):
        """
        Inicializa la clase CSVManager.
        """
        self.data = []

    def add_datum(self, wordbag, w_class):
        """
        Agrega un conjunto de datos y su clase correspondiente a la lista de datos.

        Parámetros:
            wordbag (dict): Un diccionario que representa un conjunto de datos.
            w_class (int): La clase correspondiente al conjunto de datos.

        Uso:
            csv_manager.add_datum(wordbag, w_class)
        """
        if w_class != -1:
            data_row = {word: wordbag.get(word, 0) for word in relevant_words}
            data_row['Class'] = w_class
            self.data.append(data_row)

    def store_en_csv(self, filename):
        """
        Almacena los datos en un archivo CSV con el nombre de archivo proporcionado.

        Parámetros:
            filename (str): El nombre del archivo CSV en el que se almacenarán los datos.

        Uso:
            csv_manager.store_en_csv('archivo.csv')
        """
        if not self.data:
            print("You have to add data first")
            return

        headers = relevant_words + ['Class']

        with open("out/" + filename, 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
            csv_writer.writeheader()

            for datum in self.data:
                csv_writer.writerow(datum)
