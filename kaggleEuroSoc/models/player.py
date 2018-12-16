from kaggleEuroSoc.helpers.database import Base

from sqlalchemy import Column, Integer, Text


class Player(Base):
    __tablename__ = 'Player'

    id = Column(Integer, primary_key=True)
    player_api_id = Column(Integer)
    player_name = Column(Text)
    player_fifa_api_id = Column(Integer)
    birthday = Column(Text)
    height = Column(Integer)
    weight = Column(Integer)

    def __repr__(self):
        return f'id: {self.id}'
