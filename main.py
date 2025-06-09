import os
from database.database import DataSaver
from loaders.csv_loader import CSVLoader
from loaders.excel_loader import ExcelLoader


def cargar_csv_y_excel():
    csv_path = os.path.join(os.path.dirname(__file__), 'files', 'ventas.csv')
    excel_path = os.path.join(os.path.dirname(__file__), 'files', 'productos.xlsx')

    csv_dataset = CSVLoader(csv_path)
    csv_dataset.cargar_datos()

    excel_dataset = ExcelLoader(excel_path)
    excel_dataset.cargar_datos()

    saver = DataSaver()
    saver.guardar(csv_dataset.get_data(), 'ventas_csv')
    saver.guardar(excel_dataset.get_data(), 'productos_xlsx')


if __name__ == "__main__":
    cargar_csv_y_excel()
