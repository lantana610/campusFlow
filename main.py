from ticket_processor.ticket import create_ticket
from Pipeline.workflow import assign_ticket as workflow_assign_ticket, find_ticket
from Pipeline.reports import generate_report, display_report


def ask_create(tickets):
    title = input("Title: ")
    category = input("Category (Network, Hardware, Software, Other): ")
    urgency = input("Urgency (low, medium, high): ")
    users_text = input("Affected users: ")

    try:
        affected_users = int(users_text)
    except ValueError:
        print("Error: affected users must be a whole number")
        return

    try:
        ticket = create_ticket(
            title,
            category,
            urgency,
            affected_users,
            tickets
        )
        print(
            "Created",
            ticket["id"],
            "with priority",
            ticket["priority"]
        )
    except ValueError as error:
        print("Error:", error)


def list_tickets(tickets):
    if not tickets:
        print("No tickets yet")
        return

    for ticket in tickets:
        print(
            ticket["id"],
            ticket["title"],
            ticket["priority"]
        )


def ask_assign(tickets):
    ticket_id = input("Enter ticket ID to assign: ").strip()
    staff_member = input("Enter staff member name: ").strip()

    try:
        ticket = workflow_assign_ticket(tickets, ticket_id, staff_member)
        print("Assigned", ticket["id"], "to", ticket["assigned_to"])
    except ValueError as error:
        print("Error:", error)
    except TypeError as error:
        print("Assignment function mismatch:", error)

def inspect_ticket(tickets):
    ticket_id = input("Enter ticket ID to inspect: ").strip()

    try:
        ticket = find_ticket(tickets, ticket_id)

        print("\nTicket found:")
        print("ID:", ticket["id"])
        print("Title:", ticket["title"])
        print("Status:", ticket["status"])
        print("Assigned to:", ticket.get("assigned_to", "Unassigned"))

    except ValueError:
        print(f"Ticket not found: {ticket_id}")

def main():
    tickets = []

    while True:
        print("\n=== CampusFlow ===")
        print("1. Create ticket")
        print("2. List tickets")
        print("3. Assign ticket")
        print("4. Inspect ticket")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            ask_create(tickets)

        elif choice == "2":
            list_tickets(tickets)

        elif choice == "3":
            ask_assign(tickets)

        elif choice == "4":
            inspect_ticket(tickets)

        elif choice == "0":
            print("Exiting CampusFlow...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

