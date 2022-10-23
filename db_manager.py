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
            values.append(f'("{ingredient.lower()}")')
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
            values.append(f'("{ingredient.lower()}")')
        with connection.cursor() as cursor:
            query = f"INSERT ignore into gluten_ingredients(name) values{','.join(values)};"
            cursor.execute(query)
            connection.commit()
    except:
        print("DB Error")


def get_dairy_ingredients():
    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM dairy_ingredients;"
            cursor.execute(query)
            results = cursor.fetchall()
            dairy_ingredients = []
            for res in results:
                dairy_ingredients.append(res["name"])
            return (dairy_ingredients)
    except:
        print("DB Error")


def get_gluten_ingredients():
    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM gluten_ingredients;"
            cursor.execute(query)
            results = cursor.fetchall()
            gluten_ingredients = []
            for res in results:
                gluten_ingredients.append(res["name"])
            return (gluten_ingredients)
    except:
        print("DB Error")
