import logging

from src.optimizely.optimizely import Optimizely

sdk = Optimizely("http://localhost:62088/api/episerver/v2.0", logging)

for i in range(10):
    c = sdk.content.get_single(str(i))
    print((c.name,c.id) if c else "?")

sites = sdk.sites.get()
for s in sites:
    print("site:" + s.name)
    for l in s.languages:
        print("\t" + l.name)

site_id = sites[0].id
site = sdk.sites.get(site_id)
print("done")
