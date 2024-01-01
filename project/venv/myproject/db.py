import sqlite3
import time

# 尋找該年級每個地區的答題數、答對題數、總人數
def getData(grade: int):
    con = sqlite3.connect("sql.db")

    cursor = con.cursor()
    g = f"grade{grade}"
    
    cursor.execute(
        f"""SELECT user.city, COUNT({g}.upid) AS "total_problem", 
        SUM(CASE WHEN {g}.is_correct = 1 THEN 1 ELSE 0 END) AS "total_correct", 
        COUNT(DISTINCT user.uuid) AS "total_people"
        FROM user
        JOIN {g} ON user.uuid = {g}.uuid
        GROUP BY user.city;
        """
    )
    return list(map(list, cursor.fetchall()))
    
speedList = [None for _ in range(12)]
def testSpeed(grade: int):
    s = time.time()
    getData(grade)
    e = time.time()
    speedList[grade - 1] = e - s

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
        
    
    
if __name__ == "__main__":
    
    for t in range(len(speedList)):
        testSpeed(t + 1)
        
    print(f"平均值: {sum(speedList) / len(speedList)}")
    print(f"最大值: {max(speedList)}")
    print(f"最小值: {min(speedList)}")