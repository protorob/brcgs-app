import os

# define base directory of app
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	# key for CSF
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
   
	# sqlite database uri
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
 
	# sqlalchemy track modifications in sqlalchemy
	SQLALCHEMY_TRACK_MODIFICATIONS = False