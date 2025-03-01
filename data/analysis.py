import requests as req
import json
import time
        

list_res = req.get("https://drmzubrwofxyzyhicvvx.supabase.co/rest/v1/climbs?select=*&order=total_ascents.desc.nullslast&offset=2000",
    headers={"apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzMTI3NDA1MiwiZXhwIjoxOTQ2ODUwMDUyfQ.vBZ8uBgVI3Wc9RaJ2STinaVnd0dY2HHyK42YkqBxUR0",
                "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYW5vbiIsImlhdCI6MTYzMTI3NDA1MiwiZXhwIjoxOTQ2ODUwMDUyfQ.vBZ8uBgVI3Wc9RaJ2STinaVnd0dY2HHyK42YkqBxUR0"})

uuid_list = list_res.json()

min_x, min_y = 1e6, 1e6
max_x, max_y = 0, 0

for climb in uuid_list:
    for placement in climb['placements']:
        if (placement['ledPosition'] == None): continue
        x, y = placement['x'], placement['y']
        if (x > max_x): max_x = x
        if (x < min_x): min_x = x
        if (y > max_y): max_y = y
        if (y < min_y): min_y = y

print("Max x = %s, Max y = %s" % (max_x, max_y))
print("Min x = %s, Min y = %s" % (min_x, min_y))


