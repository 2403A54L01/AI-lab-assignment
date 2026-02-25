def employee_performance_report(emp_data):
    report = {}
    
    for employee, ratings in emp_data.items():
        if not ratings:
            report[employee] = {
                "average_rating": None,
                "highest_rating_month_index": None,
                "performance_category": "No ratings"
            }
            continue
        
        average_rating = sum(ratings) / len(ratings)
        highest_rating_month_index = ratings.index(max(ratings))
        
        if average_rating >= 4.5:
            performance_category = "Excellent"
        elif average_rating >= 3.5:
            performance_category = "Good"
        elif average_rating >= 2.5:
            performance_category = "Average"
        else:
            performance_category = "Poor"
        
        report[employee] = {
            "average_rating": average_rating,
            "highest_rating_month_index": highest_rating_month_index,
            "performance_category": performance_category
        }

    return report

# Example usage
employee_data = {
    "Alice": [4.5, 4.7, 4.8, 4.6],
    "Bob": [3.0, 3.5, 3.2, 3.8],
    "Charlie": [2.0, 2.5, 2.8, 2.3],
    "David": [1.0, 1.5, 1.2, 1.8],
    "Eve": []
}
performance_report = employee_performance_report(employee_data)
for employee, report in performance_report.items():
    print(f"{employee}: {report}")      
