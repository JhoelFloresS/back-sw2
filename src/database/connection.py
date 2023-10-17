from sqlalchemy import create_engine
from decouple import config

# Database connection
# https://docs.sqlalchemy.org/en/14/core/engines.html#mysql

host = config('DB_HOST')
dbname = config('DB_NAME')
username = config('DB_USERNAME')
password = config('DB_PASSWORD')

conection = "mysql+pymysql://{username}:{password}@{host}/{dbname}"
engine = create_engine(conection.format(
    username=username,
    password=password,
    host=host,
    dbname=dbname
))