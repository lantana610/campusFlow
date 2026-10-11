
def calculate_priority(urgency, affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"
    if urgency == "high" or affected_users >= 10:
        return "high"
    if urgency == "medium" or affected_users >= 3:
        return "medium"
    else:
        return "low"
        
def validate_title(title):
    if title.strip() == "":
        raise ValueError("title cannot be blank")
    return title.strip()

def validate_urgency(urgency):
    cleaned = urgency.strip().lower()
    allowed = ["low", "medium", "high"]
    if cleaned not in allowed:
        raise ValueError("urgency must be low, medium or high")
    return cleaned

def validate_category(category):
    cleaned = category.strip().capitalize()
    allowed = ["Network", "Hardware", "Software", "Other"]
    if cleaned not in allowed:
        raise ValueError("category must be Network, Hardware, Software or Other")
    return cleaned