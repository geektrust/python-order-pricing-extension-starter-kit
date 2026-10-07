CATEGORY_NAMES = ["Electronics", "Books", "Clothing"]
CATEGORY_SHIPPING = [10, 0, 5]


def process_order(order_text):
    parts = order_text.split(" ")
    customer_type = parts[0]
    items_total = 0
    shipping_total = 0
    categories_seen = []
    distinct_category_count = 0

    if customer_type != "Regular" and customer_type != "Member" and customer_type != "VIP":
        print("INVALID CUSTOMER TYPE")
        return

    for i in range(1, len(parts)):
        fields = parts[i].split(":")
        category = fields[0]
        price = int(fields[1])
        quantity = int(fields[2])

        category_index = -1
        for j in range(len(CATEGORY_NAMES)):
            if CATEGORY_NAMES[j] == category:
                category_index = j
        if category_index < 0:
            print("INVALID CATEGORY")
            return

        if category not in categories_seen:
            distinct_category_count = distinct_category_count + 1
        categories_seen.append(category)

        shipping_total = shipping_total + CATEGORY_SHIPPING[category_index] * quantity
        items_total = items_total + price * quantity

    discount_percent = 0
    if customer_type == "Member":
        discount_percent = 10
    if customer_type == "VIP":
        discount_percent = 20

    total = items_total - (items_total * discount_percent) / 100
    if customer_type != "VIP" and distinct_category_count < 3:
        total = total + shipping_total

    print("Order Total: " + "{:.2f}".format(total))
