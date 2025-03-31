from app import app, db
from app.models import User

with app.app_context():
    users = User.query.all()
    for user in users:
 #       print(user.id)
        print(user.username)
        print(user.email)
