import pyodbc
import datetime
import os
import sys

server = r'LOKESH\SQLEXPRESS'
database = 'BILL_GENERATION'
driver = '{ODBC Driver 17 for SQL Server}'
try:
    con = pyodbc.connect(
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )

except:
    print('NOT connected')
else:
    print("Database Connected Successfully")


class Admin:

    def create_customer(self):
        try:
            name = input("Enter Customer Name: ")
            cursor = con.cursor()
            cursor.execute("INSERT INTO customer (c_name) VALUES (?)", (name,))
            con.commit()
            cursor.execute("SELECT @@IDENTITY")
            c_id = cursor.fetchone()[0]
            print("Customer Created with ID:", c_id)
        except:
            print('Enter valid records')
        return c_id

class Order:
    #define `t_o()`
    def take_order(self, c_id):
        '''
        Docstring for take_order
        This function takes the order
         '''
        cursor = con.cursor()
        while True:
            print("\n------ MENU ------")
            cursor.execute("SELECT * FROM menu")
            records = cursor.fetchall()
            for row in records:
                print(row)
            item = input("Enter item name: ")
            cursor.execute("SELECT m_id FROM menu WHERE m_name=?", (item,))
            result = cursor.fetchone()
            if not result:
                print("Invalid item")
                continue
            menu_id = result[0]
            try:
                quantity = int(input("Enter quantity: "))
            except:
                print("Invalid quantity")
                continue
            cursor.execute(
                "INSERT INTO orders (quant, menu_id, c_id) VALUES (?, ?, ?)",
                (quantity, menu_id, c_id)
            )
            con.commit()
            try:
                more = input("Add more items? (Y/N): ")
                if more.upper() != 'Y':
                    break
            except:
                print('Invalid Input')
class Bill:
    #define `g_bill()`
   def generate_bill(self, c_id):
        '''
        Docstring for generate_bill
        This function generates the bill
        '''
        cursor = con.cursor()
        cursor.execute("""
            SELECT m.m_name, o.quant, m.m_price
            FROM orders o
            JOIN menu m ON o.menu_id = m.m_id
            WHERE o.c_id = ?
        """, (c_id,))
        records = cursor.fetchall()
        timestamp = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
        if not records:
            print("No orders found")
            return
        print("\n" + "="*50)
        print("                 FINAL BILL")
        print("="*50)
        print(f"{'Customer ID : ' + str(c_id):<30}{timestamp:>20}\n")
        print("-"*50)
        print(f"{'No':<5}{'Item Name':<20}{'Qty':<8}{'Price':<8}{'Total':<8}")
        print("-"*50)
        total = 0
        for i, row in enumerate(records, start=1):
            item_total = row[1] * row[2]
            total += item_total
            print(f"{i:<5}{row[0]:<20}{row[1]:<8}{row[2]:<8}{item_total:<8}")
        print("-"*50)
        print(f"{'':<33}Grand Total : {total}")
        print("="*50)
        
        #define `p_bill()`
    def print_bill(self, c_id):
        '''
        Docstring for print_bill
        This function prints the bill into the file 
        '''
        cursor = con.cursor()
        cursor.execute("""
            SELECT m.m_name, o.quant, m.m_price
            FROM orders o
            JOIN menu m ON o.menu_id = m.m_id
            WHERE o.c_id = ?
        """, (c_id,))
        records = cursor.fetchall()
        if not records:
            print("No orders found")
            return
        path = r"E:\BIZMETRIC_TRAINING\PYTHON\daily_practice"
        timestamp = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
        filename = os.path.join(path, f"Bill_{timestamp}.txt")
        total = 0
        with open(filename, "w") as f:
            f.write("="*50 + "\n")
            f.write("              HOTEL BILL\n")
            f.write("="*50 + "\n")
            f.write(f"{'Customer ID : ' + str(c_id):<30}{timestamp:>20}\n")
            f.write("-"*50 + "\n")
            f.write(f"{'No':<5}{'Item Name':<20}{'Qty':<8}{'Price':<8}{'Total':<8}\n")
            f.write("-"*50 + "\n")
            for i, row in enumerate(records, start=1):
                item_total = row[1] * row[2]
                total += item_total
                f.write(f"{i:<5}{row[0]:<20}{row[1]:<8}{row[2]:<8}{item_total:<8}\n")
            f.write("-"*50 + "\n")
            f.write(f"{'':<33}Grand Total : {total}\n")
            f.write("="*50 + "\n")
        print("Bill saved at:", filename)
        os.startfile(filename)

if __name__ == "__main__":
    admin = Admin()
    order = Order()
    bill = Bill()

    try:
        choice = input("Do you want to order? (Y/N): ")
        if choice.upper() == "Y":
            c_id = admin.create_customer()
            order.take_order(c_id)
            view = input("Print bill to file? (Y/N): ")
            if view.upper() == "Y":
                bill.print_bill(c_id)
            else:
                bill.generate_bill(c_id)
        else:
            print("Thank you for visiting")
    except:
        print(sys.exc_info())
    finally:
        con.close()
