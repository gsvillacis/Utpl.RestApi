from sqlalchemy.orm import Session


def get_user(db: session, email: emailstr):
    return db.query(user).filter(User.email == email).first()


def create_user(db: session, user: PostUser):
    passHash = secure_pwd(user.password)
    db_user = User(email=user.email, username=user.username,
                   hashed_password=passHash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
