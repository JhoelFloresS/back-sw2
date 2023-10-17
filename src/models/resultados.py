from .base import Base

import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

class Resultados(Base):
    __tablename__ = 'tabla_resultados'
    __table_args__ = {'extend_existing': True}

    tienda_id: Mapped[int] = mapped_column( primary_key=True )
    tienda: Mapped[str] = mapped_column( String(255), primary_key=True )
    venta_id: Mapped[int] = mapped_column( primary_key=True )
    fecha_venta: Mapped[datetime.datetime] = mapped_column( primary_key=True )
    precio_venta: Mapped[float] = mapped_column( primary_key=True )
    cantidad_venta: Mapped[int] = mapped_column( primary_key=True )
    descuento_venta: Mapped[float] = mapped_column( primary_key=True )
    total_venta: Mapped[float] = mapped_column( primary_key=True )
    tipo_venta_id: Mapped[int] = mapped_column( primary_key=True )
    tipo_venta: Mapped[str] = mapped_column( String(255), primary_key=True)
    sku_id: Mapped[int] = mapped_column( primary_key=True )
    sku_nom: Mapped[str] = mapped_column( String(255), primary_key=True)
    precio_inventario: Mapped[float] = mapped_column( primary_key=True )
    cantidad_inventario: Mapped[int] = mapped_column( primary_key=True )
    marca_id: Mapped[int] = mapped_column( primary_key=True )
    marca: Mapped[str] = mapped_column( String(255), primary_key=True)
    producto_id: Mapped[int] = mapped_column( primary_key=True )
    producto: Mapped[str] = mapped_column( String(255), primary_key=True)
    categoria_id: Mapped[int] = mapped_column( primary_key=True )
    categoria: Mapped[str] = mapped_column( String(255), primary_key=True)
    rubro_id: Mapped[int] = mapped_column( primary_key=True )
    rubro: Mapped[str] = mapped_column( String(255), primary_key=True)
