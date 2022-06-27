import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from collections import defaultdict
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
ma = Marshmallow(app) 
api = Api(app)

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
        db.session.add(new_plate),
        db.session.commit(),
        return plate_schema.dump(new_plate)

api.add_resource(PlateResource, '/plate')

if __name__ == '__main__':
    app.run(debug=True)

