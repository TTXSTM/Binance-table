import json
from bestchange_api import BestChange

api = BestChange()
exchangers = api.exchangers().get()

dir_from = 185
dir_to = 161
rows = api.rates().filter(dir_from, dir_to)
title = 'Exchange rates in the direction (https://www.bestchange.ru/index.php?from={}&to={}) {} : {}'
print(title.format(dir_from, dir_to, api.currencies().get_by_id(dir_from), api.currencies().get_by_id(dir_to)))


for val in rows[:1]:
    xrp_to_trx = '{} {}'.format(exchangers[val['exchange_id']]['name'], val)
    Excange = str(xrp_to_trx)
    listff = Excange.split()
    excp = listff.strip("giv")
    print(excp)

