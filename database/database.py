from sqlalchemy import create_engine
from decouple import config
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

class DataSaver:
    def __init__(self):
        user = config('DB_USER')
        password = config('DB_PASSWORD')
        host = config('DB_HOST')
        port = config('DB_PORT')
        database = config('DB_NAME')
        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(url)

    def guardar(self, df: pd.DataFrame, table_name: str):
        if df.empty:
            print(f"No se guardó '{table_name}' porque está vacío.")
            return

        try:
            df.to_sql(table_name, con=self.engine, index=False, if_exists="replace")
            print(f"Tabla '{table_name}' creada correctamente con {len(df)} registros.")
        except SQLAlchemyError as e:
            print(f"Error guardando la tabla '{table_name}': {e}")