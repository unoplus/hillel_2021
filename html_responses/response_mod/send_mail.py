#! /usr/bin/env python3
# creata @cyberscriptor


import os
import smtplib
from configparser import ConfigParser
from email import encoders
from email.mime.text import MIMEText as MT
from email.mime.base import MIMEBase as MB
from email.mime.multipart import MIMEMultipart as MM
from email.utils import formatdate as fd

__all__ = ["send_mail_without_attachment", "send_mail_with_attachment"]
path_to_ini = "/some_path/"
file_ini = "mail.ini"


def send_mail_without_attachment(subject_mail: str, to_address: str,
                                 body_mail: str) -> None:
    """
    Функция для формирования и отправки почты без вложений.
    Принимает на вход строки:
    тема письма, получатель, дело письма.
    :param subject_mail: Тема письма.
    :param to_address: Электронный адрес получателя.
    :param body_mail: Тело письма.
    :return:
    """
    if not os.path.exists(path_to_ini + file_ini):
        print(f'Папка: "{path_to_ini}" не содержит конфигурационный файл: '
              f'"{file_ini}"! Отправка письма невозможна!')
    else:
        params = ConfigParser()
        params.read(path_to_ini + file_ini)
        host = params.get("mail", "server")
        port = params.get("mail", "port")
        from_address = params.get("mail", "from_address")
        message = MM()
        message["From"] = from_address
        message["Subject"] = subject_mail
        message["Date"] = fd(localtime=True)

        if body_mail:
            message.attach(MT(body_mail))

        message["To"] = to_address

        server = smtplib.SMTP(host, port)
        server.sendmail(from_address, to_address, message.as_string())
        server.quit()


def send_mail_with_attachment(subject_mail: str, to_address: str,
                              body_mail: str, file_attachment: str) -> None:
    """
    Функция для формирования и отправки почты без вложений.
    Принимает на вход строки:
    тема письма, получатель, дело письма.
    :param subject_mail: Тема письма.
    :param to_address: Электронный адрес получателя.
    :param body_mail: Тело письма.
    :param file_attachment: Файл вложение.
    :return:
    """
    header = "Content-Desposition","attachment; filename='%s'" % file_attachment
    if not os.path.exists(path_to_ini + file_ini):
        print(f'Папка: "{path_to_ini}" не содержит конфигурационный файл: '
              f'"{file_ini}"! Отправка письма невозможна!')
    else:
        params = ConfigParser()
        params.read(path_to_ini + file_ini)
        host = params.get("mail", "server")
        port = params.get("mail", "port")
        from_address = params.get("mail", "from_address")
        message = MM()
        message["From"] = from_address
        message["Subject"] = subject_mail
        message["Date"] = fd(localtime=True)

        if body_mail:
            message.attach(MT(body_mail))

        message["To"] = to_address
        attachment = MB("application", "octet-stream")

        try:
            with open(file_attachment, "rb") as f:
                data = f.read()

            attachment.set_payload(data)
            encoders.encode_base64(attachment)
            attachment.add_header(*header)
            message.attach(attachment)
            server = smtplib.SMTP(host, port)
            server.sendmail(from_address, to_address, message.as_string())
            server.quit()
        except IOError:
            message = "Не могу открыть вложение %s" % file_attachment
            print(message)
