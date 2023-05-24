import csv
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Post
from datetime import datetime
from dateutil.parser import parse

engine = create_engine("sqlite:///db.sqlite")
Session = sessionmaker(autocommit=False, autoflush=True, bind=engine)


@contextmanager
def db_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def insert_data_from_csv(file):
    with open(
        f"/home/vector-phi/Documents/pydb/app/{file}", "r", encoding="utf-8"
    ) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        with db_session() as session:
            for row in csvreader:
                user_id = int(row[0])
                first_name = row[1]
                last_name = row[2]
                post_id = int(row[3])
                date = parse(row[4])

                user = User(user_id=user_id, first_name=first_name, last_name=last_name)
                post = Post(post_id=post_id, user_id=user_id, date=date)
                print(user)
                print(post)
                session.add(user)
                session.add(post)
                print(f"Added record for User {first_name} succesfully!")


insert_data_from_csv("test_upload.csv")
