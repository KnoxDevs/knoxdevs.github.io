import pyaml
import yamlloader
import json
from collections import OrderedDict
import re

'''
Code to do custom nested sorting from https://stackoverflow.com/a/25024193 / https://github.com/laowantong/customsort
'''
def to_ascii(s):
    return unicodedata.normalize('NFD', s.lower()).encode('ASCII', 'ignore')

def make_custom_sort(orders):
    orders = [{k: -i for (i, k) in enumerate(reversed(order), 1)} for order in orders]
    def process(stuff):
        if isinstance(stuff, dict):
            l = [(k, process(v)) for (k, v) in stuff.items()]
            keys = set(stuff)
            order = max(orders, key=lambda order: len(keys.intersection(order)))
            order.update({key:i for (i, key) in enumerate(sorted(keys.difference(order), key=to_ascii), 1)})
            return OrderedDict(sorted(l, key=lambda x: order[x[0]]))
        if isinstance(stuff, list):
            return [process(x) for x in stuff]
        return stuff
    return process

'''
end code
'''

if __name__ == '__main__':
    with open('.migrations/bloggers.json', 'r') as f:
        bloggers = json.load(f)

    names = []
    yml_array = []

    for blogger in bloggers.items():
        yml_data = {'name':'', 'image':'', 'description':'', 'online':{'website': '', 'feed':''}, 'social': {'twitter':'', 'github':''}}
        print(blogger[0])
        yml_data['name'] = blogger[0]
        names.append(re.sub(' ', '', blogger[0].lower())) #lower case and remove space between first and last name for file naming.
        yml_data['social']['twitter'] = blogger[1]['twitter']
        yml_data['online']['website'] = blogger[1]['websiteurl']
        yml_data['online']['feed'] = blogger[1].get('rss', '') # there are 3 entries that don't have 'rss'
        yml_array.append(yml_data)

    order_yml = make_custom_sort([ ['name', 'image', 'description', 'online', 'social'], ['website', 'feed', 'twitter', 'github'] ])

    for position, name in enumerate(names):
        yml_ordered = order_yml(yml_array[position])
        with open("_data/bloggers/{}.yml".format(name), 'w') as f: #going to write to each individual file
            yml_ordered_minus_comma = re.sub('\'','', pyaml.dump(yml_ordered, indent = 4, vspacing=[1, 0]))# clean ', ensure that indents are 4 spaces, and we add a line break between top level keys.
            yml_to_write = re.sub('\"', '', yml_ordered_minus_comma)# clean "
            f.write(yml_to_write)