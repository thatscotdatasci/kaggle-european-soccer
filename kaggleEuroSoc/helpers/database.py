from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_session(connection_string, echo=False, init=False):
    engine = create_engine(connection_string, echo=echo)

    if init:
        init_db(engine)

    Session = sessionmaker(bind=engine)
    return Session()


def init_db(engine):
    import kaggleEuroSoc.models
    Base.metadata.create_all(bind=engine)
