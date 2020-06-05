from setup_database_and_table import Puppy,db

db.create_all() #CREATES ALL THE TABLES IN THE DATABASE or CONVERTING MODEL CLASS TO DATABASE


obj1=Puppy('Namisha',17)
obj2=Puppy('Monish',21)
print(obj1.id) #NONE
print(obj2.id) #NONE

db.session.add_all([obj1,obj2])

db.session.commit()

print(obj1.id)

print(obj2.id)