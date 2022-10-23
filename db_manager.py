import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")


def insert_dairy_ingredients(ingredients):
    try:
        values = []
        for ingredient in ingredients:
            values.append(f'("{ingredient}")')
        with connection.cursor() as cursor:
            query = f"INSERT ignore into dairy_ingredients(name) values{','.join(values)};"
            cursor.execute(query)
            connection.commit()
    except:
        print("DB Error")


def insert_gluten_ingredients(ingredients):
    try:
        values = []
        for ingredient in ingredients:
            values.append(f'("{ingredient}")')
        with connection.cursor() as cursor:
            query = f"INSERT ignore into gluten_ingredients(name) values{','.join(values)};"
            cursor.execute(query)
            connection.commit()
    except:
        print("DB Error")
