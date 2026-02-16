import os
import pyodbc

# 1. SQL Server connection details
server = r'BollamHarshil\SQLEXPRESS'      # Example: 'localhost' or 'SERVER\\INSTANCE'
database = 'master'  # Example: 'TestDB'

# 2. Folder containing .sql files
sql_folder = r"C:\Users\bharg\Documents\SQL"

# 3. Connect to SQL Server
conn = pyodbc.connect(
    f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
)
cursor = conn.cursor()

# 4. Loop through all .sql files in the folder
for file in os.listdir(sql_folder):
    if file.endswith(".sql"):
        file_path = os.path.join(sql_folder, file)
        print(f"Running SQL file: {file_path}")

        # Read SQL query from file
        with open(file_path, 'r', encoding='utf-8') as f:
            sql_query = f.read()

        try:
            # Execute SQL query
            cursor.execute(sql_query)
            conn.commit()
            print(f"✅ Successfully executed {file}")
        except Exception as e:
            print(f"❌ Error executing {file}: {e}")

# 5. Close connection
cursor.close()
conn.close()
