import sqlite3
db=sqlite3.connect('Game_Character_Manager.db')
cur=bd.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Characters(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Class TEXT NOT NULL,
    Level INTEGER NOT NULL);''')
db.commit()

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
    
    if choice==1:
        Add_Character()
    elif choice==2:
        pass
    elif choice==3:
        pass
    elif choice==4:
        pass
    elif choice==5:
        pass
    else:
        print('Invalid Choice, Choose From 1-5')
        Main()

def Add_Character():
    name=input('Enter Name: ')
    Class=input('Enter Class: ')
    level=int(input('Enter Level: '))

    cur.execute('''
    INSERT INTO Characters(Name,Class,Level)
    VALUES
    (?,?,?)''',(name,Class,level))
    db.commit()

Main()
db.close()
