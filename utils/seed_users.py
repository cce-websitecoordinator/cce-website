import csv
from administration.models import GrivenceUser


def seed_database():
    csv_file_path = "static/users.csv"
    try:
        with open(csv_file_path, "r") as csvfile:
            csv_reader = csv.DictReader(csvfile)

            for row in csv_reader:
                GrivenceUser.objects.create(
                    name=row["name"],
                    email=row["email"],
                    password=row["password"],
                    type="student",
                )
        return "Seeding Successful"
    except FileNotFoundError as e:
        return f"Error: CSV file not found - {e}"
    except csv.Error as e:
        return f"Error reading CSV file - {e}"
    except Exception as e:
        print(e)
        return f"Unexpected error: {e}"

