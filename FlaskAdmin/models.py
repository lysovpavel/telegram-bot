from app import db, admin
from flask_admin.contrib.sqla import ModelView


class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column('Ключ', db.String(256), unique=True)
    title = db.Column('Название', db.String(256), default='')
    content = db.Column('Контент', db.Text, default='')

    def __repr__(self):
        return f"<Command {self.key}>"


admin.add_view(ModelView(Command, db.session))


# >>> import models
# >>> from app import db
# >>> db.create_all()
