import sqlite3
import time

# 尋找該年級每個地區的答題數、答對題數、總人數
def getData(grade: int):
    con = sqlite3.connect("sql.db")
    user = "user"
    problem = "problem"

    cursor = con.cursor()

    cursor.execute(
        f"""SELECT {user}."city", COUNT({problem}.upid) AS "total_problem", 
        SUM(CASE WHEN {problem}.is_correct = 1 THEN 1 ELSE 0 END) AS "total_correct", 
        COUNT(DISTINCT {user}.uuid) AS "total_people"
        FROM {user}
        JOIN {problem} ON {user}.uuid = {problem}.uuid
        WHERE {user}.grade = {grade}
        GROUP BY {user}."city";
        """
    )
    
    return list(map(list, cursor.fetchall()))

REGIONS = {
    "chc": "彰化",
    "cy": "嘉義",
    "hc": "新竹",
    "hlc": "花蓮",
    "ilc": "宜蘭",
    "kh": "高雄",
    "kl": "基隆",
    "km": "金門",
    "lj": "連江",
    "ml": "苗栗",
    "ntct": "南投",
    "ntpc": "新北",
    "phc": "澎湖",
    "ptc": "屏東",
    "tc": "台中",
    "tn": "台南",
    "tp": "台北",
    "ttct": "台東",
    "ty": "桃園",
    "ylc": "雲林"
}

# if __name__ == "__main__":
#     s = time.time()
#     print(getData(1))
#     e = time.time()
#     print(e - s)
