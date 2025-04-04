from datetime import datetime, timedelta, timezone
from library.csv import write_csv
from library.historian import get_historian_token, get_historian_raw_data

from settings import config


settings = config.settings


def historian_task():
    # Get the token for historian API authentication
    token = get_historian_token()

    heure_utc = datetime.now(timezone.utc)

    end_time = heure_utc.replace(second=0, microsecond=0)
    start_time = end_time - timedelta(minutes=5)
    print(str(heure_utc), str(start_time), str(end_time))
    # Get the raw data from the historian API
    data = get_historian_raw_data(token, start_time, end_time)

    # Format the raw data into a more usable format
    formatted_data = format_historian_data(data)

    # Write the formatted data to a CSV file
    csv_header = ["timestamp", "TagName", "Value"]
    write_csv(csv_header, formatted_data)



def format_historian_data(data: list[dict]):
    float_precision = settings["csv"]["float_precision"]
    formatted_data = []

    if not len(data) > 0:
        return
    
    nb_tags = len(data)
    init = data[0]

    for i, sample in enumerate(init["Samples"]):
        
        date_obj = datetime.strptime( sample["TimeStamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        tmp_timestamp = date_obj.strftime("%d/%m/%Y %H:%M:%S")
        
            
        for tag_id in range(0, nb_tags):
            tag_name = data[tag_id]["TagName"]
            if data[tag_id]["DataType"] == "Float" and float_precision > 0:
                # Round the float value to the specified precision
                tmp_value = round(float(data[tag_id]["Samples"][i]["Value"]), float_precision)
            else:
                tmp_value = data[tag_id]["Samples"][i]["Value"]

            formatted_data.append([tmp_timestamp, tag_name, tmp_value])


    return formatted_data


#  15/06/2023 17:50:00;MW_PRMEI408001;0

# def format_historian_data(data):
#     formatted_data = []

#     nb_samples = len(data)

#     init = data[0]

#     for i, sample in enumerate(init["Samples"]):
#         tmp_data = {
#             "Timestamp": sample["TimeStamp"].replace("T", " ").split(".")[0]
#         }
#         for tag_id in range(0, nb_samples):
#             if data[tag_id]["DataType"] == "Float":
#                 tmp_value = round(float(data[tag_id]["Samples"][i]["Value"]), 2)
#             else:
#                 tmp_value = data[tag_id]["Samples"][i]["Value"]

#             tmp_data[data[tag_id]["TagName"]] = tmp_value

#         formatted_data.append(tmp_data)

#     return formatted_data



