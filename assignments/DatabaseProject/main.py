from people_db import PeopleDB

def main():
    """
    Main function to demonstrate PeopleDB CRUD operations.
    """

    # Initialize PeopleDB with path to JSON data
    db = PeopleDB("people.json")

    # === READ: Print all people in the database ===
    print("=== All People ===")
    for person in db.data:
        print(person)

    # === CREATE: Add a new person record ===
    print("\n=== Creating a New Person ===")
    new_person = {
        "user": {
            "name": {"first": "Alice", "last": "Brown"},
            "phone": "555-999-0000",
            "email": "alice.brown@example.com",
            "location": {"city": "Dallas", "state": "TX"}
        }
    }
    new_index = db.create_person(new_person)
    print(f"New person added at index {new_index}")

    # === READ: Search for people with first name 'Alice' ===
    print("\n=== Searching by First Name ===")
    results = db.find_by_name(first_name="Alice")
    print(results)

    # === UPDATE: Change location city of first matching 'Alice' ===
    if results:
        person = results[0]
        index = db.data.index(person)
        print("\n=== Updating Alice's City ===")
        # Note: This replaces the entire 'user' key with the given dict,
        # so in practice you might want to merge nested dictionaries to preserve other fields.
        db.update(index, {"user": {"location": {"city": "Austin", "state": "TX"}}})
        print(db.data[index])

        # === DELETE: Remove Alice from database ===
        print("\n=== Deleting Alice ===")
        db.delete(index)
        print("Deleted. Current people:")
        for person in db.data:
            print(person)

if __name__ == "__main__":
    main()
