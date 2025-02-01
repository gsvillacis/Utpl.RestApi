from pydantic import EmailStr
from sqlalchemy.orm import session
from app.models import User, PostUser


def get_user(db: session, email: EmailStr):
    return db.query(User).filter(User.email == email).first()


def create_user(db: session, user: PostUser):
    passHash = secure_pwd(user.password)
    db_user = User(email=user.email, username=user.username,
                   hashed_password=passHash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
