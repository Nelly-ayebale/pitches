import unittest
from app.models import Pitch, User
from app import db


class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username= 'James', email='ayebalenellyabi1606@gmail.com', bio= 'Hello I am James', profile_pic_path='app/static/photos', pass_secure= 'potato' )
        self.new_pitch = Pitch(user= self.user_James, title= 'password', category= 'businesspitch', pitch='A password managing app')
    
    # def tearDown(self):
    #     Pitch.query.delete()
    #     User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.user, self.user_James)
        self.assertEquals(self.new_pitch.title,'password')
        self.assertEquals(self.new_pitch.category,'businesspitch')
        self.assertEquals(self.new_pitch.pitch,'A password managing app')
    
    def test_save_pitches(self):
        self.new_pitch.save_pitches()
        self.assertTrue(len(Pitch.query.all())>0)
