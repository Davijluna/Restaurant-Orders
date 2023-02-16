import csv
import os.path
# from collections import Counter


def read(path_to_file):
    with open(path_to_file, encoding="utf-8") as read_csv:
        conteudos = csv.reader(read_csv, delimiter=",", quotechar='"')
        conteudos_list = []
        for index in conteudos:
            conteudos_list.append(index)
        return conteudos_list


def func_max_orders(client, orders):
    dishes = {}

    for customer, dish, _ in orders:
        if customer == client:
            if dish in dishes:
                dishes[dish] += 1
            else:
                dishes[dish] = 1
    return max(dishes.items(), key=lambda x: x[1])[0]


def analyze_log(path_to_file):

    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    if not os.path.exists(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente '{path_to_file}'")
    # result = get_unique_analyze(path_to_file)
    orders = read(path_to_file)
    max_orders = func_max_orders("maria", orders)
    # quantid_never = func_quantid_never()
    return max_orders


print(analyze_log("data/orders_1.csv"))
