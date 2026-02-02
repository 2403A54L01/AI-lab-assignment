# A simple product database with categories
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics"},
    {"id": 2, "name": "Python Book", "category": "Books"},
    {"id": 3, "name": "Wireless Mouse", "category": "Electronics"}
]

def recommend_products(user_interest):
    recommendations = []
    
    for item in products:
        if item["category"] == user_interest:
            # Adding the "Why" reasoning
            reason = f"Because you are interested in {user_interest}"
            recommendations.append({"product": item["name"], "reason": reason})
            
    return recommendations

# User likes Electronics
print(recommend_products("Electronics"))