from kaggleEuroSoc.helpers.database import Base

from sqlalchemy import Column, Integer, Text


class Player_Attributes(Base):
    __tablename__ = 'Player_Attributes'

    id = Column(Integer, primary_key=True)
    player_fifa_api_id = Column(Integer)
    player_api_id = Column(Integer)
    date = Column(Text)
    overall_rating = Column(Integer)
    potential = Column(Integer)
    preferred_foot = Column(Text)
    attacking_work_rate = Column(Text)
    defensive_work_rate = Column(Text)
    crossing = Column(Integer)
    finishing = Column(Integer)
    heading_accuracy = Column(Integer)
    short_passing = Column(Integer)
    volleys = Column(Integer)
    dribbling = Column(Integer)
    curve = Column(Integer)
    free_kick_accuracy = Column(Integer)
    long_passing = Column(Integer)
    ball_control = Column(Integer)
    acceleration = Column(Integer)
    sprint_speed = Column(Integer)
    agility = Column(Integer)
    reactions = Column(Integer)
    balance = Column(Integer)
    shot_power = Column(Integer)
    jumping = Column(Integer)
    stamina = Column(Integer)
    strength = Column(Integer)
    long_shots = Column(Integer)
    aggression = Column(Integer)
    interceptions = Column(Integer)
    positioning = Column(Integer)
    vision = Column(Integer)
    penalties = Column(Integer)
    marking = Column(Integer)
    standing_tackle = Column(Integer)
    sliding_tackle = Column(Integer)
    gk_diving = Column(Integer)
    gk_handling = Column(Integer)
    gk_kicking = Column(Integer)
    gk_positioning = Column(Integer)
    gk_reflexes = Column(Integer)

    def __repr__(self):
        return f'id: {self.id}'
