import configparser

def load_config(path):
    config = configparser.ConfigParser()
    config.read(path, encoding="utf-8")
    count = int(config["general"]["simulations"])
    return [dict(config[f"sim{i}"]) for i in range(1, count + 1)]