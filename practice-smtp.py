import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "from@runoob.com"
recivers = ['aasdf@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其它邮箱

# 三个参数：第一个为文本内容，第二个为plain 设置文本格式，第三个为 utf-8设置编码
message = MIMEMultipart()
message = MIMEText('Python 邮件发送测试', 'plain', 'utf-8')
message['From'] = Header("自我练习", 'utf-8')
message['To'] = Header('测试', 'utf-8')



subject = 'Python SMTP 邮件测试'

message['Subject'] = Header(subject, 'utf-8')


att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1['Content-Type'] = 'application/octet-stream'
att1['Content-Disposition'] = 'attachment;filename="test.txt"'
message.attach(att1)


# 指定图片为当前目录
fp = open('test.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID， 在HTML文本中应用
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, recivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
