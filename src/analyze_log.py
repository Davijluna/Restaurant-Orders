def analyze_log(path_to_file):
    if path_to_file != 'csv':
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}")
    # raise NotImplementedError
