import unittest

from flask import abort, url_for
from flask_testing import TestCase

from application import app, db 
from application.models import Users, Posts

class TestBase(TestCase):

    def create_app(self):

        config_name = 'testing'
        app.config.update(
            SQLACHEMY_DATABASE_URI='mysql+pymysql://root:root@35.230.155.181/flask_test')
        return app

    def setUp(self):

        db.session.commit()
        db.drop_all()
        db.create_all()

        admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password="admin2016")

        employee = Users(first_name="test", last_name="user", email="test@user.com", password="test2016")

        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    