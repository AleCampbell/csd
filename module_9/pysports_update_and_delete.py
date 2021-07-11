### Campbell, Alexander
### 11JUL2021
### Module 8 Test program for MySQL


### Imports
### import msvcrt

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


def show_players(cursor, title):
    """ method to execute an inner join on the player and team table, 
        iterate over the dataset and output the results to the terminal window.
    """

    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    # iterate over the player data set and display the results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    ### try block for errors 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    
    cursor = db.cursor()

    ### player 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    
    player_data = ("Smeagle", "Beagle", 1)

    
    cursor.execute(add_player, player_data)

    
    db.commit()

    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Smeagle', last_name = 'Beagle' WHERE first_name = 'Smeagle'")

    
    cursor.execute(update_player)

     
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

     
    delete_player = ("DELETE FROM player WHERE first_name = 'Smeagle'")

    cursor.execute(delete_player)

    ### Display Player Table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    ### close connection

    db.close()