from .base import Base

import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

class AllInOne(Base):
    __tablename__ = 'all_in_one'

    id: Mapped[int] = mapped_column(primary_key=True)
    pdv_id: Mapped[int]
    pdv_nom: Mapped[str] = mapped_column( String(100) )
    pdv_clientes_id: Mapped[int]
    pdv_clientes_nom: Mapped[str] = mapped_column( String(100) )
    pdv_ventas_id: Mapped[int]
    pdv_ventas_total: Mapped[float]
    pdv_ventas_fecha: Mapped[datetime.datetime]
    pdv_ventas_detalles_id: Mapped[int]
    pdv_ventas_detalles_precio: Mapped[float]
    pdv_ventas_detalles_cantidad: Mapped[int]
    sku_id: Mapped[int]
    sku_nom: Mapped[str] = mapped_column( String(100) )
    sku_pdv_id: Mapped[int]
    sku_pdv_nom_tem: Mapped[str] = mapped_column( String(100) )
    sku_pdv_costo: Mapped[float]
    sku_pdv_precio: Mapped[float]
    sku_pdv_cantidad: Mapped[int]
    productos_id: Mapped[int]
    productos_nom: Mapped[str] = mapped_column( String(100) )
    categorias_id: Mapped[int]
    categorias_nom: Mapped[str] = mapped_column( String(100) )
    rubro_id: Mapped[int]
    rubro_nom: Mapped[str] = mapped_column( String(100) )
    color_empaque_id: Mapped[int]
    color_empaque_nom: Mapped[str] = mapped_column( String(100) )
    fragancias_id: Mapped[int]
    fragancias_nom: Mapped[str] = mapped_column( String(100) )
    marcas_id: Mapped[int]
    marcas_nom: Mapped[str] = mapped_column( String(100) )
    sabores_id: Mapped[int]
    sabores_nom: Mapped[str] = mapped_column( String(100) )
    tipo_empaque_id: Mapped[int]
    tipo_empaque_nom: Mapped[str] = mapped_column( String(100) )
