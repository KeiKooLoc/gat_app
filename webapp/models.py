# -----------------------------------------------------------------------------
# Standard Library Imports
# -----------------------------------------------------------------------------
import os
# -----------------------------------------------------------------------------
# Related Libraries Imports
# -----------------------------------------------------------------------------
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource
# -----------------------------------------------------------------------------
# Local Imports
# -----------------------------------------------------------------------------
from webapp.app import db


# DB models
# -----------------------------------------------------------------------------
class Country(db.Model):
    __tablename__ = "country"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # country_code = db.Column(db.String(128), nullable=False)
    # panel_provider_id = db.Column(db.String(128), nullable=False)

    # def __init__(self, country_code, panel_provider_id):
    #     self.country_code = country_code
    #     self.panel_provider_id = panel_provider_id
    
    # def __repr__(self):
    #     return '<Country %r>' % (self.country_code)


class PanelProvider(db.Model):
    __tablename__ = "panel_provider"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # code = db.Column()


class Location(db.Model):
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # id, name, external_id, secret_code

class LocationGroup(db.Model):
    __tablename__ = "location_group"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # id, name, country_id, panel_provider_id


class TargetGroup(db.Model):
    __tablename__ = "target_group"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id, name, external_id, parent_id, secret_code, panel_provider_id


# API models
# -----------------------------------------------------------------------------
class LocationApi(Resource):
    
    #get location by country code
    def get(self, country_code):
        return 'db search by country_code'

    def post(self, country_code):
        new = countrycode
        return 'db update new', 201



class TargetApi(Resourcd):

    #  get target groups by country code
    def get(self, country_code):
        return 'db search by country code'