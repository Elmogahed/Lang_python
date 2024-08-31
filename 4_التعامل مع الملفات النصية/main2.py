import json

task = [
    {"id": 1, "title":"Study For 4 hours", "done": False},
    {"id": 2, "title":"Study For 30 hours", "done": True},
    {"id": 3, "title":"Study For  hours", "done": False},
]

with open('tasks.json', 'w') as write_file: 
    json.dump(task, write_file)

print("=" * 50)
json_tasks = json.dumps(task)
print(json_tasks)
print(type(json_tasks))

data = """
[
      {
       "id": 1, 
       "title": "Recorde a new video",
       "completed": false
      },
      {
       "id": 1, 
       "title": "Recorde a new video",
       "completed": false
      }

]
"""
todos = json.loads(data)
print(todos)



with open('data.json', 'r') as data_file: 
    data = json.load(data_file)

print(data)
print(data[0])
print(data[0]['url'])

capitals = ("Bagdad", "Riadh", "Cairo", "Damuscus", "Dubi")
capitals_encoded = json.dumps(capitals) # تحويل القوائم والصفوف إلى مصفوفات من بايثون إلى جسون
print(capitals_encoded) 
capitals_decoded = json.loads(capitals_encoded) #  تحويل المصفوفات إلى قوائم في من جسون إلى لغة بايثون 
print(capitals_decoded)

print(type(capitals))
print(type(capitals_decoded))