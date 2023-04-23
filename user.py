import sqlite3
import datetime
from main import Person

print("__________________________\n Evidence pojištěných \n __________________________")

#zobrazí datum a čas
now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Dnešní datum a čas: ")
print(formatted_date)

#vybrat úkon
print("Vyberte si akci: \n"
    "1 - Přidat nového pojistného \n"
    "2 - Vypsat všechny pojistné \n"
    "3 - Vyhledat pojistného \n"
    "4 - Konec")


ukon = int(input("Zadej zde: "))

#přidej osobu
if ukon == 1:
    id_number = int()
    first_name = input("Zadej křestní jméno osoby: ")
    last_name = input("Zadej přijmení osoby: ")
    age = int(input("Zadej věk osoby: "))
    phone = int(input("Zadej tel.číslo: "))
    p1 = Person(id_number, first_name, last_name, age, phone)
    p1.insert_person()
    print("Osoba byla úspěšně přidána do databáze.")

#vypsat všechny osoby
if ukon == 2:
    connection = sqlite3.connect('Evidence_pojištění')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM persons")
    result = cursor.fetchall()
    for row in result:
        print(row)
        print()  # rozdělí řádky pro lepší čitelnost


    connection.close()

#vyhledat podle jména
if ukon == 3:
    connection = sqlite3.connect('Evidence_pojištění')
    first_name = input("Vložte křestní jméno uživatele: ")
    last_name = input("Vložte přijmení uživatele: ")

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM persons WHERE first_name = ? AND last_name = ?', (first_name, last_name,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

#ukončit program
if ukon == 4:
    print("Program bude okončen.")
    quit()





