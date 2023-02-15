import csv
import os.path


def analyze_log(path_to_file):

    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    if not os.path.exists(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente '{path_to_file}'")


print(analyze_log("data/orders_1.csv"))
