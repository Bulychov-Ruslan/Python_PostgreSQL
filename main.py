import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="your_password_database",
        database="your_database_name"
    )
    cursor = connection.cursor()
    connection.autocommit = True

    def select():
        print("SELECT:")
        coloum = input("Кесте бағандарын енгіз: ")
        table = input("Кесте аты: ")
        func = input("Функция енгіз: ")
        cursor.execute(f'SELECT {coloum} FROM "{table}" {func};')
        records = cursor.fetchall()
        for row in records:
            print(row)

    def insert():
        print("INSERT: ")
        table = input("Кесте аты: ")
        for func in range(5):
            func = input("Ақпаратты енгіз: ")
            cursor.execute(f'INSERT INTO "{table}" VALUES ({func});')
            print("INSERT SUCCESS!!!")

    def update():
        print("UPDATE: ")
        table = input("Кесте аты: ")
        func = input("Өзгертетін баған аты: ")
        func2 = input("ID нөмері: ")
        cursor.execute(f'UPDATE "{table}" SET {func} WHERE {func2};')
        print("UPDATE SUCCESS!!!")

    def delete():
        print("DELETE: ")
        table = input("Кесте аты: ")
        func = input("ID нөмері: ")
        cursor.execute(f'DELETE FROM "{table}" WHERE {func};')
        print("DELETE SUCCESS!!!")

    def create():
        print("CREATE TABLE: ")
        table = input("Кесте аты: ")
        func = input("Баған аттары мен айнымалылар: ")
        cursor.execute(f'CREATE TABLE "{table}" ({func});')
        print("CREATE SUCCESS!!!")

    def tapsir8():
        print("8-тапсырма:")
        func = input("Атын енгіз: ")
        cursor.execute(f"""SELECT s."FirstName", s."LastName", s."Addr1", s."City", s."Country", s."Email", co."CourseName", co."CourseDesc", co."Credits" 
                            FROM "Students" as s 
                            JOIN "StuClasses" as st ON st."StudentID" = s."StudentID" 
                            JOIN "Classes" as cl ON cl."ClassID" = st."ClassID"
                            JOIN "Courses" as co ON co."CourseID" = cl."CourseID"
                            WHERE s."FirstName" = '{func}'""")
        records = cursor.fetchall()
        for row in records:
            print(row)
        func2 = input("Курс атын енгіз: ")
        cursor.execute(f"""SELECT s."FirstName", s."LastName", s."Addr1", s."City", s."Country", s."Email", co."CourseName", co."CourseDesc", co."Credits" 
                            FROM "Students" as s
                            JOIN "StuClasses" as st ON st."StudentID" = s."StudentID"
                            JOIN "Classes" as cl ON cl."ClassID" = st."ClassID"
                            JOIN "Courses" as co ON co."CourseID" = cl."CourseID"
                            WHERE co."CourseName" = '{func2}'""")
        records = cursor.fetchall()
        for row in records:
            print(row)

    def main():
        print(" 1-SELECT;\n 2-INSERT;\n 3-UPDATE;\n 4-DELETE;\n 5-CREATE;\n 6-8-тапсырма; ")
        cmd = input("Введите команду: ")
        while cmd != "Exit":
            if cmd == "1":
                select()

            elif cmd == "2":
                insert()

            elif cmd == "3":
                update()

            elif cmd == "4":
                delete()

            elif cmd == "5":
                create()

            elif cmd == "6":
                tapsir8()

            else:
                print("ERROR")
            print(" \n 1-SELECT;\n 2-INSERT;\n 3-UPDATE;\n 4-DELETE;\n 5-CREATE; \n 6-8-тапсырма;")
            cmd = input("Введите команду: ")
        return
    main()

except Exception as _ex:
    print(" ERROR CONNECT", _ex)

finally:
    connection.close()
    print("[INFO] PostgreSQL connection closed")
