def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(shop):
    return shop["admin"]["total_cash"]


def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount


def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]


def increase_pets_sold(shop, amount):
    shop["admin"]["pets_sold"] += amount


def get_stock_count(shop):
    return len(shop["pets"])


def get_pets_by_breed(shop, breed):
    pets_of_correct_breed = []
    for pet in shop["pets"]:
        if pet["breed"].lower() == breed.lower():
            pets_of_correct_breed.append(pet)
    return pets_of_correct_breed


def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"].lower() == name.lower():
            return pet


def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"].lower() == name.lower():
            shop["pets"].remove(pet)


def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, amount):
    customer["cash"] -= amount


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)


def customer_can_afford_pet(customer, pet):
    budget = get_customer_cash(customer)
    return pet["price"] <= budget


def sell_pet_to_customer(shop, pet, customer):
    if pet in shop["pets"] and customer_can_afford_pet(customer, pet):
        price = pet["price"]
        name = pet["name"]
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(shop, name)
        remove_customer_cash(customer, price)
        add_or_remove_cash(shop, price)
        increase_pets_sold(shop, 1)
