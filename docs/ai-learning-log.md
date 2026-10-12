Date: 09/10/2026
Task: I need to know how to handle git commands like branch, pull and push, and merge requests.

Question Asked:
I asked ChatGPT to show me how to handle those git commands.

AI's Suggestion:
It showed me how to handle each of the commands.

What I learned:
How to branch, push, pull, and merge requests.

My Implementation:
I used what I learned to branch, push, pull and merge requests and also comment.


Date: 10/10/2026
Task:
I needed to implement a function that assigns a CampusFlow ticket to a staff member.

Question Asked:
I asked ChatGPT to help me write a Python function that finds a ticket by its ID and assigns it to a staff member.

AI's Suggestion:
The AI suggested creating a find_ticket() function to locate a ticket and an assign_ticket() function to update its assigned_to field. It also suggested checking that the staff member's name was not empty.

What I Learned:
I learned how Python functions can work together, how to search through a list of dictionaries, and how to update a dictionary's value. I also learned why input validation is important.

My Implementation:
I used the suggestion as a starting point in Pipeline/workflow.py. I reviewed the function and made sure it matched the ticket structure agreed upon by my team.

Testing and Verification:
I used unit tests in test/test_workflow.py to check ticket assignment and invalid staff names. I recorded the results after running the tests.

Reflection:
I learned that a function should handle invalid input clearly instead of silently accepting incorrect values. In future, I will consider normal and error cases before implementing a function.

Entry 2: Generating ticket reports
Date: 10/10/2026
Task:
I needed to create a report showing the total number of tickets and counts grouped by status and priority.

Question Asked:
I asked ChatGPT how to generate a summary report from a list of ticket dictionaries, including how to handle an empty list.

AI's Suggestion:
The AI suggested creating a generate_report() function that initializes counters, loops through the tickets, and counts each ticket's status and priority.

What I Learned:
I learned how to use dictionaries as counters and how to process lists with a for loop. I also learned that initializing all expected categories to zero ensures that the report can show categories even when no tickets belong to them.

My Implementation:
I applied the approach in Pipeline/reports.py and used test/test_reports.py to check the output.

Testing and Verification:
I checked the empty-ticket case and a sample containing tickets with different statuses and priorities. I recorded which tests passed and investigated any failures.

Reflection:
I learned the importance of testing edge cases, particularly empty input. Next time, I will write down the expected report structure before implementing the function.

Entry 3: Debugging Python test discovery
Date: 12/10/2026
Task:
I wanted to run my unit tests but encountered an error when Python tried to discover the test files.

Question Asked:
I asked ChatGPT why the command python3 -m unittest discover -s tests -v produced an error.

AI's Suggestion:
The AI explained that my project directory was named test, not tests, and suggested running:
python3 -m unittest discover -s test -v

It also suggested checking the project directory and adding __init__.py files if needed.
What I Learned:
I learned that Python commands must use the correct directory names and that the test discovery command needs to match my project's structure.

My Implementation:
I kept my existing test and Pipeline folder names and used the command appropriate for that structure.

Testing and Verification:
I ran the corrected command and checked the output. I noted any remaining errors rather than assuming the problem was fixed.

Reflection:
I learned to check directory names and import statements before changing my project structure. I also learned that an error message can help identify where a problem originates.