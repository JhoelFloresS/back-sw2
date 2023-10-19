from src.database.connection import engine
from src.models.resultados import Resultados
from src.database.connection import engine

from sqlalchemy import select
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import json


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

    def getSimilary(_, tienda):

        resultadosToQuery = select(Resultados)

        df = pd.read_sql(resultadosToQuery, con=engine)

        store_items_matrix = df.pivot_table(
            index='tienda_id',
            columns='sku_id',
            values='cantidad_venta',
            aggfunc='sum'
        )

        store_items_matrix = store_items_matrix.applymap(lambda x: 1 if x>0 else 0)

        store_sim_matrix = pd.DataFrame(
                cosine_similarity( store_items_matrix)
            )


        store_sim_matrix['tienda_id'] = store_items_matrix.index
        store_sim_matrix = store_sim_matrix.set_index('tienda_id')
        store_sim_matrix.columns = store_items_matrix.index

        store_a = int(tienda)

        similitudes = store_sim_matrix.loc[store_a].sort_values(ascending=False)
        # return 'all ight'
        similitudes = pd.DataFrame(similitudes)

        #resetear el index
        similares = similitudes.reset_index()

        #renombrar columna
        similares.rename(columns={ similares.columns[0]: 'tiendas'}, inplace = True)

        similares.rename(columns={ similares.columns[1]: 'similitud'}, inplace = True)

        #change id to names
        tiendas_names = df.loc[df['tienda_id'].isin(set(similares['tiendas'])), ['tienda_id','tienda']
        ].drop_duplicates().set_index('tienda_id')

        similares = similares.sort_values('tiendas', ascending=True)
        tiendas_name = tiendas_names.sort_values('tienda_id', ascending=True)

        store_b = int(similares[similares.similitud < 0.99999].max()['tiendas'])

        similares['tiendas'] = tiendas_name['tienda'].tolist()

        similares = similares.set_index('tiendas')

        # obtener items comprados por clientes
        items_bouth_in_a = set(store_items_matrix.loc[store_a].iloc[
            store_items_matrix.loc[store_a].to_numpy().nonzero()
            ].index)

        items_bouth_in_b = set(store_items_matrix.loc[store_b].iloc[
            store_items_matrix.loc[store_b].to_numpy().nonzero()
            ].index)


        items_to_recommend_to_B = items_bouth_in_a - items_bouth_in_b

        resultado = df.loc[
            df['sku_id'].isin(items_to_recommend_to_B),
            ['sku_nom']
            ].drop_duplicates().reset_index(drop=True)

        resultado.rename(columns={ resultado.columns[0]: 'producto'}, inplace = True)

        response = json.dumps([similares.to_dict(), resultado.to_dict()], ensure_ascii=False)
        return response