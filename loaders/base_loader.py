from abc import ABC, abstractmethod
import pandas as pd

class BaseLoader(ABC):
    def __init__(self, filepath):
        self._filepath = filepath
        self._data = None

    @property
    def datos(self):
        return self._data

    @abstractmethod
    def cargar_datos(self):
        pass

    def get_data(self):
        return self._data