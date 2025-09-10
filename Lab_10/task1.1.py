


def discount(price, category):
    if category == "student":
        return price * (0.9 if price > 1000 else 0.95)
    return price * 0.85 if price > 2000 else price

add = lambda x, y: x + y

total_price = add(1000, 1500)
print("Total Price:", total_price)
print("Discounted Price:", discount(total_price, "student"))

