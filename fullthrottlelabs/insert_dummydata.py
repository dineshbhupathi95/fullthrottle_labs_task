import sqlite3

def insert_users_into_table(real_name, tz):
    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        users_insert_with_param = """INSERT INTO usermanagement_User
                          (real_name, tz)
                          VALUES (?, ?);"""
        data = (real_name,tz)
        cursor.execute(users_insert_with_param, data)
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert variables into sqlite table", error)
    finally:
        if (connection):
            connection.close()
            print("The SQLite connection is closed")


insert_users_into_table('bhupathi','America/Los_Angeles')
insert_users_into_table('ajay','Asia/kolkata')


#########################################################################################################

def insert_activity_periods_into_table(start_time, end_time,activity_periods):
    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        users_activity_insert_with_param = """INSERT INTO usermanagement_ActivityPeriod
                          (start_time, end_time,activity_periods_id)
                          VALUES (?, ?,?);"""
        activity_data = (start_time,end_time,activity_periods)
        cursor.execute(users_activity_insert_with_param,activity_data)
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert variables into sqlite table", error)
    finally:
        if (connection):
            connection.close()
            print("The SQLite connection is closed")


insert_activity_periods_into_table('2020-03-16 12:00','2020-03-28 13:00',2)
insert_activity_periods_into_table('2020-03-15 01:00','2020-03-22 12:00',1)
insert_activity_periods_into_table('2020-03-18 10:00','2020-03-26 08:00',2)
insert_activity_periods_into_table('2020-03-16 07:00','2020-03-28 18:00',1)