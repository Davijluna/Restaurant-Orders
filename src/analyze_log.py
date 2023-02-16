import csv
import os.path

# FUNÇÃO DE LEITURA


def read(path_to_file):
    with open(path_to_file, encoding="utf-8") as read_csv:
        conteudos = csv.reader(read_csv, delimiter=",", quotechar='"')
        conteudos_list = []
        for index in conteudos:
            conteudos_list.append(index)
        return conteudos_list


# Retorna Qual o prato mais pedido por 'maria'


def func_max_orders(client, orders):
    dishes = {}

    for customer, dish, _ in orders:
        if customer == client:
            if dish in dishes:
                dishes[dish] += 1
            else:
                dishes[dish] = 1
    return max(dishes.items(), key=lambda x: x[1])[0]


# Retorna Quantas vezes 'arnaldo' pediu 'hamburguer'

def quantit_ordered_dish(custumer, dish, orders):
    times = {}

    for client, dish, _ in orders:
        if client == custumer:
            if dish in times:
                times[dish] += 1
            else:
                times[dish] = 1
    return times[dish]

# Retorna Quais pratos 'joao' nunca pediu


def func_quantid_never(client, orders):
    all_food = set()
    ordered_fod = set()

    for customer, dish, _ in orders:
        all_food.add(dish)

    for customer, dish, _ in orders:
        if customer == client:
            ordered_fod.add(dish)

    return all_food - ordered_fod

# Retorna Quais dias 'joao' nunca foi à lanchonete


def func_never_was(client_name, orders):
    all_days = set()
    days_never_was = set()

    for _, _, weekday in orders:
        all_days.add(weekday)

    for customer, _, day in orders:
        if customer == client_name:
            days_never_was.add(day)

    return all_days - days_never_was


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    if not os.path.exists(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente '{path_to_file}'")
    # result = get_unique_analyze(path_to_file)
    orders = read(path_to_file)
    max_orders = func_max_orders("maria", orders)
    times_ordered = quantit_ordered_dish("arnaldo", "hamburguer", orders)
    quantid_never = func_quantid_never("joao", orders)
    never_was = func_never_was("joao", orders)

    # return quantid_never

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(f"{max_orders}\n")
        file.write(f"{times_ordered}\n")
        file.write(f"{quantid_never}\n")
        file.write(f"{never_was}")


print(analyze_log("data/orders_1.csv"))
