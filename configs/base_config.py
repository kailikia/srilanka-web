import secrets
import os

class Base:
    FLASK_APP = os.environ.get("FLASK_APP")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = secrets.token_hex(16)

class Development(Base):
    FLASK_ENV= os.environ.get("FLASK_ENV")
    SQLALCHEMY_DATABASE_URI= os.environ.get("SQLALCHEMY_DATABASE_URI")

class Staging(Base):
    DATABASE = "d3jbjhi84rcjka"
    POSTGRES_USER = "vheobwrimkhkic"
    POSTGRES_PASSWORD = "4474c1376841e6f99b13e75c35727e2b69f046cd349cb4f954ffd75fa8ac4e4e"
    SQLALCHEMY_DATABASE_URI="postgres://vheobwrimkhkic:4474c1376841e6f99b13e75c35727e2b69f046cd349cb4f954ffd75fa8ac4e4e@ec2-34-254-69-72.eu-west-1.compute.amazonaws.com:5432/d3jbjhi84rcjka"
    # pass

class Production(Base):
<<<<<<< HEAD
    DATABASE = "d5vu3rta2gc2pj"
    POSTGRES_USER = "aavksirdpafume"
    POSTGRES_PASSWORD = "bfe61ebc69c77fa949238ff77a514b02cd5e0bbb3d1f3dd143b49f09f1e2006f"
    SQLALCHEMY_DATABASE_URI="postgres://aavksirdpafume:bfe61ebc69c77fa949238ff77a514b02cd5e0bbb3d1f3dd143b49f09f1e2006f@ec2-54-217-236-206.eu-west-1.compute.amazonaws.com:5432/d5vu3rta2gc2pj"
=======
    DATABASE = "decnc6o0b2c4i4"
    POSTGRES_USER = "fukakokzsluroc"
    POSTGRES_PASSWORD = "c2fdf5b6ed6c59d99fdcd13032a6fa38ed4173c78fe8d5a5953e1f17ee2fad59"
    SQLALCHEMY_DATABASE_URI="postgresql://fukakokzsluroc:c2fdf5b6ed6c59d99fdcd13032a6fa38ed4173c78fe8d5a5953e1f17ee2fad59@ec2-3-214-136-47.compute-1.amazonaws.com:5432/decnc6o0b2c4i4"
>>>>>>> 6ba8ea3420104dae0300e21e731c1b28e624f8bb
