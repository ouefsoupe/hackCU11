import requests as req
import json
import time

# angle, grade, quality, placements

MAXPAGES = 150
with open("climbs.json", 'w') as f:
    f.write("[\n")
    for offset in range(0, MAXPAGES*1000, 1000):
        time.sleep(0.1)
        list_res = req.get("https://drmzubrwofxyzyhicvvx.supabase.co/rest/v1/climbs?select=*&order=total_ascents.desc.nullslast&offset=%s" % offset, 
                        headers={"apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzMTI3NDA1MiwiZXhwIjoxOTQ2ODUwMDUyfQ.vBZ8uBgVI3Wc9RaJ2STinaVnd0dY2HHyK42YkqBxUR0",
                                    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzMTI3NDA1MiwiZXhwIjoxOTQ2ODUwMDUyfQ.vBZ8uBgVI3Wc9RaJ2STinaVnd0dY2HHyK42YkqBxUR0"})
        if (list_res.status_code != 200): 
            print("stopped at i=%s" % (offset/1000))
            break
        print("On page %s/%s" % (int(offset/1000), MAXPAGES))

        uuid_list = list_res.json()
        for climb in uuid_list:
            climb_data = {
                "placements": climb['placements']
            }
            f.write("    %s,\n" % json.dumps(climb_data))

    f.write("]")
