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
        time.sleep(0.1)
        list_res = req.get("https://drmzubrwofxyzyhicvvx.supabase.co/rest/v1/climbs?select=*&order=total_ascents.desc.nullslast&offset=%s" % offset, 
                        headers={"apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzMTI3NDA1MiwiZXhwIjoxOTQ2ODUwMDUyfQ.vBZ8uBgVI3Wc9RaJ2STinaVnd0dY2HHyK42YkqBxUR0",
                                    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzMTI3NDA1MiwiZXhwIjoxOTQ2ODUwMDUyfQ.vBZ8uBgVI3Wc9RaJ2STinaVnd0dY2HHyK42YkqBxUR0"})
        if (list_res.status_code != 200): 
            print("Stopped at i=%s" % (offset/1000))
            break
        print("On page %s/%s" % (int(offset/1000)+1, MAXPAGES))

        uuid_list = list_res.json()
        for climb in uuid_list:
            angle_index = -1
            has_null_led = False
            for hold in climb['placements']:
                if (hold['ledPosition'] == None): 
                    has_null_led = True
                    break
            if (has_null_led): continue
            total_count += 1

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



curr_hold
next_hold

rel_x = next_hold[0] - curr_hold[0] + RADIUS
rel_y = next_hold[1] - curr_hold[1] + RADIUS
index = rel_y * (2*RADIUS + 1) + rel_x

start_x, start_y = 0, 0
for placement in climb['placements']:
    if ('type' in placement and placement['type'] == 'START'):
        start_x = placement['x']
        start_y = placement['y']
        break
climb['placements'] = climb['placements'].sort(key=lambda e: np.abs(['x']-start_x + (e['y']-start_y)**2))