# Access the input data from the webhook
input_data = _input.all()[0].json

# Get the list of menu items
items_list = input_data.get('body', {}).get('Items', [])

# Create a list of objects that match your sheet structure
output = []
for item in items_list:
    output.append({
        "Name": item.get("Name"),
        "Description": item.get("Description"),
        "Portion": item.get("Portions", ""),  # Get from Portions field (updated from form)
        "PcsDisplay": item.get("PcsDisplay", ""),
        "Rate": item.get("Rate"),
        "Category": item.get("Category", ""),
        "Veg/Non Veg": item.get("VegNonVeg", ""),
        "Amount": item.get("Amount")
    })

return output