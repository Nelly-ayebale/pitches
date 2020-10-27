import unittest
from app.models import Upvote, Pitch
from app import db


class TestUpvote(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch(title= 'password', category= 'businesspitch', pitch='A password managing app')
        self.new_upvote = Upvote(pitch=self.new_pitch)
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_upvote.pitch, self.new_pitch)
    
    def test_save_upvote(self):
        self.new_upvote.save_upvotes()
        self.assertTrue(len(Upvote.query.all())>0)
    
    def test_get_upvote_by_pitch_id(self):
        self.new_upvote.save_upvotes()
        got_upvotes = Upvote.get_upvotes(self.new_pitch.id)
        self.assertTrue(len(got_upvotes)==1)


