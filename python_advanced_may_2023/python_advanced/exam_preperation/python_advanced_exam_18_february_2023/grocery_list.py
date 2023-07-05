def shop_from_grocery_list(budget, grocery_list, *products):
    purchased = set()
    total_cost = 0

    for product, price in products:
        if product not in grocery_list:
            continue

        if product in purchased:
            continue

        if budget < price:
            break

        purchased.add(product)
        total_cost += price
        budget -= price

    if len(purchased) == len(grocery_list):
        remaining_budget = format(budget, ".2f")
        return f"Shopping is successful. Remaining budget: {remaining_budget}."
    else:
        missing_products = set(grocery_list) - purchased
        return f"You did not buy all the products. Missing products: {missing_products}."


# Input
budget = 100
grocery_list = ["tomato", "cola"]
products = [
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
]

# Call the function
output = shop_from_grocery_list(budget, grocery_list, *products)

# Output
print(output)
