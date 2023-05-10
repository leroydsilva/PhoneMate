# Create tables.
# Base.metadata.create_all(bind=engine)
# from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine, and_
from sqlalchemy import and_
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from decouple import config
db=SQLAlchemy()

# create an engine object to connect to the database
url = config('SQLALCHEMY_DATABASE_URI')
engine = db.create_engine(url)

# metadata = MetaData()


# Reflect the existing database schema
# phone_table = Table('phone', db.metadata,autoload_with=engine)
# ratings_table = Table('ratings', db.metadata,autoload_with=engine)
# specs_table = Table('specs', db.metadata,autoload_with=engine)


Base = automap_base()
Base.prepare(engine,reflect=True)
Phone= Base.classes.phone
Specs= Base.classes.specs
Ratings= Base.classes.ratings
# Create the table objects from the reflected schema
# class PhoneFetch(db.Model):
#     # __table__ = phone_table
#     # Ratings = db.relationship("Ratings", uselist=False, backref="phone", primaryjoin='Phone.Phone_id == Ratings.Phone_id')
#     # Specs = db.relationship("Specs", uselist=False, backref="phone", primaryjoin='Phone.Phone_id == Specs.Phone_id')

#     @staticmethod
def get_phones(args):
    camera = args['Camera']
    storage = args['Storage']
    usage = args['Usage']
    game = args['Game']
    display = args['Display']
    protection = args['Protection']
    try:
        phone_query = (
            db.session.query(Phone.Phone_id, Phone.Phone_name, Phone.Phone_price, Phone.Phone_img,Specs.Screen_size,
            Specs.RAM,Specs.Internal_storage,Specs.Processor,Specs.Rear_camera,Specs.Front_camera, Specs.Battery_capacity,
            Specs.fiveg, Ratings.Value_for_Money)
            .join(Ratings, Phone.Phone_name == Ratings.Phone_name)
            .join(Specs, Phone.Phone_name == Specs.Phone_name)
            .filter(and_(
                Ratings.Camera > (7 if camera else 6),
                Specs.Internal_storage.like('%128GB%') if storage else True,
                Ratings.Battery_Life > 8 if usage else True,
                Specs.Battery_capacity > 4000 if usage else True,
                (
                    Specs.RAM.like('%12GB%')
                    | Specs.RAM.like('%8GB%')
                    | Specs.Processor_make.like('%Apple%')
                ) if game else True,
                Specs.Refresh_Rate > 80 if game else True,
                Ratings.Performance > 8 if game else True,
                Ratings.Display > 8 if display else Ratings.Display > 6,
                Ratings.Design > 8 if protection else True,
            ))
        )
        phones = phone_query.all()
        return phones
    except Exception as e:
        print('below exception occured',e)
        

    
    
# class Ratings(db.Model):
#     __table__ = ratings_table
#     # phone_id = Column(Integer, ForeignKey('phone.Phone_id'))
#     # phone_name = Column(String(100), ForeignKey('phone.Phone_name'))
#     phone = db.relationship("Phone", back_populates="ratings")

# class Specs(db.Model):
#     __table__ = specs_table
#     phone = db.relationship("Phone", back_populates="specs")
    # phone_id = Column(Integer, ForeignKey('phone.Phone_id'))
    # phone_name = Column(String(100), ForeignKey('phone.Phone_name'))


