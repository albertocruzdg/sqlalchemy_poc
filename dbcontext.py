from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

connection_string = ""

# session = Session()

class DbContext:
    def __init__(self):
        self.engine = create_engine(connection_string)
        self.engine.connect()

        # ensure_created(self.engine)

        self.get_session = sessionmaker(bind=self.engine)