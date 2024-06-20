import json
def get_tags_to_get_operations(data: dict)-> dict[str,list[str]]:
  tags_to_get_operations = {}

  for path, methods in data.get("paths",{}).items():
    if 'get' in methods:
      tags = methods['get'].get('tags', [])
      for tag in tags:
        if tag not in tags_to_get_operations:
          tags_to_get_operations[tag] = []
        tags_to_get_operations[tag].append(path)
  return tags_to_get_operations

with open('weather.json', 'r') as file:
  data = json.load(file)

tags_to_operations = get_tags_to_get_operations(data)

# print(tags_to_get_operations)
# find the tag with most GET operation
max_tag = None
max_operations = 0

for tag, operations in tags_to_operations.items():
  if len(operations) > max_operations:
    max_operations = len(operations)
    max_tag = tag

print(f"Tag with most GET operations: {max_tag} with {max_operations} operations.")