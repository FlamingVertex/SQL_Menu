
import sqlite3



# =============================================================================
# def create_connection(path):
#     connection = None
#     try:
#         connection = sqlite3.connect(path)
#         print("Connection to SQLite DB successful")
#     except sqlite3.Error as e:
#         print(f"The error '{e}' occurred")
#     return connection
# =============================================================================

# create database file by specifying location
connection = sqlite3.connect(r"Insert your desired Database path Ex. \home\etc\Database.sqlite")
# initialize cursor object to interact with database
cur = connection.cursor()
 
cur.execute("""CREATE TABLE IF NOT EXISTS Cuisine( 
                cuisine_id INTEGER PRIMARY KEY NOT NULL, 
                cuisine TEXT NOT NULL UNIQUE
                )""")
                
connection.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS Course( 
                course_id INTEGER PRIMARY KEY NOT NULL, 
                course TEXT NOT NULL UNIQUE
                )""")
                
connection.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS Diet( 
                diet_id INTEGER PRIMARY KEY NOT NULL, 
                diet TEXT NOT NULL UNIQUE
                )""")
                
connection.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Method( 
                method_id INTEGER PRIMARY KEY NOT NULL, 
                method TEXT NOT NULL UNIQUE
                )""")
                
connection.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS Effort( 
                effort_id INTEGER PRIMARY KEY NOT NULL, 
                effort TEXT NOT NULL UNIQUE
                )""")
                
connection.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS RecipeImage( 
                image_id INTEGER PRIMARY KEY NOT NULL, 
                image BLOB
                )""")
                
connection.commit()

#Insert the default values
cur.execute('''INSERT INTO Cuisine (cuisine) VALUES(?)''',('%',))
connection.commit()
cur.execute('''INSERT INTO Course (course) VALUES(?)''',('%',))
connection.commit()
cur.execute('''INSERT INTO Diet (diet) VALUES(?)''',('%',))
connection.commit()
cur.execute('''INSERT INTO Method (method) VALUES(?)''',('%',))
connection.commit()
cur.execute('''INSERT INTO Effort (effort) VALUES(?)''',('%',))
connection.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS Recipe( 
                recipe_id INTEGER PRIMARY KEY NOT NULL, 
                recipe_name TEXT NOT NULL,
                recipe_url TEXT NOT NULL,
                recipe_notes TEXT,
                recipe_ingredients TEXT NOT NULL,
                recipe_instructions TEXT NOT NULL,
                date TEXT,
                cuisine_id INTEGER,
                course_id INTEGER,
                diet_id INTEGER,
                method_id INTEGER,
                effort_id INTEGER,
                image_id INTEGER,
                FOREIGN KEY (cuisine_id) REFERENCES Cuisine(cuisine_id),
                FOREIGN KEY (course_id) REFERENCES Course(course_id),
                FOREIGN KEY (diet_id) REFERENCES Diet(diet_id),
                FOREIGN KEY (image_id) REFERENCES RecipeImage(image_id),
                FOREIGN KEY (method_id) REFERENCES Method(method_id),
                FOREIGN KEY (effort_id) REFERENCES Effort(effort_id)
                )""")
#
                
connection.commit()

# 
# =============================================================================

connection.close()

# =============================================================================
#                 
#                 
#                 
#                 
# =============================================================================
