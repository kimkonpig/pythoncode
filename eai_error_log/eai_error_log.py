import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from datetime import datetime, timedelta

## 타겟 사이트 주소(EAI Administrator)
## 이 주소의 경우 회사망에서만 실행 가능 !
baseUrl = 'http://10.151.5.5:10103/alert'

## 타겟 사이트 접속 시 로그인 정보(Basic Auth 활용)
r = requests.get(baseUrl, auth=('paranoid', 'survive'))
# print("[status_code] : ", r.status_code)
soup = bs(r.content, 'lxml')

## 웹사이트 데이터 추출
id_list, process_list, project_list, code_list, severity_list, time_list, des_list = [], [], [], [], [], [], []
for i in soup.find_all('alert'):
    try:
        tmp_str = i.get('description')

        if "max execution time over!" not in tmp_str:
            id_list.append(i.get('id'))
            process_list.append(i.get('process'))
            code_list.append(i.get('code'))
            time_list.append(i.get('time'))
            # des_list.append(i.get('description'))
            des_content = i.get('description').split(':', maxsplit=1)
            des_list.append(des_content[1])
            
            ## split 대신 사용할 수 있는 메서드 있는지 찾아보기
            project_list.append(des_content[1].split('@projectId')[1].split('/')[4].split('@')[0])

        else:
            pass
    except:
        pass

## DataFrame으로 데이터 확인하기, 파일 로컬 저장
df = pd.DataFrame([id_list, process_list, project_list, code_list,  time_list, des_list]).T
df.columns = ['ID', 'PROCESS', 'PROJECT', 'CODE', 'TIME', 'DESCRIPTION']
# df.to_csv("C:\\Users\\user\\Desktop\\PYTHON_PRJ\\EAI_ERROR_LOG\\EAI_ERROR_LOG_1.csv", encoding='utf-8-sig', index=False)
df.to_csv("C:\\pythoncode\\eai_error_logEAI_ERROR_LOG_1.csv", encoding='utf-8-sig', index=False)
# print(data.head())


## 메일링을 위한 데이터만 뽑기
## 배치를 5시간 주기로 수행되도록 할 예정
now = datetime.now() # 현재시간
boh = now - timedelta(hours=5) # 5시간 전(before_one_hour)
final_boh = str(boh.strftime("%H:%M:%S"))
# print("final_boh : ",final_boh)

is_before_one_hour = df['TIME'] >= final_boh
# print('is_before_one_hour : ', is_before_one_hour)

check_data_df = df[is_before_one_hour]
# check_data_df.to_csv("C:\\Users\\user\\Desktop\\PYTHON_PRJ\\EAI_ERROR_LOG\\EAI_ERROR_LOG_DETAIL_1.csv", encoding='utf-8-sig', index=False)
check_data_df.to_csv("C:\\pythoncode\\EAI_ERROR_LOG_DETAIL_1.csv", encoding='utf-8-sig', index=False)
# print(check_data)
# print(check_data.groupby('PROCESS').size())

chkdt_size_df = check_data_df.groupby('PROCESS').size()
# print(chkdt_size_df)

mailFlag = False
for i in chkdt_size_df:
    if i > 4:
        mailFlag = True
    else:
        pass

if(mailFlag):
    ## exchangelib 라이브러리를 사용하여 outlook 메일 발송
    from re import T
    # pip install exchangelib
    from exchangelib import Account, Message, Mailbox, Credentials, FileAttachment, DELEGATE
    from exchangelib.items import SEND_ONLY_TO_ALL, SEND_ONLY_TO_CHANGED

    ## 메일 발송 시 첨부할 파일 append
    attachments = []
    with open('C:\\Users\\user\\Desktop\\PYTHON_PRJ\\EAI_ERROR_LOG\\EAI_ERROR_LOG_DETAIL_1.csv', 'rb') as f:
        content = f.read()
    attachments.append(('EAI_ERROR_LOG_DETAIL_1.csv', content))

    ## 메일 발송 시 계정 설정
    credentials = Credentials(username='hsnc\\yourforest', password='Kimyoulim1009!@')
    a = Account(primary_smtp_address='yourforest@hanwha.com', credentials=credentials
            , autodiscover=T, access_type=DELEGATE)

    ## 메일 발송계정, 제목, 내용, 수신인 등 설정
    m = Message(
        account = a,
        subject = 'python eai error log mailing test',
        body = chkdt_size_df,
        to_recipients=[
            Mailbox(email_address='yourforest@hanwha.com')
        ]
        # cc_recipients=[],
        # bcc_recipients=[],
    )

    ## 파일 첨부
    for attachment_name, attachment_content in attachments or []:
        file = FileAttachment(name=attachment_name, content=attachment_content)
        m.attach(file)

    m.send()