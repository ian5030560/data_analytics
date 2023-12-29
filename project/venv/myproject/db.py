import sqlite3
import time

# 尋找該年級每個地區的答對題數、答題數、總人數
def getData(grade: int):
    con = sqlite3.connect("sql.db")
    user = "user"
    problem = "problem"

    cursor = con.cursor()

    cursor.execute(
        f"""SELECT "city", COUNT({problem}.upid), 
        SUM(CASE WHEN {problem}.is_correct = 1 THEN 1 ELSE 0 END),
        COUNT(DISTINCT {user}.uuid)
        FROM {user}
        JOIN {problem} ON {user}.uuid = {problem}.uuid
        WHERE {user}.grade = {grade}
        GROUP BY "city";
        """
    )

    return list(map(list, cursor.fetchall()))

# REGIONS = {
#     "chc": "Chiayi",
#     "cy": "Chiayi City",
#     "hc": "Hsinchu City",
#     "hlc": "Hualien City",
#     "ilc": "Yilan City",
#     "kh": "Kaohsiung City",
#     "kl": "Keelung City",
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
#     s = time.time()
#     print(getData(1))
#     e = time.time()
#     print(e - s)