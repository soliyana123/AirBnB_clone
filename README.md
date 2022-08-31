# AirBnB_clone The Console
![airbnb](https://user-images.githubusercontent.com/59724074/187626081-6bbb4eb4-20e1-4001-b996-0d184e8b74d8.jpg)
## Background Context
The goal of the project is to deploy on our server a simple copy of the [AirBnB website](https://www.airbnb.com/).

we won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, we will have a complete web application composed by:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
## Steps
we won’t build this application all at once, but step by step.

Each step will link to a concept. this specfic Repositoray:

** The Console **
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from our console code (the command interpreter itself) and from the front-end and RestAPI we will build later.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine
![airbnbclone](https://user-images.githubusercontent.com/59724074/187630820-493cda30-d1e3-418d-9e1b-374b453965b0.jpg)

### Requirements
** Python Scripts **
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

