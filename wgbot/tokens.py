from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Alexey/PYTHON/wgbot/tokens.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////opt/WGBOT/tokens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Tokens(db.Model):
    account_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10), nullable=False)
    access_token = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(24), nullable=False)
    expires_at = db.Column(db.Integer, nullable=False)
    telegram_id = db.Column(db.Integer, nullable=True)
    vk_id = db.Column(db.Integer, nullable=True)
    squad = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<Tokens %r>' % self.account_id

