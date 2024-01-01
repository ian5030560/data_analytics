import sqlite3
from multiprocessing import Pool

def create(grade: int):
    con = sqlite3.connect("sql.db")
    cursor = con.cursor()
    
    g = f"grade{grade}"
    cursor.execute(
        f"""CREATE TABLE {g}(
            "upid" TEXT NOT NULL,
            "uuid" TEXT NOT NULL,
            "ucid" TEXT NOT NULL,
            "is_correct" INTEGER NOT NULL,
            FOREIGN KEY("uuid") REFERENCES user("uuid")
        )
        """
    )
    
    con.commit()
    print(f"create table {g} successfully")
    cursor.close()
    con.close()
    
def insert(grade: int):
    con = sqlite3.connect("sql.db")
    cursor = con.cursor()
        
    g = f"grade{grade}"
    cursor.execute(
        f"""SELECT problem.upid, user.uuid, problem.ucid, problem.is_correct 
        FROM user
        JOIN problem ON user.uuid = problem.uuid
        WHERE user.grade = {grade}
        """
    )
    
    print(f"get data from problem when grade is {grade}")
    
    cursor.executemany(
        f"INSERT INTO {g} VALUES(?, ?, ?, ?)",
        cursor.fetchall()
    )
    
    print(f"insert data into {g} successfully")
    con.commit()
    cursor.close()
    con.close()
    
def execute(grade: int):
    create(grade)
    insert(grade)
    
if __name__ == "__main__":
    grades = [i for i in range(1, 13)]
    
    pool = Pool(4)
    pool.map(execute, grades)
    pool.close()
    print("Finished")