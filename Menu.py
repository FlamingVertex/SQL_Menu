#import libraries
import sqlite3
from recipe_scrapers import scrape_me
import tkinter as tk
from tkinter import filedialog
import datetime
import os.path

# =============================================================================
#Connect to SQLITE3 database
SQL_Path = "Insert your desired Database path Ex. \home\etc\Database.sqlite"

def ChangeDbPath(dbPath,Window):
	global SQL_Path
	def CloseOnError(Window):
		Window.destroy()
		
	dbPath= dbPath[:-1]
	Window.destroy()
	if (os.path.exists(dbPath)):
		connection = sqlite3.connect(dbPath)
		cur = connection.cursor()
		print("Connected. Please update program with following path:")
		print(dbPath)
		connection.close()
		SQL_Path = dbPath
		CreateMain()
	else:
		Root = tk.Tk()
		Root.rowconfigure(0, weight=0)
		Root.columnconfigure(0, weight=0)
		Root.title("Database Error")
		Root.minsize(400,40)
		F2 = tk.Frame(Root)
	
		DB_Prompt = tk.Label(F2, text = "Still could not file database. Check Path\Existence. Update program.",bg='sky blue', fg='white')
		DB_Prompt.grid(row=0,column=0, sticky = "nsew") 
	
	
		btn_Change = tk.Button(F2, text="Quit Programs", highlightbackground="goldenrod", activebackground='red2',command=lambda: CloseOnError(Root))
		btn_Change.grid(row=2, column=0, sticky="nsew")
	
		F2.rowconfigure([0,1], weight=0)
		F2.columnconfigure(0,weight=0)

		F2.grid(row=0,column=0,sticky="nsew")
		Root.mainloop()

#Functions to Add/Remove options from columns
def AddCuisine(word,Window):
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	if word and not word.isspace():
		cur.execute('''INSERT INTO Cuisine (cuisine) VALUES(?)''',(word,))
		connection.commit()
		connection.close()
		print(word+ ' Added')
	Window.destroy()
	CreateMain()
	
def RemCuisine(word,Window):
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	#Check to see if cuisine is in cuisine table
	cur.execute('''SELECT cuisine_id FROM Cuisine WHERE cuisine=?''',(word,))
	data= cur.fetchone()
	if data is None:
		print('There is no cuisine named %s'%word)
	else:
		#If cuisine is in cuisine table replace the cuisine in Recipe table with default value
		cur.execute('''UPDATE Recipe SET cuisine_id = REPLACE (cuisine_id,?,1)''',(data[0],))
		#print('Component %s found with id %s'%(word,data[0]))
		#Delete cuisine from Cuisine table
		cur.execute('''DELETE FROM Cuisine WHERE cuisine = ?''',(word,))
		connection.commit()
		connection.close()
		print(word+ ' Removed')
	Window.destroy()
	CreateMain()
	
def AddCourse(word, Window):
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	if word and not word.isspace():
		cur.execute('''INSERT INTO Course (course) VALUES(?)''',(word,))
		connection.commit()
		connection.close()
		print(word+ ' Added')
	Window.destroy()
	CreateMain()
	
def RemCourse(word, Window):
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	cur.execute('''SELECT course_id FROM Course WHERE course=?''',(word,))
	data= cur.fetchone()
	if data is None:
		print('There is no course named %s'%word)
	else:
		cur.execute('''UPDATE Recipe SET course_id = REPLACE (course_id,?,1)''',(data[0],))
		#print('Component %s found with id %s'%(word,data[0]))
		cur.execute('''DELETE FROM Course WHERE course = ?''',(word,))
		connection.commit()
		connection.close()
		print(word+ ' Removed')
	Window.destroy()
	CreateMain()
	
def AddDiet(word, Window):
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	if word and not word.isspace():
		cur.execute('''INSERT INTO Diet (diet) VALUES(?)''',(word,))
		connection.commit()
		connection.close()
		print(word+ ' Added')
	Window.destroy()
	CreateMain()
	
