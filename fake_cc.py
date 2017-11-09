from faker import Faker
fake = Faker('en_US')

# This will create 10,000 records, adjust the range to adjust the size of the dataset

for i in range(0,10000):
 print(i) ,
 print "," , fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y") ,
 print "," , fake.credit_card_provider(card_type=None) ,
 print "," , fake.credit_card_number(card_type=None) ,
 print "," , fake.credit_card_security_code(card_type=None)
