from injector import Module, singleton, provider
from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
Base = declarative_base()

class SqlModule(Module):
    @provider
    @singleton
    def provide_session(self) -> orm.Session:
        db_url = os.getenv('DATABASE_URL')
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        Session = orm.sessionmaker(bind=engine)
        return Session()
 