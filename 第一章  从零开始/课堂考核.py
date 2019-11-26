from email.mime.text import MIMEText  # 调用构建邮件文本
 # from email.mime.multipart import MIMEMultipart  # 构建多个元素
 # from email.mime.image import MIMEImage  # 构建邮件图片

# 构建电子邮件内容
msg_text = MIMEText('你好','plain')

import smtplib
while True:
    srv = smtplib.SMTP('smtp.qq.com',25)  # 连接服务器
    srv.login('1005630541@qq.com','ceiwedfyxtyebdfb')  # 登录
    srv.sendmail('1005630541@qq.com','1482596775@qq.com',
             msg_text.as_string())  # 后一个邮箱为对方qq邮箱