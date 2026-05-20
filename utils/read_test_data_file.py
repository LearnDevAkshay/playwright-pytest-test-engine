import csv
from pathlib import Path


class TestDataReader:

    @staticmethod
    def read_all_csv_by_test_case(folder_path, test_case_name):
        test_data_list = []
        folder_path = Path(folder_path)

        # Get all .csv files in the folder
        csv_files = folder_path.glob("*.csv")

        for csv_file in csv_files:
            with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row.get("test_cases", "").strip().lower() == test_case_name.strip().lower():
                        print(row)
                        test_data_list.append(row)

        return test_data_list