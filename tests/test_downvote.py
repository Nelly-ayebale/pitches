import unittest
from app.models import Downvote, Pitch
from app import db


class TestDownvote(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch(title= 'password', category= 'businesspitch', pitch='A password managing app')
        self.new_downvote = Downvote(pitch=self.new_pitch)
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_downvote.pitch, self.new_pitch)
    
    def test_save_downvote(self):
        self.new_downvote.save_downvotes()
        self.assertTrue(len(Downvote.query.all())>0)
    
    def test_get_downvote_by_pitch_id(self):
        self.new_downvote.save_downvotes()
        got_downvotes = Downvote.get_downvotes(self.new_pitch.id)
        self.assertTrue(len(got_downvotes)==1)


