from kaggleEuroSoc.helpers.database import Base

from sqlalchemy import Column, Integer, Text


class Team(Base):
    __tablename__ = 'Team'

    id = Column(Integer, primary_key=True)
    team_api_id = Column(Integer)
    team_fifa_api_id = Column(Integer)
    team_long_name = Column(Text)
    team_short_name = Column(Text)

    def __repr__(self):
        return f'id: {self.id}'
