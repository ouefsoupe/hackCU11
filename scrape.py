import requests as req
import json

# angle, grade, quality, placements

list_res = req.get("https://drmzubrwofxyzyhicvvx.supabase.co/rest/v1/climbs?select=*&order=total_ascents.desc.nullslast&offset=0", 
                   headers={"apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzMTI3NDA1MiwiZXhwIjoxOTQ2ODUwMDUyfQ.vBZ8uBgVI3Wc9RaJ2STinaVnd0dY2HHyK42YkqBxUR0",
                            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzMTI3NDA1MiwiZXhwIjoxOTQ2ODUwMDUyfQ.vBZ8uBgVI3Wc9RaJ2STinaVnd0dY2HHyK42YkqBxUR0"})

uuid_list = list_res.json()
with open("climbs.json", 'w') as f:
    f.write("[\n")
    for climb in uuid_list:

        climb_data = {
            "placements": climb['placements']
        }
        f.write("    %s,\n" % json.dumps(climb_data))

    f.write("]")
