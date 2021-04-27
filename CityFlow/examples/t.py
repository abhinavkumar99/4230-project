import cityflow
import json
from tqdm import tqdm

config = {
    "interval": 1.0,
    "seed": 0,
    "dir": "./",
    "roadnetFile": "roadnet_1_1.json",
    "flowFile": "flow_1_1.json",
    "rlTrafficLight": False,
    "saveReplay": True,
    "laneChange": True,
    "roadnetLogFile": "log.json",
    "replayLogFile": "log.txt"
}

with open('config.json', 'w') as fp:
    json.dump(config, fp)

config_path = 'config.json'
eng = cityflow.Engine(config_path, thread_num=1)


for i in tqdm(range(300)):
    # print(i)
    # print("Vehicle count: ",eng.get_vehicle_count())
    eng.next_step()
print("Average travel time:",eng.get_average_travel_time())