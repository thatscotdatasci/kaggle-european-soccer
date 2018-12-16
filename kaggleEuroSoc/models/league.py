from kaggleEuroSoc.helpers.database import Base

from sqlalchemy import Column, Integer, Text, ForeignKey


class League(Base):
    __tablename__ = 'League'

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('Country.id'))
    name = Column(Text)

    def __repr__(self):
        return f'id: {self.id}'
