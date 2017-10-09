import smtplib

from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '88239962@qq.com' # 发件人邮箱帐号
my_pass = 'xxxxxxx' # 发件人邮箱密码
my_user = '88239962@qq.com'


def mail():
    ret = True
    try:
        msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["FK", my_sender]) # 括号里的对应发件人邮箱昵称，发件人邮箱帐号
        msg['To'] = formataddr(['FK', my_user]) # 括号里的对应收件人邮箱昵称，收件人邮箱帐号
        msg['Subject'] = "Python SMTP发送邮件" # 邮件主题


        server = smtplib.SMTP_SSL('smtp.qq.com', 465) # 发件人邮箱中的SMTP服务器端口是25
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret

ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")