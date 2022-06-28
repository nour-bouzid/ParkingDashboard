import re
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from collections import defaultdict
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
ma = Marshmallow(app) 
api = Api(app)
CORS(app, resources={r"/*":{'origins':"*"}})
CORS(app, resources={r"/*":{'origins':'http://localhost:5000',"allow_headers":"Access-Control-Allow-Origin"}})

class Plate(db.Model):
    plate = db.Column(db.String(10), primary_key=True)
    owner = db.Column(db.String(30))
    start_date = db.Column(db.String(50), default=datetime.now(timezone.utc).isoformat()\
        .replace("+00:00", "Z"))
    end_date = db.Column(db.String(50))

    def __repr__(self):
        return f"Plate('{self.plate}', '{self.owner}', '{self.start_date}', '{self.end_date}')"

class PlateSchema(ma.Schema):
    class Meta:
        fields = ("plate","owner","start_date","end_date")
        model = Plate

plate_schema = PlateSchema()
plates_schema = PlateSchema(many=True)

def malformed(data):
    if data['start_date'] != '':
        try:
            datetime.strptime(data['start_date'], '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            return True

    if data['end_date'] != '':
        try:
            datetime.strptime(data['end_date'], '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            return True

    if re.search("^[A-Z]{1,3}-[A-Z]{1,2}((?!0)[0-9]{0,4})$", data['plate']):
        return False
    else:
        return True
    
class PlateResource(Resource):
    def get(self):
        plates = Plate.query.all()
        return plates_schema.dump(plates)

    def post(self):
        data = defaultdict(str, request.json)
        new_plate = Plate(
            plate=data['plate'],
            owner=data['owner'],
            start_date=data['start_date'],
            end_date=data['end_date']
        )
        try:
            db.session.add(new_plate),
            db.session.commit(),
            if malformed(data):
                return 'malformed', 402
            return plate_schema.dump(new_plate), 200
        except Exception as e:
            return f'error: {e}', 400

api.add_resource(PlateResource, '/plate')

if __name__ == '__main__':
    app.run(debug=True)

