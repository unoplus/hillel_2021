# Create by Bender
"""
Написать програму для проверки пароля.
У пользователя запрашивается пароль сравнивается с ожидаемой фразой -
нужно сообщить о том что пароль совпал или пароль не совпал
"""

your_password = "Password"
user_password = input("Type your password: ")
if user_password == your_password:
    print("Granted!")
else:
    print("Denied!")
