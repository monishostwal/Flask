from setup_database_and_table import db,Puppy


############################################################ CREATE ###################################################################
puppy1=Puppy('Ayush',22)
db.session.add(puppy1)
db.session.commit()

print(puppy1.id)

############################################################## READ ######################################################################


# Reading all puppies
all_puppies=Puppy.query.all() 
print(all_puppies)
 # Select by id
puppy_5=Puppy.query.get(5)
print(puppy_5)

# Selecting by filter
puppy_monish=Puppy.query.filter_by(name='Monish')
print(puppy_monish.all())


############################################################ UPDATE ###################################################################
puppy_1=Puppy.query.get(1)
puppy_1.age=100
db.session.add(puppy_1)
db.session.commit()
############################################################ DELETE ###################################################################

second_puppy=Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()


############################################################ Viewing ###################################################################

print('--------------------------------------------------------------------------------------------------------------------')
all_puppies=Puppy.query.all()
print(all_puppies)