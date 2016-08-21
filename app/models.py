from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    # Optional: Gibt einen lesbaren String zurück für z.B. debugging oder testing
    def __repr__(self):
        return '<Role %r' % self.name


class User(db.Model):
    __tablename = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # Optional: Gibt einen lesbaren String zurück für z.B. debugging oder testing
    def __repr__(self):
        return '<User %r' % self.username