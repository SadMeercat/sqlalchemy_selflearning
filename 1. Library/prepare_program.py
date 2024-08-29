import os
from sqlalchemy import create_engine
import schemas

def deleteDB():
    if os.path.exists('./library.db'):
        os.remove('./library.db')
    createDB()

def createDB():
    engine = create_engine("sqlite:///library.db")
    schemas.Base.metadata.create_all(engine)

if __name__ == '__main__':
    deleteDB()