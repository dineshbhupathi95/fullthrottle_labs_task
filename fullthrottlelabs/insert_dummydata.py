import sqlite3

def insert_users_into_table(real_name, tz,start_time, end_time,activity_periods):
    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        print("Connected to SQLite")

        users_insert_with_param = """INSERT INTO usermanagement_User
                          (real_name, tz) 
                          VALUES (?, ?);"""

        users_activity_insert_with_param = """INSERT INTO usermanagement_ActivityPeriod
                          (start_time, end_time) 
                          VALUES (?, ?);"""
        activityperiod_inser =  """SELECT * FROM usermanagement_activityperiod
                          ;"""
        data = (real_name,tz)
        activity_data = (start_time,end_time)
        # a  = (activity_periods)
        cursor.execute(users_insert_with_param, data)
        cursor.execute(users_activity_insert_with_param,activity_data)
        cursor.execute(activityperiod_inser)
        connection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (connection):
            connection.close()
            print("The SQLite connection is closed")


insert_users_into_table('ajay','Asia/Kolkata','2020-03-20 08:00','2020-03-30 12:00',1)
insert_users_into_table('harish','Asia/kolkata','2020-03-25 10:00','2020-03-31 01:00',2)

###########################################################################


