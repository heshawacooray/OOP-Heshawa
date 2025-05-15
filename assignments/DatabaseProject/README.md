# Database Project - JSON DB Assignment - Heshawa Cooray

This project implements a simple JSON database system using Python. It includes a base class `JsonDB` that supports generic CRUD operations on JSON data stored in a file. 
Specialized subclasses extend the base functionality to handle domain-specific data and queries.

## Files

- `jsondb.py`: Base class `JsonDB` implementing CRUD methods with JSON file persistence.
- `people_db.py`: Subclass `PeopleDB` extending `JsonDB` to handle user records with custom search and creation methods.
- `people.json`: Sample JSON data file containing people records.
- `main.py`: Script demonstrating usage of `PeopleDB` for CRUD operations.

## Features

- Generic JSON data handling with load and save.
- Create, Read (with filtering), Update, Delete operations.
- Domain-specific querying (e.g., search people by name).
- Demonstrates object-oriented design with inheritance.

## Usage

Run the `main.py` script to see the PeopleDB in action performing CRUD operations on the JSON data.
