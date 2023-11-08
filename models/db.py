from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# engine = create_engine("mysql://mysql:%40%409866499953AAaa@localhost:3306/fastapitest")



url = URL.create(
    drivername="mysql",
    username="mysql",
    password="@@9866499953AAaa",
    host="localhost",
    database="fastapitest",
    port=3306
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()


# Base.metadata.create_all(engine)