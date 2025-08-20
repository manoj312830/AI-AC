# Simple Product Recommendation System
# Sample product categories and products
products = {
    "soap": ["Dove Soap", "Lux Soap", "Pears Soap"],
    "mobile": ["iPhone 14", "Samsung Galaxy S23", "OnePlus 11"],
    "toys": ["Lego Set", "Barbie Doll", "Hot Wheels Car"],
    "games": ["Chess Board", "Monopoly", "Uno Cards"],
    "laptop": ["Dell Inspiron", "MacBook Air", "HP Pavilion"]
}
# User search history
user_history = []
def recommend_products(history):
    if not history:
        print("No search history found. Please search for a product.")
        return
    last_search = history[-1]
    if last_search in products:
        print(f"Recommended products for '{last_search}':")
        for item in products[last_search]:
            print(f"- {item}")
    else:
        print("No recommendations found for your search.")

def main():
    print("Welcome to the Product Recommendation System!")
    print("Available categories:", ', '.join(products.keys()))
    while True:
        search = input("Search for a product category (or type 'exit' to quit): ").strip().lower()
        if search == 'exit':
            print("Thank you for using the system!")
            break
        user_history.append(search)
        recommend_products(user_history)
if __name__ == "__main__":
    main()