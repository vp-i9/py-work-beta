from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import create_engine

# from db import Base
from models import User, Post
from sqlalchemy.orm import sessionmaker

# from models import User, Post
from datetime import datetime

Base = declarative_base()


engine = create_engine("sqlite:///db.sqlite")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()


# # Create sample instances

# user1 = User(user_id=4, first_name="Emily", last_name="Johnson")
# user2 = User(user_id=5, first_name="Daniel", last_name="Williams")
# user3 = User(user_id=6, first_name="Sophia", last_name="Brown")

# post1 = Post(post_id=4, user_id=4, date=datetime.datetime(2023, 5, 19, 9, 0, 0))
# post2 = Post(post_id=5, user_id=5, date=datetime.datetime(2023, 5, 19, 10, 30, 0))
# post3 = Post(post_id=6, user_id=6, date=datetime.datetime(2023, 5, 19, 11, 45, 0))


# # Add instances to the session and commit
# session.add_all([user1, user2, user3, post1, post2, post3])
# session.commit()

# # Test querying the data
# print("Users:")
# users = session.query(User).all()
# for user in users:
#     print(user)

# print("\nPosts:")
# posts = session.query(Post).all()
# for post in posts:
#     print(post)
