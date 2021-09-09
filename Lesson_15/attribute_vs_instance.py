# Create by Bender

class CaffeBill:
    # чаевые
    # Атрибут объекта класса
    tips = 10

    def __init__(self):
        # Атрибут экземпляра класса
        self.tax = 15


table1 = CaffeBill()
table2 = CaffeBill()
print(table1.tips, table2.tips)
CaffeBill.tips = 12
print(table1.tips, table2.tips)
