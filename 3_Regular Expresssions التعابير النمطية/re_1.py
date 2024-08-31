import re


str = 'Hsoub Academy'
x = 'Hsoub Acadmy'

m = re.match(r'\w+\s\w+', str)
print(m)
h = 'HsoubAcademy'

k = re.match(r'\w+\s\w+', h)
print(k)

print(m.group()) # type: ignore
print(m.start(), m.end()) # type: ignore

l = re.match(r'Academy', str)
print(l)
l = re.search(r'Academy', str)
print(l)

z = re.search(r'Academy', x)
print(z)

message = "mohamed@yhaoo.com"
a = re.search(r'([\w\.]+)@([\w\.]+)', message) 

if a: 
    print(a.group())
else: 
    print('Nothing was found')

if a: 
    print(a.group(1))
else: 
    print('Nothing was found')
if a: 
    print(a.group(2))
else: 
    print('Nothing was found')

a = re.findall(r'([\w\.]+)@([\w\.]+)', message) 

if a: 
    print(a)
else: 
    print('Nothing was found')


text = ""

entries = re.split(r'\n+', text)
print(entries)

phonebook = [re.split(r':? ', entry, 4) for entry in entries]
print(phonebook)