def RemDiet(word, Window):
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	cur.execute('''SELECT diet_id FROM Diet WHERE diet=?''',(word,))
	data= cur.fetchone()
	if data is None:
		print('There is no diet named %s'%word)
	else:
		cur.execute('''UPDATE Recipe SET diet_id = REPLACE (diet_id,?,1)''',(data[0],))
		#print('Component %s found with id %s'%(word,data[0]))
		cur.execute('''DELETE FROM Diet WHERE diet = ?''',(word,))
		connection.commit()
		connection.close()
		print(word+ ' Removed')
	Window.destroy()
	CreateMain()
	
def AddMethod(word, Window):
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	if word and not word.isspace():
		cur.execute('''INSERT INTO Method (method) VALUES(?)''',(word,))
		connection.commit()
		connection.close()
		print(word+ ' Added')
	Window.destroy()
	CreateMain()
	
def RemMethod(word, Window):
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	cur.execute('''SELECT method_id FROM Method WHERE method=?''',(word,))
	data= cur.fetchone()
	if data is None:
		print('There is no method named %s'%word)
	else:
		cur.execute('''UPDATE Recipe SET method_id = REPLACE (method_id,?,1)''',(data[0],))
		#print('Component %s found with id %s'%(word,data[0]))
		cur.execute('''DELETE FROM Method WHERE method= ?''',(word,))
		connection.commit()
		connection.close()
		print(word+ ' Removed')
	Window.destroy()
	CreateMain()
	

def AddEffort(word, Window):
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	if word and not word.isspace():
		cur.execute('''INSERT INTO Effort (effort) VALUES(?)''',(word,))
		connection.commit()
		connection.close()
		print(word+ ' Added')
	Window.destroy()
	CreateMain()
	
def RemEffort(word, Window):
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	cur.execute('''SELECT effort_id FROM Effort WHERE effort=?''',(word,))
	data= cur.fetchone()
	if data is None:
		print('There is no effort named %s'%word)
	else:
		cur.execute('''UPDATE Recipe SET effort_id = REPLACE (effort_id,?,1)''',(data[0],))
		#print('Component %s found with id %s'%(word,data[0]))
		cur.execute('''DELETE FROM Effort WHERE effort = ?''',(word,))
		connection.commit()
		connection.close()
		print(word+ ' Removed')
	Window.destroy()
	CreateMain()
	
def UploadAction():
	UploadAction.PicPath = filedialog.askopenfilename()
	print(UploadAction.PicPath)


def convertToBinaryData(PicPath):
	# Convert digital data to binary format
	with open(PicPath, 'rb') as file:
		blobData = file.read()
	return blobData
#Initialize PicPath incase there is no call to function
UploadAction.PicPath = None
  
def saveImage(Data):
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	cur.execute('''INSERT INTO RecipeImage (image) VALUES (?) ''',(Data,))
	connection.commit()
	ID = cur.execute('select image_id from RecipeImage WHERE image = ?',(Data,)).fetchone()
	connection.close()
	#Tuple is returned and only need integer
	return ID[0]
            
#Initiate recipe scrapper and popup window if success. Errors will appear in terminal window     
def SearchRecipe(RecipeURL, WildStatus, CuisineVal, CuisineDB, CourseVal, CourseDB, DietVal, DietDB, MethodVal, MethodDB, EffortVal, EffortDB, NotesInput):

    #Creates SQL command to add data to SQL
	def AddRecipe():
		connection = sqlite3.connect(SQL_Path)
		cur = connection.cursor()
		if UploadAction.PicPath == None:
			ImageId = None
		else:
			ImageData = convertToBinaryData(UploadAction.PicPath)
			ImageId = saveImage(ImageData)

		#get ["1.0"] means starting at line 1 and character 0 and tk.END always includes newline character added at the end
		NotesInput = Notes.get("1.0",tk.END)
		IngrInput = Ingr.get("1.0",tk.END)
		InstrInput = Instr.get("1.0",tk.END)
		TitleInput = Title.get("1.0",tk.END)
		#The [:-1] is to remove the newline character added by the tkinter text widget
		RecipeInput = [TitleInput[:-1], str(RecipeURL), NotesInput[:-1], IngrInput[:-1], InstrInput[:-1], DateInput[:-1], str("".join(CuisineInput)), str("".join(CourseInput)), str("".join(DietInput)), str("".join(MethodInput)),str("".join(EffortInput)),ImageId]
        
