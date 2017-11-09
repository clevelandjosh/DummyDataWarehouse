from faker import Faker
fake = Faker('en_US')

# The number of records created is based on the range, this range creates 10,000 records. Adjust as needed.
for i in range(0,10000):
 print(i) ,
 print "," , fake.first_name() ,
 print "," , fake.last_name() ,
 print "," , fake.ssn() ,
 print "," , fake.street_address() ,
 print "," , fake.city() ,
 print "," , fake.state_abbr() ,
 print "," , fake.postalcode_plus4() ,
 print "," , fake.phone_number()
