import sqlite3
import time

# 尋找該地區的全部年級的各個答對題數
def getData(region: str):
    con = sqlite3.connect("sql.db")
    userTable = "user"
    problemTable = "problem"

    cursor = con.cursor()

    cursor.execute(
        f"""SELECT {userTable}.grade, COUNT(is_correct) FROM {userTable} 
        JOIN {problemTable} ON {userTable}.uuid = {problemTable}.uuid
        WHERE city = "{region}" AND is_correct = 1
        GROUP BY {userTable}.grade;
        """
    )

    return list(map(list, cursor.fetchall()))
    
# def getRegion():
#     con = sqlite3.connect("sql.db")
#     userTable = "user"

#     cursor = con.cursor()

#     cursor.execute(
#         f"""SELECT {userTable}.city FROM {userTable} 
#         GROUP BY {userTable}.city;
#         """
#     )
    
#     print(len(cursor.fetchall()))

# REGIONS = {
#     "chc": "Chiayi",
#     "cy": "Chiayi City",
#     "hc": "Hsinchu City",
#     "hlc": 
#     "kh": "Kaohsiung",
#     "kl": "Keelung",
#     "km": "Kinmen",
#     "lj": "Lienchiang",
#     "ml": "Miaoli",
#     "ntct": "Nantou",
#     "ntpc": "New Taipei",
#     "phc": "Pingtung",
#     "tc": "Taitung City",
#     "tn": "Tainan",
#     "tp": "Taipei",
#     "tcct": "Taitung County",
#     "ty": "Taoyuan",
#     "ylc": "Yunlin",
    
# }

# if __name__ == "__main__":
#     getRegion()