# =============================================================================
#         print(str("".join(CuisineInput)))
#         print(type("".join(CuisineInput)))
#         print("".join(CuisineInput)+"hello")
# =============================================================================
		cur.execute('''INSERT INTO Recipe (recipe_name, recipe_url, recipe_notes, recipe_ingredients, recipe_instructions, date, cuisine_id, course_id, diet_id, method_id, effort_id, image_id) VALUES (?,?,?,?,?,?,(SELECT cuisine_id FROM Cuisine WHERE cuisine = ?),(SELECT course_id FROM Course WHERE course = ?),(SELECT diet_id FROM Diet WHERE diet = ?),(SELECT method_id FROM Method WHERE method = ?),(SELECT effort_id FROM Effort WHERE effort = ?),?);''', RecipeInput);

		connection.commit()
		connection.close()
		print(TitleInput[:-1]+": Added")
		#Clean out old file path 
		UploadAction.PicPath = None
		PopUp.destroy()
        
    #RecipeURL= ent_url.get()
    #WildStatus = int(read_wild.get())
    #CuisineVal = int(read_cuisine.get())
    #CourseVal = int(read_course.get())
    #DietVal = int(read_diet.get())
    #MethodVal = int(read_method.get())
    #EffortVal = int(read_effort.get())
    
    #NotesInput = "-"+read_notes.get()
	DateInput = datetime.date.today().strftime('%m/%d/%y')
	CuisineInput = CuisineDB[CuisineVal]
	CourseInput = CourseDB[CourseVal]
	DietInput = DietDB[DietVal]
	MethodInput = MethodDB[MethodVal]
	EffortInput = EffortDB[EffortVal]	

	#Attempt to use scrapper if it errors toggle switch
	if WildStatus==0:
		try:
			scraper = scrape_me(RecipeURL, wild_mode=False)
			ScrapperFail = 0
		except:
			ScrapperFail = 1
	else:
		try:
			scraper = scrape_me(RecipeURL, wild_mode=True)
			ScrapperFail = 0
		except:
			ScrapperFail = 1
	#If scrapper fails fill data with blank and move to manual entry
	if ScrapperFail == 1:
		ScrapTitle = ""
		ScrapIngr = ""
		ScrapInstr = ""
	else:
		ScrapTitle = scraper.title()
		ScrapIngr = scraper.ingredients()
		ScrapInstr = scraper.instructions()
    
    
	PopUp = tk.Tk()

	PopUp.rowconfigure(0, weight=1)
	PopUp.columnconfigure(0, weight=1)
	PopUp.title("Preview Input")
	PopUp.minsize(720,400)
	g1 = tk.Frame(PopUp)
	label_title = tk.Label(g1, text = "Recipe Name",bg='sky blue', fg='white')
	label_title.grid(row=0,column=0, sticky = "nsew")
	Title = tk.Text(g1, height= 1,bg='bisque2')
	Title.insert(tk.INSERT, ScrapTitle)
	Title.grid(row=0,column=1, sticky = "nsew")

	label_Ingr = tk.Label(g1, text = "Ingredients",bg='sky blue', fg='white')
	label_Ingr.grid(row=1,column=0, sticky = "nsew")
	Ingr = tk.Text(g1,height =10)
	Ingr.insert(tk.INSERT, ScrapIngr)
	Ingr.grid(row=1,column=1, sticky = "nsew")

	label_Instr = tk.Label(g1, text = "Instructions",bg='sky blue', fg='white')
	label_Instr.grid(row=2,column=0, sticky = "nsew")
	Instr = tk.Text(g1,height =10)
	Instr.insert(tk.INSERT, ScrapInstr)
	Instr.grid(row=2,column=1, sticky = "nsew")

	label_Cui = tk.Label(g1, text = "Cuisine",bg='sky blue', fg='white')
	label_Cui.grid(row=3,column=0, sticky = "nsew")
	label_Cui2 = tk.Label(g1, text = str("".join(CuisineInput)),justify="left")
	label_Cui2.grid(row=3,column=1, sticky = "nsw")

	label_Cou = tk.Label(g1, text = "Course",bg='sky blue', fg='white')
	label_Cou.grid(row=4,column=0, sticky = "nsew")
	label_Cou2 = tk.Label(g1, text = str("".join(CourseInput)), justify="left")
	label_Cou2.grid(row=4,column=1, sticky = "nsw")

	label_Die = tk.Label(g1, text = "Diet",bg='sky blue', fg='white')
	label_Die.grid(row=5,column=0, sticky = "nsew")
	label_Die2 = tk.Label(g1, text = str("".join(DietInput)), justify="left")
	label_Die2.grid(row=5,column=1, sticky = "nsw")

	label_Meth = tk.Label(g1, text = "Method",bg='sky blue', fg='white')
	label_Meth.grid(row=6,column=0, sticky = "nsew")
	label_Meth2 = tk.Label(g1, text = str("".join(MethodInput)), justify="left")
	label_Meth2.grid(row=6,column=1, sticky = "nsw")

	label_Eff = tk.Label(g1, text = "Effort",bg='sky blue', fg='white')
	label_Eff.grid(row=7,column=0, sticky = "nsew")
	label_Eff2 = tk.Label(g1, text = str("".join(EffortInput)), justify="left")
	label_Eff2.grid(row=7,column=1, sticky = "nsw")

	label_PicPath = tk.Label(g1, text = "Picture",bg='sky blue', fg='white')
	label_PicPath.grid(row=8,column=0, sticky = "nsew")
	label_PicPath2 = tk.Label(g1, text = str(UploadAction.PicPath), justify="left")
	label_PicPath2.grid(row=8,column=1, sticky = "nsw")   

	label_Not = tk.Label(g1, text = "Notes",bg='sky blue', fg='white')
	label_Not.grid(row=9,column=0, sticky = "nsew")
	Notes = tk.Text(g1, height =3)
	Notes.insert(tk.INSERT,NotesInput)
	Notes.grid(row=9,column=1, sticky = "nsew")
    
	btn_Confirm = tk.Button(g1, text="Submit To Database", activebackground='pale green', command=AddRecipe)
	btn_Confirm.grid(row=10, column=0,columnspan=2, pady=10, sticky="nsew")
	g1.rowconfigure(0, weight=0)
	g1.rowconfigure(1, weight=1)
	g1.rowconfigure(2, weight=2)
	g1.rowconfigure(3, weight=0)
	g1.rowconfigure(4, weight=0)
	g1.columnconfigure(0,weight=0)
	g1.columnconfigure(1,weight=1)
	g1.grid(row=0,column=0,sticky="nsew")

	

	PopUp.mainloop()


