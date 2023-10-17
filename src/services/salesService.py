from src.database.connection import engine
from src.models.resultados import Resultados

from sqlalchemy import select
import pandas as pd



class SalesService:

    def getSales(self):
        with engine.connect() as connection:
            query = connection.execute('SELECT * FROM resultados')
            return [dict(row) for row in query]


    def getSalesByFilter(self, tienda):
        resultadosToQuery = select(Resultados).where(Resultados.tienda_id == tienda)

        df = pd.read_sql(resultadosToQuery, con=engine)

        # tiendas = df.groupby(by=['tienda_id']).cantidad_venta.sum()

        tiendasJson = df.to_json(orient='records', force_ascii=False)

        return tiendasJson

