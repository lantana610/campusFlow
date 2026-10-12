def find_ticket(tickets, ticket_id):
    #Return the ticket with the requested ID.
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    raise ValueError(f"Ticket not found: {ticket_id}")

def assign_ticket(tickets, ticket_id, staff_name):
    #Assign a ticket to a staff member.
    if not isinstance(staff_name, str) or not staff_name.strip():
        raise ValueError("Staff name cannot be empty")

    ticket = find_ticket(tickets, ticket_id)
    ticket["assigned_to"] = staff_name.strip()

    return ticket