from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Permit(db.Model):
    plate = db.Column(db.String(10), primary_key=True)
    owner = db.Column(db.String(30), nullable=False)
    start_date = db.Column(db.String(50), default=datetime.now(timezone.utc).isoformat()\
        .replace("+00:00", "Z"))
    end_date = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Plate('{self.plate}', '{self.owner}', '{self.start_date}', '{self.end_date}')"

@app.route('/')
def home():
    return 'init'

if __name__ == '__main__':
    app.run(debug=True)

