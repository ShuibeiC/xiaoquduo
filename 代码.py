import datetime
import json
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header

openid = ''
Username = ''
pasd = ''
phone = ''
server_host = 'smtp.qq.com'

def GetId():
    url = 'https://mps.zocedu.com/corona/submitHealthCheck'
    res = requests.get(url,{
        "openId":openid,
        "latitude":"",
        "longtitude":""
    })
    id = res.cookies.get("JSESSIONID")
    return id

def send_email():
    server = smtplib.SMTP()
    server.connect(server_host)
    server.login(Username,pasd)
    sender = Username
    recever = Username
    subject = '健康打卡已经完成！'
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    sentence = '当前时间为：'+time+'，当天健康打卡已经完成！'

    #邮件内容
    message = MIMEText(sentence,'plain','utf-8')
    message['Subject'] = Header(subject,'utf-8')
    server.sendmail(sender,recever,message.as_string())
    server.quit()

def CheckIn():
    id = GetId()
    url = 'https://mps.zocedu.com/corona/submitHealthCheck/submit'
    data = {
        "checkPlace":"XX省 - XX市 - XX区",
        "contactMethod":phone,
        "teacher":"",
        "temperature":"36.5",
        "isCohabitFever":"否",
        "isLeavePalce":"否",
        "beenPlace":"",
        "isContactNcov":"否",
        "livingPlace":checkPlace,
        "livingPlaceDetail":"xxxx",
        "name1":"",
        "relation1":"",
        "phone1":"",
        "name2":"",
        "relation2":"",
        "phone2":"",
        "remark":"",
        "extraInfo":"[]",
        "healthStatus":"z",
        "emergencyContactMethod":"[]",
        "checkPlacePoint":"124, 37",
        "checkPlaceDetail":"",
        "checkPlaceCountry":"",
        "checkPlaceProvince":"XX省",
        "checkPlaceCity":"XX市",
        "checkPlaceArea":"XX区",
    }
    headers = {"User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"}
    cookies = {
        "JSESSIONID":id
    }
    res = requests.post(url,data=data,headers=headers,cookies=cookies)
    if res.text == "":
        print("校趣多打卡成功！当前时间：" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        send_email()
    else:
        print("校趣多打卡失败！请检查配置文件是否填写正确！")

def main(event,Contact):
    CheckIn()
