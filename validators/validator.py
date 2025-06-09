import pandas as pd

class DataValidator:
    def validar(self):
        if self.df is None or self.df.empty:
            raise ValueError("El DataFrame está vacío o no fue cargado correctamente.")

        self.df.drop_duplicates(inplace=True)
        self.df.dropna(how='all', inplace=True)

        for column, rules in self.schema.items():
            if rules.get("required", False) and column not in self.df.columns:
                raise ValueError(f"La columna obligatoria '{column}' no existe en el DataFrame.")

            if column in self.df.columns:
                expected_type = rules["type"]
                try:
                    self.df[column] = self.df[column].astype(expected_type)
                except Exception:
                    raise ValueError(f"La columna '{column}' no puede convertirse a {expected_type}.")

        required_cols = [col for col, rules in self.schema.items() if rules.get("required", False)]
        self.df.dropna(subset=required_cols, inplace=True)

        filas_finales = len(self.df)
        print(f"Validación completada. Filas finales: {filas_finales}")
        return self.df
    
    '''def resumen(self):
        try:
            if self._datos is not None:
                print(self._datos.describe(include='all'))
            else:
                print("No hay datos para mostrar resumen.")
        except Exception as e:
            print(f"Error al mostrar resumen: {e}")
    '''