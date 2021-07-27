# Create by Bender
"""
Создать программу которая запрашивает год для проверки, убеждается что введен цыфры обозначающие год
и  соответствует следующему требованию:
Требование к вводимому году  :  1900 < год < 1000000
При не соответсвии - сообщить что введеный год не отвечает условиям.
Если год отвечает требованиям - проверить на выскостный\невысокостный и сообщить в терминал о результатах
например :
      “1987 is not leap year”
"""

while True:
    user_year = input("Type year: ")
    if user_year.isdigit() and 1900 < int(user_year) < 1000000:
        break
    else:
        print("Year must be between 1900 and 1000000!")

year = int(user_year)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"Year {year} is leap.")
else:
    print(f"Year {year} is not leap.")
