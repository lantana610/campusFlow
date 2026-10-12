## Fellow: Lantana Yusuf

### Interaction #1: Raising and catching exceptions
Problem: I needed to learn how a function can refuse bad input, for ticket validation.
My initial understanding: my understanding  was that the function was to reget invalid input but not think about when the spaces in between so and i just using only print to return an error instead of using the function like ValueError
Prompt to AI: [how can you reget a bad input]
Useful AI guidance: A function can use `raise ValueError(message)` to stop on bad input. The caller can catch it with `try/except` and show the message.
My independent experiment/test: I wrote `check_age` in practice.py and ran `check_age(5)` and `check_age(-1)`. 

Verification source or result: Output was `5` then `Error: age cannot be negative`. 
Decision: Accepted. I used the same pattern in `validate_title`, `validate_urgency` and `validate_category`.
Related file/commit: ticket_processor/ticket.py, validate_title 
What I can now explain without AI: i can explain how why my function works

### Interaction #2: unittest, ERROR versus FAIL
Problem: I needed to learn how to write automated tests with unittest.
My initial understanding: was only start the test but not knowing i will have to put everthoing in class and also inport unittest
Prompt to AI: what i need to write a test file in python and how to start
Useful AI guidance: Tests go in a class that inherits `unittest.TestCase`. `assertEqual(actual, expected)` compares two values, and `assertRaises` checks that an error is raised.
My independent experiment/test: My first test gave an ERROR: `missing 1 required positional argument: 'second'`. Later I changed two numbers to 9 and 3 and got a FAIL: `'high' != 'critical'`.
Verification source or result: ERROR means the test code itself could not run. FAIL means it ran and the answer differed. In both FAIL cases the function was right and my test was wrong. After fixing them, 22 tests passed.
Decision: Improved. I also found one test whose name said low urgency but whose call used "medium", and fixed it so the name and call match.
Related file/commit: tests/test_ticket.py 
What I can now explain without AI: my test file and why the am test each case

### Interaction #3: Validating a number, and the True trap
Problem: affected_users must be a positive whole number, not 0, -3, 5.0, text or a boolean.
My initial understanding: was that affected user can be either float or maybe 0 if none is affected
Prompt to AI: can my affected be a boolean, float or nagetive number
Useful AI guidance: Check the type before the value. Python treats True as the integer 1, so `isinstance(True, int)` is True and the bool case needs its own check.
My independent experiment/test: My first version rejected a valid 5, because I had the type check backwards. My second version, `not isinstance(x, int)`, let True through. I traced both by hand and wrote `test_boolean_users_is_rejected`.
Verification source or result: The boolean test showed the bug in my second version. I then used the fix the AI gave me, `isinstance(x, bool) or not isinstance(x, int)`, and all 22 tests passed.
Decision: I rejected my own two versions after tracing them and testing them. I accepted the AI's final line only after the test confirmed it. I did not write that final line myself.
Related file/commit: validate_affected_users in ticket.py, test_boolean_users_is_rejected 
What I can now explain without AI: my ticket file