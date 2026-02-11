# Fabric MySQL Deployment Automation

## Project Overview

This project uses Fabric (Python) to automate:

- Installation of MySQL Server
- Creation of a MySQL database
- Importing a SQL dump file

It demonstrates basic DevOps automation for database deployment.

---

## Technologies Used

- Python 3
- Fabric
- MySQL Server
- Ubuntu/Linux

---

## Project Structure

fabric_mysql/
│
├── deploy.py
├── password.txt
├── .gitignore
└── README.md

yaml
Copy code

---

## How It Works

The `deploy.py` script performs the following tasks:

1. Connects to the host using Fabric
2. Installs MySQL server
3. Creates a database named `alu_database`
4. Imports the SQL file `database_setup.sql`

---

## How To Run

Install dependencies:

pip3 install fabric

yaml
Copy code

Run the script:

python3 deploy.py

yaml
Copy code

---

## Notes

- `password.txt` is excluded from GitHub using `.gitignore`
- This project is for academic and learning purposes
- In production environments, credentials should be managed securely

---

## Author

Ariane ITETERO  