import pymysql
import os
from dotenv import load_dotenv

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

load_dotenv()

db = pymysql.connect(
    host = os.getenv("MYSQL_ADDON_HOST"),
    user = os.getenv("MYSQL_ADDON_USER"),
    password = os.getenv("MYSQL_ADDON_PASSWORD"),
    database=os.getenv("MYSQL_ADDON_DB")
)

mycursor = db.cursor()

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

mycursor.execute('''
    create table people (
    	secret_sentence varchar(100) primary key,
        name varchar(100) not null,
        age int not null,
        email varchar(100) not null,
        gender enum("male", "female", "others") not null
    );
''')

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

mycursor.execute('''
        create table scores (
    	secret_sentence varchar(100),
    	date DATETIME not null,
    	topic varchar(200) not null,
    	dificulty enum("mixed", "easy", "medium", "hard") not null,
    	score int not null
    );
''')

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

mycursor.execute('''
        create table charts (
    	date DATETIME not null,
    	topic varchar(200) not null,
    	dificulty enum("mixed", "easy", "medium", "hard") not null,
    	score int not null
    );
''')