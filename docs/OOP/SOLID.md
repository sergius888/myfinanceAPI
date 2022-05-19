SOLID are a set of 5 programming principles, especially directed to Object Oriented Programming. Each letter represent a principle.

S - Single Responsibility Principle -> every class function should perform a single functionality

    -> functions
        -> wrong: a function edits an element in a DB and deletes another element
        -> right: a function edits an element in a DB, a different function deletes an element from DB
	
    -> classes
        -> wrong: a class reads/writes to a DB and reads/writes to a file
        -> right: a class has the responsibility to manage interactions with a DB (read & write), another class does this for a file

https://sobolevn.me/2019/03/enforcing-srp

O - Open Closed Principle -> classes/functions should be open for extension, but closed to change

https://www.stevebrownlee.com/open-closed-principle-practical-example/

https://michalgodkowicz.medium.com/how-to-make-your-python-code-maintainable-with-the-open-close-principle-1860fecc8ec0

L - Liskov Substitution Principle -> I can use a child class exactly as I can use the parent class

https://www.pythonforeveryone.com/articles/liskov-substitution-principle-python.html

I - Interface Seggregation Principle -> a caller of a class should not depend on functions it does not use 

https://dev.to/naomidennis/introduction-to-the-interface-separation-principle-3bmj

D - Dependency Injection Principle -> High-level modules should not depend on low-level modules

    -> for example, we can have a shopping app
        -> classes which represent the products we sell should not know which DB we use
        -> if we change the DB, we should make no change in our product classes (or very minimal changes)

https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html

https://www.linisnil.com/articles/python-dependency-inversion-principle/
