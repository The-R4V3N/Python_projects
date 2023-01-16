import sqlite3


class DbOperations:

    # Database connection
    def connect_to_db(self):
        conn = sqlite3.connect('password_records.db')
        return conn

    # Creating Tables in the Database
    def create_table(self, table_name="password_info"):
        conn = self.connect_to_db()
        query = f'''
        CREATE TABLE  IF NOT EXISTS {table_name} (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            website TEXT NOT NULL,
            username VARCHAR(200),
            password VARCHAR(50)
        );
        '''

        with conn as conn:
            cursor = conn.cursor()
            cursor.execute(query)

    # Creating Records
    def create_record(self, data, table_name="password_info"):
        website = data['website']
        username = data['username']
        password = data['password']

        conn = self.connect_to_db()
        query = f'''
        INSERT INTO {table_name}('website', 'username', 'password') VALUES
        (?,?,?);
        '''

        with conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, (website, username, password))

    # Show the Records
    def show_records(self, table_name="password_info"):
        conn = self.connect_to_db()
        query = f'''
        SELECT * FROM {table_name};
        '''

        with conn as conn:
            cursor = conn.cursor()
            list_records = cursor.execute(query)
            return list_records

    # Update Records
    def update_record(self, data, table_name="password_info"):
        ID = data['ID']
        website = data['website']
        username = data['username']
        password = data['password']
        conn = self.connect_to_db()
        query = f'''
        UPDATE {table_name} SET website = ?, username =?, password =? WHERE ID = ?;

        '''

        with conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, (website, username, password, ID))

    # Delete Records
    def delete_record(self, ID, table_name="password_info"):

        conn = self.connect_to_db()
        query = f'''
        DELETE FROM {table_name} WHERE ID = ?;
        '''

        with conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, (ID,))
