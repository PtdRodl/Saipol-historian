import csv
from datetime import datetime
import os

from settings import config


settings = config.settings

def write_csv(header,data):
    file_directory = settings["csv"]["directory"]
    file_base_name = settings["csv"]["base_name"]
    file_time = datetime.now().strftime("%d-%m-%YT%H_%M_%S")
    # file_time = ""
    file_extension = settings["csv"]["extension"]

    file_name = f"{file_directory}/{file_base_name}-{file_time}.{file_extension}"

    directory = os.path.dirname(file_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        # Write the header
        header = ["heure", "variable", "valeur"]
        writer.writerow(header)
        # Write the data
        writer.writerows(data)