def CreateMain():
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	#Start of the actual program not in functions
	#Create tkinter window called scrape recipe
	MainWindow = tk.Tk()
	w = 720 # width for the Tk root
	h = 400 # height for the Tk root
	MainWindow.minsize(w,h) #May need to increase if start up window is too small compared to columns
	MainWindow.title("Scrape Recipe")
	#Centers tkinter window
	# get screen width and height
	ws = MainWindow.winfo_screenwidth() # width of the screen
	hs = MainWindow.winfo_screenheight() # height of the screen
	# calculate x and y coordinates for the Tk root window
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	# set the dimensions of the screen 
	# and where it is placed
	MainWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

	MainWindow.rowconfigure(0, weight=1)
	MainWindow.columnconfigure(0,weight=1)

	#Row 1
	Main_R1 = tk.Frame(MainWindow)

	#URL Box
	label_url = tk.Label(Main_R1,text="Recipe URL", bg="sky blue", fg="white")
	label_url.grid(row=0, column=0, columnspan=1, sticky="nsew")
	#Create "Tkinter variable" in MainWindow and set default value to Enter Recipe URL
	read_url = tk.StringVar(MainWindow)
	ent_url = tk.Entry(Main_R1, textvariable= read_url, width = 50,bg="white", fg="black")
	ent_url.grid(row=1, rowspan=2, column=0, columnspan =1,sticky="nsew")

	#Wild Mode Box
	label_wild = tk.Label(Main_R1,text="Wild Mode", bg="sky blue", fg="white")
	label_wild.grid(row=0, column=1,columnspan=1, sticky="nsew")
	#Create "Tkinter variable" in MainWindow and set default value to 0 
	read_wild= tk.IntVar(MainWindow,0)
	#read_wild.set(0)
	tk.Radiobutton(Main_R1, text="OFF",padx = 10, variable=read_wild, value=0).grid(row=1,column=1,columnspan=1, sticky="w")
	tk.Radiobutton(Main_R1, text="ON",padx = 10, variable=read_wild, value=1).grid(row=2,column=1, columnspan=1, sticky="w")

	Main_R1.grid_rowconfigure([0,1,2], weight=0)
	Main_R1.grid_columnconfigure(0, weight=1)
	Main_R1.grid_columnconfigure(1, weight=0)

	Main_R1.grid(row=0, column=0,columnspan = 10,sticky = "nsew")

	#Row 2
	Main_R2 = tk.Frame(MainWindow)
	#Create Header for each Attribute
	label_Cuisine = tk.Label(Main_R2,text="Cuisine", width= 12,bg="sky blue", fg="white")
	label_Cuisine.grid(row=0, column=0,columnspan=2,sticky="nsew")
	label_Course = tk.Label(Main_R2,text="Course",width= 12, bg="sky blue", fg="white")
	label_Course.grid(row=0, column=2,columnspan=2,sticky="nsew")
	label_Diet = tk.Label(Main_R2,text="Diet",width= 12, bg="sky blue", fg="white")
	label_Diet.grid(row=0, column=4,columnspan=2,sticky="nsew")
	label_Method = tk.Label(Main_R2,text="Method",width= 12, bg="sky blue", fg="white")
	label_Method.grid(row=0, column=6,columnspan=2,sticky="nsew")
	label_Effort = tk.Label(Main_R2,text="Effort",width= 12, bg="sky blue", fg="white")
	label_Effort.grid(row=0, column=8,columnspan=2,sticky="nsew")


	#Read options from sql
	read_cuisine = tk.IntVar(MainWindow,0)
	CuisineDB = cur.execute('select cuisine from Cuisine').fetchall()
	CuisineDB.sort()
	for name in CuisineDB:  
		#Row CuisineDB.index(name)+1 because header is row 0
		tk.Radiobutton(Main_R2, text = name[0], variable = read_cuisine,value = CuisineDB.index(name)).grid(row=CuisineDB.index(name)+1,column=0,columnspan=2,sticky ="W") 

	read_course = tk.IntVar(MainWindow,0)
	CourseDB = cur.execute('select course from Course').fetchall()
	CourseDB.sort()
	for name in CourseDB:  
	    	tk.Radiobutton(Main_R2, text = name[0], variable = read_course, value = CourseDB.index(name)).grid(row=CourseDB.index(name)+1, column=2, columnspan=2,sticky ="W") 

	read_diet = tk.IntVar(MainWindow,0)
	DietDB = cur.execute('select diet from Diet').fetchall()
	DietDB.sort()
	for name in DietDB:  
	    	tk.Radiobutton(Main_R2, text = name[0], variable = read_diet,value = DietDB.index(name)).grid(row=DietDB.index(name)+1, column=4, columnspan=2,sticky ="W") 

	read_method = tk.IntVar(MainWindow,0)
	MethodDB = cur.execute('select method from Method').fetchall()
	MethodDB.sort()
	for name in MethodDB:  
		tk.Radiobutton(Main_R2, text = name[0], variable = read_method,value = MethodDB.index(name)).grid(row=MethodDB.index(name)+1, column=6, columnspan=2,sticky ="W") 

	read_effort = tk.IntVar(MainWindow,0)
	EffortDB = cur.execute('select effort from Effort').fetchall()
	EffortDB.sort()
	for name in EffortDB:  
	    	tk.Radiobutton(Main_R2, text = name[0], variable = read_effort, value = EffortDB.index(name)).grid(row=EffortDB.index(name)+1, column=8, columnspan=2,sticky ="W") 

	Main_R2.grid_rowconfigure(0, weight=1)
	#Making all columns resize the same to keep things looking pretty
	Main_R2.grid_columnconfigure([0,1,2,3,4,5,6,7,8,9], weight=1)
	
	Main_R2.grid(row =1,column = 0,columnspan = 10,sticky = "nsew")

	#Row 3

	Main_R3 = tk.Frame(MainWindow)
	label_Cuisine = tk.Label(Main_R3,text="Cuisine", width= 12,bg="sky blue", fg="white")
	label_Cuisine.grid(row=0, column=0,columnspan=2,sticky="nsew")
	label_Course = tk.Label(Main_R3,text="Course",width= 12, bg="sky blue", fg="white")
	label_Course.grid(row=0, column=2,columnspan=2,sticky="nsew")
	label_Diet = tk.Label(Main_R3,text="Diet",width= 12, bg="sky blue", fg="white")
	label_Diet.grid(row=0, column=4,columnspan=2,sticky="nsew")
	label_Method = tk.Label(Main_R3,text="Method",width= 12, bg="sky blue", fg="white")
	label_Method.grid(row=0, column=6,columnspan=2,sticky="nsew")
	label_Effort = tk.Label(Main_R3,text="Effort",width= 12, bg="sky blue", fg="white")
	label_Effort.grid(row=0, column=8,columnspan=2,sticky="nsew")

	ent_Cuisine = tk.Entry(Main_R3, width=10)
	ent_Cuisine.grid(row=1, column=0,columnspan=2, sticky="nsew")
	#instead of lambda can use partial from library functools as alternative
	btn_RemCuisine = tk.Button(Main_R3, text="Remove", highlightbackground="goldenrod", activebackground='light blue', command=lambda: RemCuisine(ent_Cuisine.get(),MainWindow))
	btn_RemCuisine.grid(row=2, column=0, pady=10, sticky="nsew")
	btn_AddCuisine = tk.Button(Main_R3, text="Add", highlightbackground="goldenrod", activebackground='light blue',command=lambda: AddCuisine(ent_Cuisine.get(),MainWindow))
	btn_AddCuisine.grid(row=2, column=1, pady=10, sticky="nsew")
		
	ent_Course = tk.Entry(Main_R3, width=10)
	ent_Course.grid(row=1, column=2, columnspan=2, sticky="nsew")
	btn_RemCourse = tk.Button(Main_R3, text="Remove",highlightbackground="goldenrod", activebackground='light blue', command=lambda: RemCourse(ent_Course.get(),MainWindow))
	btn_RemCourse.grid(row=2, column=2, pady=10, sticky="nsew")
	btn_AddCourse = tk.Button(Main_R3, text="Add",highlightbackground="goldenrod", activebackground='light blue', command=lambda: AddCourse(ent_Course.get(),MainWindow))
	btn_AddCourse.grid(row=2, column=3, pady=10, sticky="nsew")
	
	
	ent_Diet = tk.Entry(Main_R3, width=10)
	ent_Diet.grid(row=1, column=4,columnspan=2, sticky="nsew")
	btn_RemDiet = tk.Button(Main_R3, text="Remove",highlightbackground="goldenrod", activebackground='light blue', command=lambda: RemDiet(ent_Diet.get(),MainWindow))
	btn_RemDiet.grid(row=2, column=4, pady=10, sticky="nsew")
	btn_AddDiet = tk.Button(Main_R3, text="Add", highlightbackground="goldenrod", activebackground='light blue',command=lambda: AddDiet(ent_Diet.get(),MainWindow))
	btn_AddDiet.grid(row=2, column=5, pady=10, sticky="nsew")
	
	ent_Method = tk.Entry(Main_R3, width=10)
	ent_Method.grid(row=1, column=6, columnspan=2, sticky="nsew")
	btn_RemMethod = tk.Button(Main_R3, text="Remove",highlightbackground="goldenrod", activebackground='light blue', command=lambda: RemMethod(ent_Method.get(),MainWindow))
	btn_RemMethod.grid(row=2, column=6, pady=10, sticky="nsew")
	btn_AddMethod = tk.Button(Main_R3, text="Add",highlightbackground="goldenrod", activebackground='light blue', command=lambda: AddMethod(ent_Method.get(),MainWindow))
	btn_AddMethod.grid(row=2, column=7, pady=10, sticky="nsew")
	
	ent_Effort = tk.Entry(Main_R3, width=10)
	ent_Effort.grid(row=1, column=8,columnspan=2, sticky="nsew")
	btn_RemEffort = tk.Button(Main_R3, text="Remove",highlightbackground="goldenrod", activebackground='light blue', command=lambda: RemEffort(ent_Effort.get(),MainWindow))
	btn_RemEffort.grid(row=2, column=8, pady=10, sticky="nsew")
	btn_AddEffort = tk.Button(Main_R3, text="Add",highlightbackground="goldenrod", activebackground='light blue', command=lambda: AddEffort(ent_Effort.get(),MainWindow))
	btn_AddEffort.grid(row=2, column=9, pady=10, sticky="nsew")
	

	Main_R3.grid_rowconfigure(0, weight=1)
	#Making all columns resize the same to keep things looking pretty
	Main_R3.grid_columnconfigure([0,1,2,3,4,5,6,7,8,9], weight=1)

	Main_R3.grid(row =2,column = 0, sticky = "nsew")

	#Row 4

	Main_R4 = tk.Frame(MainWindow)
	
	btn_Pic = tk.Button(Main_R4, text="Add Picture", activebackground='light blue', width= 60, command=UploadAction)
	btn_Pic.grid(row = 0, column=0, columnspan=2, sticky="nsew")

	btn_Submit = tk.Button(Main_R4, text="Lookup Recipe", activebackground='pale green', width= 60, command=lambda: SearchRecipe(ent_url.get(),int(read_wild.get()),int(read_cuisine.get()),CuisineDB,int(read_course.get()),CourseDB,int(read_diet.get()),DietDB,int(read_method.get()),MethodDB,int(read_effort.get()),EffortDB,"-"+read_notes.get()))
	btn_Submit.grid(row = 0, column=2, columnspan=6, sticky="nsew")

	Main_R4.grid_rowconfigure(0, weight=1)
	Main_R4.grid_columnconfigure(0, weight=1)
	Main_R4.grid(row=3,column=0,columnspan=8,sticky="nsew")

	#Row 5

	Main_R5 = tk.Frame(MainWindow)

	label_notes = tk.Label(Main_R5,text="Recipe Notes", bg="sky blue", fg="white")
	label_notes.grid(row=0, column=0, columnspan=8, sticky="nsew")

	read_notes = tk.StringVar()
	ent_notes = tk.Entry(Main_R5, textvariable= read_notes,bg="white", fg="black")
	ent_notes.grid(row=1, column=0, columnspan=8,sticky="nsew")

	Main_R5.grid_rowconfigure(0, weight=1)
	Main_R5.grid_columnconfigure(0, weight=1)
	Main_R5.grid(row=4,column=0,columnspan=8,sticky="nsew")
	connection.close()
	MainWindow.mainloop()
	
	
