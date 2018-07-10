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
    country_code = db.Column(db.Integer, nullable=False)
    panel_provider_id = db.relationship('location_group', backref='id', lazy='dynamic')

    # def __init__(self, country_code, panel_provider_id):
    #     self.country_code = country_code
    #     self.panel_provider_id = panel_provider_id
    
    # def __repr__(self):
    #     return '<Country %r>' % (self.country_code)


class PanelProvider(db.Model):
    __tablename__ = "panel_provider"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.Integer, unique=True)


class Location(db.Model):
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True, unique=True)
    external_id = db.relationship('location', secondary=LocationGroup, backref=db.backref('location_group', lazy=True), lazy='subquery')
    secret_code = db.Column(db.String(120), index=True, unique=True)


LocationGroup = db.Table('location_group',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('name', db.String(120), index=True, unique=True),
    db.Column('country_id', db.Integer, db.ForeignKey('country.id')),
    db.Column('panel_provider_id', db.Integer, db.ForeignKey('panel_provider.id')))


TargetGroup = db.Table('location_group',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('name', db.String(120), index=True, unique=True),
    db.Column('external_id', db.Integer, db.ForeignKey('country.id')),
    db.Column('parent_id', db.Integer, db.ForeignKey('panel_provider.id')),
    db.Column('secret_code', db.Integer, db.ForeignKey('location.secret_code')),
    db.Column('panel_provider_id', db.Integer, db.ForeignKey('panel_provider.id')))


# class TargetGroup(db.Model):
#     __tablename__ = "target_group"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(120), index=True, unique=True)
#     external_id = db.Column(db.Integer, db.ForeignKey('panel_provider.id')
#     parent_id = db.Column(db.Integer, db.ForeignKey('target_group.id')
#     secret_code = db.Column(db.String(120), index=True, unique=True)
#     panel_provider_id = db.Column(db.Integer, db.ForeignKey('panel_provider.id')


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