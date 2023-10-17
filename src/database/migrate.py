from src.models.base import Base
from src.database.connection import engine
from src.models.allInOne import AllInOne


AllInOne.metadata.create_all(engine)


# Base.metadata.create_all(engine)