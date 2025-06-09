from loaders.base_loader import BaseLoader
from validators.validator import DataValidator
import pandas as pd

class CSVLoader(BaseLoader):
    def cargar_datos(self):
        try:
            self._data = pd.read_csv(self._filepath)
        except Exception as e:
            print(f"Error al leer CSV{self._filepath}:{e}")
    
    def validar(self):
        if self._data is not None:
            validator = DataValidator(self._data)
            self._data = validator.validar()
        else:
            print("No hay datos para validar.")