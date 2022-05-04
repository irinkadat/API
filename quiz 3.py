# task 1
import requests
import json
import sqlite3


# spoonacular api

key = '15d3f9db070e4b7980dd731441e1b04f'
r = requests.get(f'https://api.spoonacular.com/recipes/complexSearch?apiKey={key}&query=pasta&maxFat=25&number=2')
print(r.status_code)  # სერვერიდან მიღებული პასუხის სტატუსი
print(r.headers)  # სერვერიდან მიღებული პასუხის დამატებითი ინფორმაცია. მაგ. სერვერის დასახლება, კონტენტის ტიპი, ა.შ. შედეგი არის dict ტიპის
print(r.text)  # შიგთავსის დაბეჭდვა ტექსტის სახით
result = r.json()  # გადაყავს dictionary-ში
print(result)

# task 2
with open('Data.json', 'w') as file:
    json.dump(result, file, indent=4)
print(file)

# task 3
# spoonacular.com-იდან API-ს მეშვეობით მომაქვს ჩემთვის სასურველი კერძის რეცეპტი.
key = '15d3f9db070e4b7980dd731441e1b04f'
query = input('enter dishes:')
maxFat = float(input('enter maxFat:'))
number = int(input('enter number of dishes:'))
payload = {'apiKey': key, 'query': query, 'maxFat': maxFat, 'number': number}
r = requests.get(f'https://api.spoonacular.com/recipes/complexSearch', params=payload)
res = json.loads(r.text)
print(res)
title = res['results'][0]['title']
image = res['results'][0]['image']
fat = res['results'][0]['nutrition']['nutrients'][0]['amount']
print(title) #დაბეჭდავს კერძის დასახელებას


# task 4 შევქმენი ბაზა სადაც შევიტანე იმ კერძის ინფორმაცია(კერძის დასახელება, ფოტოს url, ცხიმის შემცველობა), რომელიც წამოვიღე spoonacular.com-დან
conn = sqlite3.connect('data.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE if not exists dish(id integer primary key AUTOINCREMENT,
                 title TEXT, image TEXT, fat FLOAT )''')
cursor.execute("INSERT INTO dish(title, image, fat) VALUES (?, ?, ?)", (title, image, fat))
conn.commit()
conn.close()






#  wrapper (დამატებითი)
import spoonacular as sp

api = sp.API("15d3f9db070e4b7980dd731441e1b04f")

# Parse an ingredient
response = api.parse_ingredients("3.5 cups King Arthur flour", servings=1)
data = response.json()
print(data[0]['name'])
# >>>"flour"

# Detect text for mentions of food
response = api.detect_food_in_text("I really want a cheeseburger.")
data = response.json()
print(data['annotations'][0])
# >>>{"annotation": "cheeseburger", "tag":"dish"}

# Get a random food joke
response = api.get_a_random_food_joke()
data = response.json()
print(data['text'])
# >>>"People are a lot less judgy when you say you ate an 'avocado salad' instead of a bowl of guacamole."
