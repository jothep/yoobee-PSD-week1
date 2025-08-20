Sqlite3 tables management function

After you run `main.py`, the program first checks whether the default database file at `data/users.db` exists. If it doesn’t, the file will be created automatically and the `users` table will be created. Then a menu appears with these options:

1. Create all YB College–related tables (Activity 4 task)
2. Show all current tables
3. Select a table to manage
4. Manage the `users` table (keeps the sample features from the original code)

If you choose option 3, you’ll be prompted to enter the name of the table to manage, and then you’ll see this menu:

1. Add a record
2. Delete a record
3. View all records in the current table
4. Return to the previous menu

For creating the YB College–related tables, I batch-create them by executing specified SQL statements via `cursor.execute()`. For listing all tables, I use the same approach by running a SQL statement that queries all tables.

For adding a record to a specified table, I first read all column names and types from the table, then print prompts in sequence and ask for input according to each column’s name and type. After the inputs are provided, I assemble the corresponding fields into an `INSERT` statement and execute it.

For deleting a record, the user provides the `rowid` of the record to delete; I then assemble a complete `DELETE` command and execute it. I did not choose to use the primary key (PK) as the deletion condition because two tables here—`STUDENTS_SUBJECTS` and `CLASS_SUBJECTS`—use composite primary keys, which complicates deletion. Since `rowid` exists by default, I use `rowid` for deletion.
