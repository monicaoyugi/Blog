from flask_mail import Message
from flask import render_template
from . import mail
from .models import User


def mail_message(template, **kwargs):
    users = User.query.all()
    with mail.connect() as conn:
        for user in users:
            sender_email = 'monicaoyugi@gmail.com'

            msg = Message(recipients=[user.email],
                          sender=sender_email)

            msg.body = render_template(template + ".txt", **kwargs)
            msg.html = render_template(template + ".html", **kwargs)

            conn.send(msg)