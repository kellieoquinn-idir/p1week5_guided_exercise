import csv
from sqlalchemy import text
from database import engine  # type: ignore

def main() -> None:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM products"))
        headers = result.keys()
        rows = result.fetchall()

    with open("products.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)

if __name__ == "__main__":
    main()
       