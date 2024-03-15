from database import Database


def tables():
    menuTable = f"""
        CREATE TABLE menu(
            menu_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            create_date TIMESTAMP DEFAULT now())"""

    orderTable = f"""
            CREATE TABLE orders(
                order_id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                create_date TIMESTAMP DEFAULT now())"""

    data = {
        "menuTable":menuTable,
        "orderTable":orderTable
    }

    for i in data:
        print(f"{i} - {Database.connect(data[i], "create")}")

#
# if __name__ == "__main__":
#     tables()