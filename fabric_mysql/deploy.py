from fabric import Connection

# Read password
with open('password.txt') as f:
    password = f.read().strip()

# Replace with your username
connection = Connection(
    host='127.0.0.1',
    user='ariane',
    connect_kwargs={'password': password}
)

def install_mysql():
    print("Installing MySQL...")
    connection.sudo('apt update')
    connection.sudo('apt install mysql-server -y')

def create_database():
    db_name = "alu_database"
    print("Creating database...")
    connection.sudo(f'mysql -e "CREATE DATABASE IF NOT EXISTS {db_name};"')

def import_sql():
    db_name = "alu_database"
    dump_path = "/home/ariane/Documents/ALU/momo-sms-analytics/database/database_setup.sql"


    print("Importing SQL dump...")
    connection.sudo(f'mysql {db_name} < {dump_path}')

def deploy():
    install_mysql()
    create_database()
    import_sql()

if __name__ == "__main__":
    deploy()
