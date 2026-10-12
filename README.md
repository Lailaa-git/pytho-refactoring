Python refactoring
Example 1:

Replaced multiple if/elif statements with a dictionary to simplify order creation and make it easier to add new order types.

Example 2:
Separated user management, storage, emails, and reports into different classes, following the Single Responsibility Principle.

Example 3:
Changed the inheritance structure so bicycles are not required to implement engine functionality, following the Liskov Substitution Principle.

Reflection
This task helped me understand how solid principles improve code structure. I started by separated responsibilities,then  simplified object creation, and improved inheritance. The goal was to make the code easier to understand not just for me but anyone reading it, and extend without adding unnecessary code.