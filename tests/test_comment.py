import unittest
from app.models import Comment,Pitch, User
from app import db

class TestComment(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch(title= 'password', category= 'businesspitch', pitch='A password managing app')
        self.new_comment= Comment(comment='Good one',pitch= self.new_pitch)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Good one')
        self.assertEquals(self.new_comment.pitch, self.new_pitch)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_pitch_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(self.new_pitch.id)
        self.assertTrue(len(got_comments)==1)
        
    
