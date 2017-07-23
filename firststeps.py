from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,String,Integer

# step 1  create an engine that defines the db location
engine = create_engine('sqlite:///:memory:', echo=False)


# step 2 base as declarative base
Base = declarative_base()

# step 3 create the class with required columns
class User(Base):
    __tablename__='users'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    # to specify the result format when read from the database
    def __repr__(self):
        return "<User(name={},fullname={},password={})>".format(self.name,self.fullname,self.password)

# step 4 run the Base.metadata to create all the tables
Base.metadata.create_all(engine)

# intialize session with engine
Session = sessionmaker(bind=engine)
# create a class instance with the class returned with sessionmaker
session = Session( )

# create a record of the class instance
ed_user = User(name='ed',fullname='Ed jones',password='edspassword')

# add the data using session.add
session.add(ed_user)

# add multiple data
session.add_all([
 User(name='wendy', fullname='Wendy Williams', password='foobar'),
 User(name='mary', fullname='Mary Contrary', password='xxg527'),
 User(name='fred', fullname='Fred Flinstone', password='blah')])
print(session.new)

# query the database
our_user = session.query(User).filter_by(name='mary').first()
ed_user.password = 'securepassword'



print(session.dirty)

session.commit()
print(our_user.id)

for instance in session.query(User).order_by(User.id):
    print (" id is {} and username is {}".format(instance.id,instance.fullname))






























