#Check if Database exists otherwise 


if (os.path.exists(SQL_Path)):
	connection = sqlite3.connect(SQL_Path)
	cur = connection.cursor()
	print("Connected to Database")
	CreateMain()
else:
	print("Failed to find database at:",SQL_Path)
	StartUp = tk.Tk()
	StartUp.rowconfigure(0, weight=1)
	StartUp.columnconfigure(0, weight=1)
	StartUp.title("StartUp Error")
	StartUp.minsize(640,75)
	F1 = tk.Frame(StartUp)
	
	DB_Prompt = tk.Label(F1, text = "Cannot Find Database Insert Path",bg='sky blue', fg='white')
	DB_Prompt.grid(row=0,column=0, sticky = "nsew") 
	
	DB_Path = tk.Text(F1, height= 1,bg='bisque2')
	DB_Path.insert(tk.INSERT, "")
	DB_Path.grid(row=1,column=0, sticky = "nsew")
	
	
	btn_Change = tk.Button(F1, text="Change Path", highlightbackground="goldenrod", activebackground='light green',command=lambda: ChangeDbPath( DB_Path.get("1.0",tk.END),StartUp))
	btn_Change.grid(row=2, column=0, sticky="nsew")
	
	F1.rowconfigure([0,2], weight=0)
	F1.rowconfigure([1], weight=1)
	F1.columnconfigure(0,weight=1)

	F1.grid(row=0,column=0,sticky="nsew")
    
	StartUp.mainloop()

























