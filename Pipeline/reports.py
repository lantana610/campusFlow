def generate_report(tickets):
    report = {
        "total": len(tickets),
        "by_status": {
            "open": 0,
            "in_progress": 0,
            "resolved": 0
        },
        "by_priority": {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0
        }
    }

    for ticket in tickets:
        status = ticket["status"]
        priority = ticket["priority"]
        if status in report["by_status"]:
            report["by_status"][status] += 1
        if priority in report["by_priority"]:
            report["by_priority"][priority] += 1
    return report


def display_report(tickets):   
    report = generate_report(tickets)
    print("\n CAMPUSFLOW REPORT")
    print(f"Total tickets: {report['total']}")
    print("\nTickets by Status:")
    for status, count in report["by_status"].items():
        print(f"  {status.replace('_', ' ').title()}: {count}")
    print("\nTickets by Priority:")
    for priority, count in report["by_priority"].items():
        print(f"  {priority.title()}: {count}")
    print("\n")