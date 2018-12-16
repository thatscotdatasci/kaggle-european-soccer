from kaggleEuroSoc.helpers.database import Base

from sqlalchemy import Column, Integer, Text, Numeric, ForeignKey


class Match(Base):
    __tablename__ = 'Match'

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('Country.id'))
    league_id = Column(Integer, ForeignKey('League.id'))
    season = Column(Text)
    stage = Column(Integer)
    date = Column(Text)
    match_api_id = Column(Integer)
    home_team_api_id = Column(Integer)
    away_team_api_id = Column(Integer)
    home_team_goal = Column(Integer)
    away_team_goal = Column(Integer)
    home_player_X1 = Column(Integer)
    home_player_X2 = Column(Integer)
    home_player_X3 = Column(Integer)
    home_player_X4 = Column(Integer)
    home_player_X5 = Column(Integer)
    home_player_X6 = Column(Integer)
    home_player_X7 = Column(Integer)
    home_player_X8 = Column(Integer)
    home_player_X9 = Column(Integer)
    home_player_X10 = Column(Integer)
    home_player_X11 = Column(Integer)
    away_player_X1 = Column(Integer)
    away_player_X2 = Column(Integer)
    away_player_X3 = Column(Integer)
    away_player_X4 = Column(Integer)
    away_player_X5 = Column(Integer)
    away_player_X6 = Column(Integer)
    away_player_X7 = Column(Integer)
    away_player_X8 = Column(Integer)
    away_player_X9 = Column(Integer)
    away_player_X10 = Column(Integer)
    away_player_X11 = Column(Integer)
    home_player_Y1 = Column(Integer)
    home_player_Y2 = Column(Integer)
    home_player_Y3 = Column(Integer)
    home_player_Y4 = Column(Integer)
    home_player_Y5 = Column(Integer)
    home_player_Y6 = Column(Integer)
    home_player_Y7 = Column(Integer)
    home_player_Y8 = Column(Integer)
    home_player_Y9 = Column(Integer)
    home_player_Y10 = Column(Integer)
    home_player_Y11 = Column(Integer)
    away_player_Y1 = Column(Integer)
    away_player_Y2 = Column(Integer)
    away_player_Y3 = Column(Integer)
    away_player_Y4 = Column(Integer)
    away_player_Y5 = Column(Integer)
    away_player_Y6 = Column(Integer)
    away_player_Y7 = Column(Integer)
    away_player_Y8 = Column(Integer)
    away_player_Y9 = Column(Integer)
    away_player_Y10 = Column(Integer)
    away_player_Y11 = Column(Integer)
    home_player_1 = Column(Integer)
    home_player_2 = Column(Integer)
    home_player_3 = Column(Integer)
    home_player_4 = Column(Integer)
    home_player_5 = Column(Integer)
    home_player_6 = Column(Integer)
    home_player_7 = Column(Integer)
    home_player_8 = Column(Integer)
    home_player_9 = Column(Integer)
    home_player_10 = Column(Integer)
    home_player_11 = Column(Integer)
    away_player_1 = Column(Integer)
    away_player_2 = Column(Integer)
    away_player_3 = Column(Integer)
    away_player_4 = Column(Integer)
    away_player_5 = Column(Integer)
    away_player_6 = Column(Integer)
    away_player_7 = Column(Integer)
    away_player_8 = Column(Integer)
    away_player_9 = Column(Integer)
    away_player_10 = Column(Integer)
    away_player_11 = Column(Integer)
    goal = Column(Text)
    shoton = Column(Text)
    shotoff = Column(Text)
    foulcommit = Column(Text)
    card = Column(Text)
    cross = Column(Text)
    corner = Column(Text)
    possession = Column(Text)
    B365H = Column(Numeric)
    B365D = Column(Numeric)
    B365A = Column(Numeric)
    BWH = Column(Numeric)
    BWD = Column(Numeric)
    BWA = Column(Numeric)
    IWH = Column(Numeric)
    IWD = Column(Numeric)
    IWA = Column(Numeric)
    LBH = Column(Numeric)
    LBD = Column(Numeric)
    LBA = Column(Numeric)
    PSH = Column(Numeric)
    PSD = Column(Numeric)
    PSA = Column(Numeric)
    WHH = Column(Numeric)
    WHD = Column(Numeric)
    WHA = Column(Numeric)
    SJH = Column(Numeric)
    SJD = Column(Numeric)
    SJA = Column(Numeric)
    VCH = Column(Numeric)
    VCD = Column(Numeric)
    VCA = Column(Numeric)
    GBH = Column(Numeric)
    GBD = Column(Numeric)
    GBA = Column(Numeric)
    BSH = Column(Numeric)
    BSD = Column(Numeric)
    BSA = Column(Numeric)

    def __repr__(self):
        return f'id: {self.id}'