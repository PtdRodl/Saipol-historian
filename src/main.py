import time
from library import saipol
import schedule
from settings import config

settings = config.settings

def saipol_task():
    saipol.historian_task()

task_frequency = settings["task"]["frequency"]
schedule.every(task_frequency).seconds.do(saipol_task)

while True:
    schedule.run_pending()
    time.sleep(1)



