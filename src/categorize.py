import re

def categorize(text):
    text = text.lower()

    rules = {
        "Food": ["swiggy", "zomato", "food", "restaurant"],
        "Transport": ["uber", "ola", "ride", "bus"],
        "Shopping": ["amazon", "flipkart", "shopping"],
        "Bills": ["electricity", "bill", "netflix"],
        "Income": ["salary", "income"]
    }

    for cat, keywords in rules.items():
        for k in keywords:
            if re.search(k, text):
                return cat

    return "Others"