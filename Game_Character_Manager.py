import sqlite3
#Connects to a database file, allowing for editing and updating
db=sqlite3.connect('Game_Character_Manager.db')
#Cursor controls the procedures done to the database
cur=db.cursor()

#Creates table first time it is run, ignores rest of time
cur.execute('''
CREATE TABLE IF NOT EXISTS Characters(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Class TEXT NOT NULL,
    Level INTEGER NOT NULL,
    MaxHP INTEGER NOT NULL,
    HP INTEGER NOT NULL,
    Status TEXT NOT NULL);''')
db.commit()



#Main menu, runs continuously until program is terminated
def Main():
    print('')
    print('Welcome to the the Game Character Manager')
    print('')
    print('1. Add Character')
    print('2. View All Characters')
    print('3. Update Character')
    print('4. Delete Character')
    print('5. Exit')
    print('')
    choice=int(input('Enter Your Choice: '))

    #Gives options between the functions of the program
    if choice==1:
        Add_Character()
        Main()
    elif choice==2:
        View_Characters()
        Main()
    elif choice==3:
        Update_Character()
        Main()
    elif choice==4:
        Delete_Character()
        Main()
    elif choice==5:
        exit()
    else:
        print('Invalid Choice, Choose From 1-5')
        Main()


#Adds a character to the database table
def Add_Character():
    print('')
    name=input('Enter Name: ')
    Class=input('Enter Class: ')
    level=int(input('Enter Level: '))
    while level > 100 or level < 1:
        print('Invalid. Level must be between 1 and 100.')
        level=int(input('Enter Level: '))
    MaxHP= ((level*3)+10)
    Status= 'Alive'

    cur.execute('''
    INSERT INTO Characters(Name,Class,Level,MaxHP,HP,Status)
    VALUES
    (?,?,?,?,?,?)''',(name,Class,level,MaxHP,MaxHP,Status))
    db.commit()


#Prints all entries in database table
def View_Characters():
    cur.execute('''
    SELECT * FROM Characters''')
    data=cur.fetchall()
    for line in data:
        print('')
        print(f'Character Slot {line[0]}: {line[1]}, a LVL {line[3]} {line[2]}')
        print(f'HP: {line[5]}/{line[4]}')
        print(f'Status: {line[6]}')


#Updates an existing entry in table
def Update_Character():
    print('')
    slot=int(input('Which Character Slot: '))
    print('')
    new_name=input('Enter Name: ')
    new_class=input('Enter Class: ')
    new_lvl=int(input('Enter Level: '))
    while new_lvl > 100 or new_lvl < 1:
        print('Invalid. Level Must Be Between 1 and 100.')
        new_lvl=int(input('Enter Level: '))
    new_MaxHP=((new_lvl*3)+10)
    curr_HP=-1
    while curr_HP < 0 or curr_HP > new_MaxHP:
        curr_HP=int(input('Enter Current HP: '))
    if curr_HP == 0:
        Status= 'Defeated'
    elif curr_HP <= 0.5 * new_MaxHP:
        Status= 'Injured'
    else:
        Status= 'Alive'
    
    cur.execute('''
    UPDATE Characters
    SET Name = ?,
        Class = ?,
        Level = ?,
        MaxHP = ?,
        HP = ?,
        Status = ?
    WHERE ID = ?;
    ''', (new_name,new_class,new_lvl,new_MaxHP,curr_HP,Status,slot))
    db.commit()


#Delete function, removes an entry from database table
def Delete_Character():
    print('')
    slot=int(input('Which Character Slot: '))
    print('')
    cur.execute('''
    DELETE FROM Characters
    WHERE ID = ?;
    ''', (slot,))
    db.commit()
    
    
#Begins program
Main()
#Closes database
db.close()
