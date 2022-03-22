import os
import json

save_file_dir = "file_dir"

if save_file_dir not in os.listdir("."):
    os.mkdir("./" + save_file_dir)

data = {"table": ["", "A01", "A02", "A03","A04"]}
file_a = open(save_file_dir + "/file_name_JJJ.json", "w")
json.dump(data, file_a)
file_a.close()
