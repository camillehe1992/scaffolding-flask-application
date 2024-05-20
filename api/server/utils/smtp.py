import smtplib
from email.mime.text import MIMEText
from flask import current_app


class SMTPClient:

    def __init__(self, subject, body, to, text_type="plain"):
        self.enabled = current_app.config["SMTP_HOST"] or "localhost"
        self.subject = subject
        self.body = body
        self.to = to
        self.text_type = text_type

        self.smtp_host = current_app.config["SMTP_HOST"]
        self.smtp_port = current_app.config["SMTP_PORT"]

        if self.enabled == "localhost":
            self.sender = current_app.config["SMTP_USER"]

            self.smtp = smtplib.SMTP(self.smtp_host, self.smtp_port)

        else:
            self.sender = current_app.config["SMTP_USER"]
            self.smtp_user = current_app.config["SMTP_USER"]
            self.smtp_pass = current_app.config["SMTP_PASS"]

            self.smtp = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)
            # Authentication
            self.smtp.login(self.smtp_user, self.smtp_pass)

        print(f"{self.enabled } SMTP server is instantiated")

    def _generate_html_body(self, body) -> str:
        template = body["template"]
        args = body["args"]
        html_body = ""
        with open(
            f"templates/{template}.html", "r"
        ) as file:  # r to open file in READ mode
            html_as_string = file.read()
            html_body = html_as_string.format(**args)
        return html_body

    def _generate_message(self) -> str:
        if self.text_type == "plain":
            message = MIMEText(self.body, self.text_type, "utf-8")
        else:
            html_body = self._generate_html_body(self.body)
            message = MIMEText(html_body, self.text_type, "utf-8")
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
