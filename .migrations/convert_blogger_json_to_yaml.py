import yaml
import json

with open('bloggers.json', 'r') as f:
    bloggers = json.load(f)

print(bloggers)