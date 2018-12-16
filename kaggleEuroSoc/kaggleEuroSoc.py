from kaggleEuroSoc.models.country import Country
from kaggleEuroSoc.models.league import League
from kaggleEuroSoc.models.match import Match
from kaggleEuroSoc.models.player import Player
from kaggleEuroSoc.models.player_attributes import Player_Attributes
from kaggleEuroSoc.models.team import Team
from kaggleEuroSoc.models.team_attribtues import Team_Attribtutes
from kaggleEuroSoc.helpers.database import create_session


def main():
    print('Connecting to databases')
    sqllite_session = create_session('sqlite:///database.sqlite')
    postgres_session = create_session('postgresql+psycopg2://username:password@localhost:5432/database', init=True)

    print('Beginning migration')
    migrate(Country, sqllite_session, postgres_session)
    migrate(League, sqllite_session, postgres_session)
    migrate(Match, sqllite_session, postgres_session)
    migrate(Player, sqllite_session, postgres_session)
    migrate(Player_Attributes, sqllite_session, postgres_session)
    migrate(Team, sqllite_session, postgres_session)
    migrate(Team_Attribtutes, sqllite_session, postgres_session)

    print('Migration complete')


def migrate(Model, origin_session, dest_session):
    print(f'Migrating table: {Model.__tablename__}')
    for result in origin_session.query(Model).order_by(Model.id):
        prop_dict = vars(result)
        prop_dict.pop('_sa_instance_state')

        # Uncomment the below if you do not want to import the original IDs

        # prop_dict.pop('id')
        # if 'country_id' in prop_dict.keys():
        #     prop_dict.pop('country_id')
        # if 'league_id' in prop_dict.keys():
        #     prop_dict.pop('league_id')

        new_row = Model(**prop_dict)
        dest_session.add(new_row)
    dest_session.commit()


if __name__ == '__main__':
    main()
