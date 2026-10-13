from ticket_processor.ticket import create_ticket

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
        ticket = create_ticket(title, category, urgency, affected_users, tickets)
        print("Created", ticket["id"], "with priority", ticket["priority"])
    except ValueError as error:
        print("Error:", error)

def main():
    tickets = []
    while True:
        print("1. Create ticket")
        print("2. List tickets")
        print("0. Exit")
        choice = input("Choose: ")
        if choice == "1":
            ask_create(tickets)
        elif choice == "2":
            if len(tickets) == 0:
                print("No tickets yet")
            for ticket in tickets:
                print(ticket["id"], ticket["title"], ticket["priority"])
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()