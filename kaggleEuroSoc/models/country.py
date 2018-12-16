from kaggleEuroSoc.helpers.database import Base

from sqlalchemy import Column, Integer, Text


class Country(Base):
    __tablename__ = 'Country'

    id = Column(Integer, primary_key=True)
    name = Column(Text)

    def __repr__(self):
        return f'id: {self.id}'
