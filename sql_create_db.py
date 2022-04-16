from sql_database import Video, engine, Base


Base.metadata.create_all(engine)
