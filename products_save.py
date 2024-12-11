'''
products_save.PY: Här så skapas csv filen med alla produkter

__author__  = "Linus Norling"
__version__ = "1.0.0"
__email__   = "linus.norling2@elev.ga.ntig.se"
'''

import csv

products = [
    {
        "id": 1,
        "name": "Cuddly Bear Plush",
        "desc": "A soft and fluffy bear plush toy perfect for hugging.",
        "price": 29.99,
        "quantity": 150
    },
    {
        "id": 2,
        "name": "Fuzzy Bunny Stuffed Animal",
        "desc": "A cute bunny stuffed animal with long ears and a soft coat.",
        "price": 19.99,
        "quantity": 75
    },
    {
        "id": 3,
        "name": "Rainbow Unicorn Plush",
        "desc": "A colorful unicorn plush toy with a shiny mane and tail.",
        "price": 39.99,
        "quantity": 50
    },
    {
        "id": 4,
        "name": "Panda Bear Cuddle Toy",
        "desc": "An adorable panda bear stuffed animal with soft black and white fur.",
        "price": 25.99,
        "quantity": 200
    },
    {
        "id": 5,
        "name": "Teddy Bear Deluxe",
        "desc": "A classic teddy bear plush with a ribbon around its neck.",
        "price": 49.99,
        "quantity": 120
    },
    {
        "id": 6,
        "name": "Koala Snuggle Plush",
        "desc": "A cute koala stuffed animal that is perfect for snuggling.",
        "price": 34.99,
        "quantity": 80
    },
    {
        "id": 7,
        "name": "Fluffy Tiger Plush",
        "desc": "A tiger stuffed animal with soft fur and a playful expression.",
        "price": 39.99,
        "quantity": 90
    },
    {
        "id": 8,
        "name": "Penguin Buddy Stuffed Toy",
        "desc": "A little penguin stuffed toy with a cute belly and tiny flippers.",
        "price": 19.99,
        "quantity": 140
    },
    {
        "id": 9,
        "name": "Elephant Plush Friend",
        "desc": "A big, soft elephant plush with large ears and a friendly face.",
        "price": 59.99,
        "quantity": 110
    },
    {
        "id": 10,
        "name": "Giraffe Snuggle Toy",
        "desc": "A tall, soft giraffe plush with long neck and cute spots.",
        "price": 44.99,
        "quantity": 95
    },
    {
        "id": 11,
        "name": "Sloth Plush Cuddle Buddy",
        "desc": "A relaxed sloth plush with a cozy, fuzzy feel.",
        "price": 29.99,
        "quantity": 130
    }
]

# Define the CSV file path
csv_file_path = "db_stuffed_animals.csv"

# Write the products data to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "desc", "price", "quantity"])
    writer.writeheader()  # Write the header row
    writer.writerows(products)  # Write the product data

print(f"Data successfully saved to {csv_file_path}")