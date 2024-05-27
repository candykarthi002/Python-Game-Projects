import sqlite3

connection = sqlite3.connect('password_manager.db')
cursor = connection.cursor()


def add_password(username, account, password, platform):
    try:
        cursor.execute("INSERT INTO Password_Manager VALUES(?, ?, ?, ?)",
                       (username, account, password, platform))
        connection.commit()
        return "Success"
    except:
        return "Failed"


def delete_password(username):
    try:
        cursor.execute(
            "DELETE * FROM Password_Manager WHERE username = :user", {'user': username})
        connection.commit()
        return "Success"
    except:
        return "Failed"


def search_password(username, account):
    cursor.execute("SELECT * FROM Password_Manager")
    queries = cursor.fetchall()
    for q in queries:
        if q[0] == username and q[1] == account:
            return f"Username: {q[0]}\nAccount: {q[1]}\nPassword: {q[2]}\nPlatform: {q[3]}"

    return "There is no such account!!"


def display_all_passwords():
    cursor.execute("SELECT * FROM Password_Manager")
    info = cursor.fetchall()
    if len(info) > 0:
        passwords = []
        for data in info:
            p = {}
            p["User_name"] = data[0]
            p["Account"] = data[1]
            p["Password"] = data[2]
            p["Platform"] = data[3]
            passwords.append(p)

        return passwords

    else:
        return None
