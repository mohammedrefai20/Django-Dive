from django.shortcuts import render

def menu_view(request):
    # -------------------------
    # Hard-coded data (simple list)
    # -------------------------
    items = [
        {"name": "Margherita Pizza", "category": "Pizza"},
        {"name": "Pepperoni Pizza", "category": "Pizza"},
        {"name": "Chicken Burger", "category": "Burger"},
        {"name": "Beef Burger", "category": "Burger"},
        {"name": "Greek Salad", "category": "Salad"},
        {"name": "Caesar Salad", "category": "Salad"},
    ]

    # Extract unique categories
    categories = sorted(list({item["category"] for item in items}))

    # -------------------------
    # Get filters from GET params
    # -------------------------
    selected_category = request.GET.get("category", "")
    search_query = request.GET.get("search", "").lower()

    # -------------------------
    # Filtering logic
    # -------------------------
    filtered_items = items

    if selected_category:
        filtered_items = [
            item for item in filtered_items
            if item["category"] == selected_category
        ]

    if search_query:
        filtered_items = [
            item for item in filtered_items
            if search_query in item["name"].lower()
        ]

    # -------------------------
    # Pass everything to template
    # -------------------------
    context = {
        "categories": categories,
        "selected_category": selected_category,
        "search_query": search_query,
        "results": filtered_items,
    }

    return render(request, "menu.html", context)