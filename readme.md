# Python exercise to find which tag has the most get operations associated
## QUESTION
Create a function that takes an openAPI JSON document as input and produces a dictionary. The dictionary should map tags to a list of GET operationId that are tagged with that specific tag.

Other types of operations such as "post" or "delete" should not be considered. 

Read weather.json and use the output of get_tags_to_get_operations to find which tag has the most get operations associated and print it. 



Example

---

INPUT:
```
{
  "openapi": "3.0.0",
  "info": {
    "version": "1.0.0",
    "title": "Swagger Petstore",
    "license": {
      "name": "MIT"
    }
  },
  "paths": {
    "/pets": {
      "get": {
        "summary": "List all pets",
        "operationId": "listPets",
        "tags": [
          "pets"
        ],
        "parameters": [...],
        "responses": {...}
      }
    },
    "/owner": {
      "get": {
        "summary": "List all owners",
        "operationId": "listOwners",
        "tags": [
          "owner"
        ],
        "parameters": [...],
        "responses": {...}
      }
    },
    "/dogs": {
      "get": {
        "summary": "List all dogs",
        "operationId": "listDogs",
        "tags": [
          "pets"
        ],
        "parameters": [...],
        "responses": {...}
      }
    }
  },
  "components": {...}
}
```

OUTPUT:
```
{"pets": ["listPets", "listDogs"], "owner": ["listOwner"]}
```

## SOLUTION
Extract the tags associated with GET operations, and determine which tag has the most GET operations:

```python
import json

def get_tags_to_get_operations(data: dict) -> dict:
    tag_to_get_operations = {}

    for path, methods in data.get("paths", {}).items():
        if 'get' in methods:
            tags = methods['get'].get('tags', [])
            for tag in tags:
                if tag not in tag_to_get_operations:
                    tag_to_get_operations[tag] = []
                tag_to_get_operations[tag].append(path)
    
    return tag_to_get_operations

# Load the JSON data (replace with the actual path if needed)
with open('weather.json', 'r') as file:
    data = json.load(file)

# Get the tag to GET operations mapping
tag_to_operations = get_tags_to_get_operations(data)

# Find the tag with the most GET operations
max_tag = None
max_operations = 0

for tag, operations in tag_to_operations.items():
    if len(operations) > max_operations:
        max_operations = len(operations)
        max_tag = tag

print(f"Tag with most GET operations: {max_tag} with {max_operations} operations")
```

### Explanation:
1. **Function `get_tags_to_get_operations(data)`**:
   - Iterates through each path and its methods in the OpenAPI JSON document.
   - Checks if the method is a 'GET'.
   - Extracts the tags associated with the 'GET' method and maps them to the corresponding paths.

2. **Loading the JSON**:
   - Opens the `weather.json` file and loads its content into a Python dictionary.

3. **Determining the Tag with Most GET Operations**:
   - Iterates through the dictionary returned by `get_tags_to_get_operations`.
   - Tracks which tag has the most associated GET operations and prints it.

This code will read the JSON, process the data, and print the required result. Ensure the `weather.json` file is correctly placed in the same directory as the script or provide the correct path to it.

### Complexity
Let  P  be the number of paths,  T  be the average number of tags per ‘GET’ method and  K  unique tags.
- **Time Complexity:** \( O(P x T + K) \)
- **Space Complexity:** \( O(P + K) \)