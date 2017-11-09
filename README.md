# DummyDataWarehouse
### This sets up a dummy data warehouse with two little tables and data generated with Faker 
#### (which is pretty awesome!)

##### The layout is pretty simple
##### Database - DummyDataWarehouse

##### This is how it is spun up (pretty much the .sql contents, but feel free to inspect the content)

####
```
CREATE TABLE customerCreditCard(customerNumber INT(32), dateExpire VARCHAR(16), cardProvider VARCHAR(32), cardNumber VARCHAR(255), cvvNumber INT(16)) ;
 
CREATE TABLE customerContact (customerNumber INT(32), firstName VARCHAR(64), lastName VARCHAR(64), socialNumber VARCHAR(16), s    treetAddress VARCHAR(255), city VARCHAR(128), stateAbbr VARCHAR(8), zipPlus VARCHAR(16), phoneNumber VARCHAR(32)) ;
```
 
#### Faker scripts create dummy content
#### For the customer information
```
from faker import Faker
fake = Faker('en_US')

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

```
#### For the credit card information
####
```
from faker import Faker
fake = Faker('en_US')

for i in range(0,10000):
 print(i) ,
 print "," , fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y") ,
 print "," , fake.credit_card_provider(card_type=None) ,
 print "," , fake.credit_card_number(card_type=None) ,
 print "," , fake.credit_card_security_code(card_type=None)

```
#### Then the Faker (from here: faker.readthedocs.io) created files are pulled in. 
 
```
  LOAD DATA LOCAL INFILE 'creditcard.txt' INTO TABLE customerCreditCard COLUMNS TERMINATED BY ',';
  
  LOAD DATA LOCAL INFILE 'customer_contact.txt' INTO TABLE customerContact COLUMNS TERMINATED BY ',';
```
  
#### Then there will be two tables that look roughly like : 
#### 
```
  MariaDB [DummyDataWarehouse]> select * from customerCreditCard LIMIT 10;
+----------------+------------+-------------------------------+--------------------+-----------+
| customerNumber | dateExpire | cardProvider                  | cardNumber         | cvvNumber |
+----------------+------------+-------------------------------+--------------------+-----------+
|              0 |  06/22     |  Discover                     |  4702816372464661  |      9779 |
|              1 |  07/25     |  JCB 16 digit                 |  30277491622252    |       695 |
|              2 |  08/22     |  Voyager                      |  4522896619838214  |       975 |
|              3 |  10/20     |  Diners Club / Carte Blanche  |  180027408857493   |       748 |
|              4 |  09/21     |  VISA 13 digit                |  4332577509204     |       163 |
|              5 |  09/18     |  Diners Club / Carte Blanche  |  210033664740419   |       649 |
|              6 |  05/19     |  Diners Club / Carte Blanche  |  675907480809      |       556 |
|              7 |  04/20     |  American Express             |  3337643757264085  |       760 |
|              8 |  09/25     |  Discover                     |  3096098875516356  |       768 |
|              9 |  02/26     |  Diners Club / Carte Blanche  |  5114975137309642  |       603 |
+----------------+------------+-------------------------------+--------------------+-----------+
10 rows in set (0.00 sec)

MariaDB [DummyDataWarehouse]> select * from  customerContact LIMIT 10;
+----------------+-------------+------------+---------------+---------------------------------+----------------------+-----------+--------------+-----------    -----------+
| customerNumber | firstName   | lastName   | socialNumber  | streetAddress                   | city                 | stateAbbr | zipPlus      | phoneNumbe    r          |
+----------------+-------------+------------+---------------+---------------------------------+----------------------+-----------+--------------+-----------    -----------+
|              0 |  Brandy     |  Kelley    |  518-41-3998  |  83029 Stanley Mall             |  Robertport          |  LA       |  35523-3479  |  282-819-6    367x432    |
|              1 |  Joseph     |  Wright    |  146-71-5360  |  810 Brooke Expressway          |  East Nathanielfort  |  MH       |  58550-5242  |  +18(3)927    6766630    |
|              2 |  Joan       |  Hayes     |  303-93-4061  |  426 Heather Pike Apt. 335      |  Port Juliehaven     |  UT       |  72277-8064  |  1-586-690    -0244      |
|              3 |  Richard    |  Cardenas  |  276-44-1041  |  056 Susan Trafficway Apt. 611  |  Jeremybury          |  IA       |  51923-5197  |  186.246.7    536x84509  |
|              4 |  Laura      |  Bruce     |  227-79-3642  |  292 Murray Lock                |  Lake Maria          |  NH       |  61598-0290  |  774-694-8    863x7632   |
|              5 |  Joseph     |  Hughes    |  563-57-8254  |  547 Klein Parkways Apt. 744    |  Westbury            |  MT       |  93585-1345  |  (444)329-    9577x36317 |
|              6 |  Christy    |  Mayer     |  756-92-5533  |  5145 Louis Cliff               |  Mejiaton            |  MI       |  23263-0309  |  651.512.4    101x38571  |
|              7 |  David      |  Hill      |  559-89-6211  |  659 Cheryl Port Apt. 156       |  Lake Ashleyfort     |  AL       |  21676-9021  |  (539)170-    9675       |
|              8 |  Stephanie  |  Lee       |  857-67-7991  |  88172 Miller Plains Apt. 642   |  Lake Chad           |  GA       |  24557-2950  |  250-333-5    633x3125   |
|              9 |  Derek      |  Miller    |  070-57-3498  |  87918 Barbara Gateway          |  Marcusview          |  NE       |  79278-4587  |  +67(6)220    0364816    |
+----------------+-------------+------------+---------------+---------------------------------+----------------------+-----------+--------------+-----------    -----------+
#### 10 rows in set (0.00 sec)

  
```

#### Hope this helps someone needing to spin up a quick database. 
#### Any overlap with real names, credit card information, socials, and addresses is purely coincidental. 
  
