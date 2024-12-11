'''
open.py: Här så öppnar man csv filen för att kunna ta bort, visa, lägga till eller ändra produkterna i csv filen

__author__  = "Linus Norling"
__version__ = "1.0.0"
__email__   = "linus.norling2@elev.ga.ntig.se"
'''

import csv
import os
import locale
from time import sleep


def load_data(filename): 
    products = [] 
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(        #list
                {                    #dictionary
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products


def add_product(products, name, desc, price, quantity):
    max_id = max(products, key=lambda x: x["id"])

    id_value = max_id["id"]

    id = id_value + 1

    products.append(
        {
            "id": id,
            "name": name,
            "desc": desc,
            "price": price,
            "quantity": quantity
        }
    )
    return f'Lade till produkt: {id}'

def edit_product(product, name, desc, price, quantity):
    product["name"] = name
    product["desc"] = desc
    product["price"] = price
    product["quantity"] = quantity
    
def remove_product(products, id):
    temp_product = None

    for product in products:
        if product["id"] == id:
            temp_product = product
            break  # Avsluta loopen så snart produkten hittas

    if temp_product:
        products.remove(temp_product)
        return f"Product: {id} {temp_product['name']} was removed"
    else:
        return f"Product with id {id} not found"


def view_product(products, id):
    # Go through each product in the list
    for product in products:
        # Check if the product's id matches the given id
        if product["id"] == id:
            # If it matches, return the product's name and description
            return f"Visar produkt: {product['name']} {product['desc']}"
    
    # If no matching product is found, return this message
    return "Produkten hittas inte"


def view_products(products):
    product_list = []
    for index, product in enumerate(products, 1):
        product_info = f"{index}) (#{product['id']:<5}) {product['name']:<15} \t {product['desc']:<50} \t {str(locale.currency(product['price'], grouping=True)):<10} \t Quantity: {product['quantity']}"
        product_list.append(product_info)
    
    return "\n".join(product_list)


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls' if os.name == 'nt' else 'clear')
products = load_data('db_stuffed_animals.csv')
while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(view_products(products))  # Show ordered list of products

        choice = input("Vill du (V)isa, (T)a bort en produkt, (L)ägga till en produkt eller (Ä)ndra en produkt? ").strip().upper()

        if choice == "L":
            name = input("Namn på produkten: ")
            desc = input("Beskrivning: ")
            price = float(input("Pris: "))
            quantity = int(input("Antal: "))

            print(add_product(products, name, desc, price, quantity))

        if choice in ["V", "T", "Ä"]:
            index = int(input("Enter product ID: "))
            if 1 <= index <= len(products): 
            
                if choice == "Ä":
                    placeholder = products[index - 1]
                    name = input(f"Skriv nytt namn: {placeholder['name']} ")
                    desc = input(f"Skriv ett nytt description: {placeholder['desc']} ")
                    price = float(input(f"Ändra priset på produkten: {placeholder['price']} "))
                    quantity = int(input(f"Skriv hur mycket det finns av produkten: {placeholder['quantity']} "))
                    print(edit_product(placeholder, name, desc, price, quantity))

                
                elif choice == "V":   #visa
                   
                    selected_product = products[index - 1]  # Get the product using the list index
                    id = selected_product['id']  # Extract the actual ID of the product
                    print(view_product(products, id))  # Remove product using the actual ID
                    done = input()
                        
                   

                elif choice == "T": #ta bort
                   
                    selected_product = products[index - 1]  # Get the product using the list index
                    id = selected_product['id']  # Extract the actual ID of the product

                    print(remove_product(products, id))  # Remove product using the actual ID
                    sleep(0.5)            

            else:
                print("Ogiltig produkt")
                sleep(0.3)    
        
    except ValueError:
        print("Välj en produkt med siffor")
        sleep(0.5)

    csv_file_path = "db_stuffed_animals.csv"

    # Write the products data to a CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "desc", "price", "quantity"])
        writer.writeheader()  # Write the header row
        writer.writerows(products)  # Write the product data

    print(f"Data successfully saved to {csv_file_path}")