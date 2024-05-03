import re

def parser_regex(file_contents):
    parsed_info: dict = {}

    # Extract Receipt No
    receipt_id = re.search(r'\s{3}Receipt\s*No\.\s*:\s*(\S+)', file_contents)
    receipt_id = receipt_id.group(1)

    # Extract Receipt Date
    date = re.search(r'\d{1}\/\d{2}\/\d{4}', file_contents)
    date = date.group()

    # Extract Receipt Time
    time = re.search(r'\d{2}\:\d{2}\:\d{2}\s[APap][Mm]', file_contents)
    time = time.group()

    # Extract User
    user = re.search(r'\s{3}User:\s*(\S+\s\S+)', file_contents)
    user = user.group(1)

    # Extract Order No
    order_no = re.search(r'\s{3}Order\s*No\.\s*:\s*(\S+)', file_contents)
    order_no = order_no.group(1)

    # Extract Items count
    count = re.search(r'\s{3}Items count:\s*(\S+)', file_contents)
    count = count.group(1)

    # Extract Total
    total = re.search(r'\s{3}TOTAL:\s*(\S+)', file_contents)
    total = total.group(1)

    # Extract Cash
    cash = re.search(r'\s{3}Cash:\s*(\S+)', file_contents)
    cash = cash.group(1)

    # Extract Paid amount
    paid_amount = re.search(r'\s{3}Paid amount:\s*(\S+)', file_contents)
    paid_amount = paid_amount.group(1)

    # Extract Items
    items= []
    item_matches = re.findall(r'\s*(\w+)\s+(\d+)\s*x\s*\$(\d+\.\d+)\s*\$(\d+\.\d+)', file_contents)

    # Extract each item and populate items list
    for item in item_matches:
        item_name, item_quantity, item_price, total_price = item
        item_quantity = int(item_quantity)
        item_price = float(item_price)
        total_price = float(total_price)
        items.append({
            "Item_name": item_name,
            "Item_price": item_price,
            "Item_quantity": item_quantity,
            "Total_price": total_price
        })

    parsed_info = { "Receipt No": receipt_id, "Receipt Date": date, "Receipt Time": time, "User": user, 
                    "Order No": order_no, "items": items, "Items count": count, "Total": total, "Cash": cash, 
                    "Paid amount": paid_amount}

    return parsed_info
