import requests as req
import json
import time

# angle, grade, quality, placements

MAXPAGES = 23
dropped_count = 0
total_count = 0

with open("climbs.json", 'w') as f:
    f.write("[\n")
    for offset in range(0, MAXPAGES*1000, 1000):
        time.sleep(1)
        list_res = req.get("https://drmzubrwofxyzyhicvvx.supabase.co/rest/v1/climbs?select=*&order=total_ascents.desc.nullslast&offset=%s" % offset, 
                        headers={"apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzMTI3NDA1MiwiZXhwIjoxOTQ2ODUwMDUyfQ.vBZ8uBgVI3Wc9RaJ2STinaVnd0dY2HHyK42YkqBxUR0",
                                    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzMTI3NDA1MiwiZXhwIjoxOTQ2ODUwMDUyfQ.vBZ8uBgVI3Wc9RaJ2STinaVnd0dY2HHyK42YkqBxUR0"})
        if (list_res.status_code != 200): 
            print("Stopped at i=%s" % (offset/1000))
            break
        print("On page %s/%s" % (int(offset/1000)+1, MAXPAGES))

        uuid_list = list_res.json()
        total_count += len(uuid_list)
        for climb in uuid_list:
            angle_index = -1
            for i in range(0, len(climb['climb_stats'])):
                angle = climb['climb_stats'][i]['angle']
                if (40 <= angle <= 45):
                    angle_index = i
                    break
            if (angle_index == -1): 
                dropped_count += 1
                continue

            climb_data = {
                "difficulty": climb['climb_stats'][angle_index]['difficulty_average'],
                "placements": climb['placements']
            }
            f.write("    %s,\n" % json.dumps(climb_data))
    f.write("]")

print("Found %s runs, dropped %s" % (total_count, dropped_count))