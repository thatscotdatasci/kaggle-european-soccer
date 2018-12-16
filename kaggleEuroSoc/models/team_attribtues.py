from kaggleEuroSoc.helpers.database import Base

from sqlalchemy import Column, Integer, Text


class Team_Attribtutes(Base):
    __tablename__ = 'Team_Attributes'

    id = Column(Integer, primary_key=True)
    team_fifa_api_id = Column(Integer)
    team_api_id = Column(Integer)
    date = Column(Text)
    buildUpPlaySpeed = Column(Integer)
    buildUpPlaySpeedClass = Column(Text)
    buildUpPlayDribbling = Column(Integer)
    buildUpPlayDribblingClass = Column(Text)
    buildUpPlayPassing = Column(Integer)
    buildUpPlayPassingClass = Column(Text)
    buildUpPlayPositioningClass = Column(Text)
    chanceCreationPassing = Column(Integer)
    chanceCreationPassingClass = Column(Text)
    chanceCreationCrossing = Column(Integer)
    chanceCreationCrossingClass = Column(Text)
    chanceCreationShooting = Column(Integer)
    chanceCreationShootingClass = Column(Text)
    chanceCreationPositioningClass = Column(Text)
    defencePressure = Column(Integer)
    defencePressureClass = Column(Text)
    defenceAggression = Column(Integer)
    defenceAggressionClass = Column(Text)
    defenceTeamWidth = Column(Integer)
    defenceTeamWidthClass = Column(Text)
    defenceDefenderLineClass = Column(Text)

    def __repr__(self):
        return f'id: {self.id}'
