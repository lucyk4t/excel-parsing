import pandas as pd
import re
import random as r

df = pd.read_excel("SignalList.xlsx", "SignalList") 
vas = df.values

# 신규 arxml 파일 적용
sigreg = re.compile(r'^\w+')  # 정상 동작 확인
msgreg = re.compile(r'(\"\w+\")\t(\"\w+\")') # 정상 동작 확인

siglist = []
msglist = []

# sig and msg example
# SomeSig;SomeMsg;-;0;8;Motorola;Unsigned;0;1;0;0;127;bit;<none>;ECU Address;0x208;0;0;0;OnWrite;0;0

def sigmsgread():
    try:
        for i in vas:
            for j in i:
                sigstr = re.search(sigreg, j) # Signal 이름 검색
                msgstr = re.search(msgreg, j) # Msg 이름 검색

                if sigstr:
                    sigmod = sigstr.group()
                if msgstr:
                    msgmod = msgstr.group(2).strip(r'\"')

                if sigstr not in ["AReq", "DLvl", "DimLvl", "MAuth", "MInv"]:
                    siglist.append(sigmod)
                    msglist.append(msgmod)
                else:
                    print("Signal Name is in list")
                    sigmsgread()

        ransig = r.randint(0, len(siglist))
        ranmsg = r.randint(0, len(msglist))

        # 랜덤 메시지 확인용, 아래 인덱스를 가지고 SendCANSignal(siglist[ransig], data) 형태로 신호 전송
        print(siglist[ransig], msglist[ranmsg])

    except AttributeError as e:
        print(e)


sigmsgread()
