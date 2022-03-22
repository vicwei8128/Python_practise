import json

data = {"drink": [{"hot": {"coffee": 100, "tea": 90}},
                  {"juice": {"apple": 95, "banana": 85}}],
        "table": ["", "A01", "A02", "A03", "A04", "A05"]
        }

file_a = open("file_name_JJJ.json", "w")
json.dump(data, file_a)
file_a.close()