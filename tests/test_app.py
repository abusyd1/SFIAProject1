#!/usr/bin/python3

import unittest
from flask_testing import TestCase
from flask import url_for

from application import app, db
from application.models import Parent, Player

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///")
        app.config['SECRET_KEY'] = "testingtesting"
        return app
    def setUp(self):
        db.drop_all()
        db.create_all()

        testteam1=Parent(name="testteam1", league="testleague")
        testteam2=Parent(name="testteam2", league="testleague")
        testteam3=Parent(name="testteam3", league="testleague")

        db.session.add(testteam1)
        db.session.add(testteam2)
        db.session.add(testteam3)

        db.session.commit()

        db.session.add_all([
            Player(name="testplayer1", age="15", position="Defender", team=testteam1),
            Player(name="testplayer2", age="16", position="Midfielder", team=testteam2),
            Player(name="testplayer3", age="17", position="Forward", team=testteam3)])
        db.session.commit()

    def tearDown(self):
        db.drop_all()

class TestAccess(TestBase):
    def test_access_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    def test_access_parent(self):
        response=self.client.get(url_for('parent', id=1))
        self.assertEqual(response.status_code, 200)

    def test_access_player(self):
        response=self.client.get(url_for('player', id=1))
        self.assertEqual(response.status_code, 200)

    def test_find_parent(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b'testteam1', response.data)

    def test_find_player(self):
        response=self.client.get(url_for('parent', id=1))
        self.assertIn(b'testplayer1', response.data)

class TestAdding(TestBase):
    def test_add_parent(self):
        response = self.client.post(url_for('add'), data=dict(name="testaddteam"))
        self.assertIn(b'testaddteam', response.data)

class TestUpdate(TestBase):
    def test_update_player(self):
        response = self.client.post(url_for('edit', parent_id=1, id=1), data=dict(name="hello"))
        self.assertIn(b'hello', response.data)

class TestDelete(TestBase):
    def test_delete_player(self):
        response=self.client.get(url_for('delete', parent_id=1, id=1), data=dict(name="testplayer1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestModels(TestBase):
    def test_parent_model(self):
        self.assertEqual(Parent.query.count(), 3)

    def test_player_model(self):
        self.assertEqual(Player.query.count(), 3)


