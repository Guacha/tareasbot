from tareasbot.database.models import Base


def initialise_database(engine):
    Base.metadata.create_all(engine)


def delete_database(engine):
    Base.metadata.drop_all(engine)
