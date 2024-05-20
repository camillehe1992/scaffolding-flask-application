import smtplib
from email.mime.text import MIMEText

# Mocked SMTP Server
LOCAL_SMTP_HOST = "localhost"
LOCAL_SMTP_PORT = 2525

# QQ SMTP Server
QQ_SMTP_HOST = "smtp.qq.com"
QQ_SMTP_PORT = 465
QQ_SMTP_USER = "1075141183@qq.com"
QQ_SMTP_PASS = "rrmeldvmusuyidab"


class SMTPClient:

    def __init__(self, subject, body, to, debug=True):

        self.subject = subject
        self.body = body
        self.to = to

        if debug:
            self.smtp_host = LOCAL_SMTP_HOST
            self.smtp_port = LOCAL_SMTP_PORT
            self.smtp_user = None
            self.smtp_pass = None

            self.sender = "no-reply@demo.com"

            self.smtp = smtplib.SMTP(self.smtp_host, self.smtp_port)
        else:
            self.smtp_host = QQ_SMTP_HOST
            self.smtp_port = QQ_SMTP_PORT
            self.smtp_user = QQ_SMTP_USER
            self.smtp_pass = QQ_SMTP_PASS

            self.sender = QQ_SMTP_USER

            self.smtp = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)
            # Authentication
            self.smtp.login(self.smtp_user, self.smtp_pass)

    def _generate_message(self) -> str:
        message = MIMEText(self.body, "plain", "utf-8")
        message["From"] = self.sender
        message["To"] = self.to
        message["Subject"] = self.subject
        return message.as_string()

    def send_email(self) -> bool:
        try:
            message = self._generate_message()
            self.smtp.sendmail(self.sender, [self.to], message)
            self.smtp.quit()
            return True
        except Exception as error:
            print(error)
            print(message)
            return False
