from jsondb import JsonDB

class PeopleDB(JsonDB):
    """
    Specialized database class for handling 'user' records inside a people JSON file.
    Inherits generic CRUD from JsonDB and adds people-specific methods.
    """

    def __init__(self, filepath):
        """
        Initialize PeopleDB with the path to the people JSON file.
        Calls the base class initializer to load data.
        """
        super().__init__(filepath)

    def find_by_name(self, first_name=None, last_name=None):
        """
        Search people by first or last name.
        
        Args:
            first_name (str, optional): First name to search for.
            last_name (str, optional): Last name to search for.

        Returns:
            list: List of person records matching the given names.
        """
        results = []
        for person in self.data:
            user = person.get("user", {})
            name = user.get("name", {})
            # Check if either first or last name matches
            if (first_name and name.get("first") == first_name) or \
               (last_name and name.get("last") == last_name):
                results.append(person)
        return results

    def create_person(self, person_data):
        """
        Add a new person record following the nested user structure.
        
        Args:
            person_data (dict): Person record to add. Must include 'user' key.
        
        Returns:
            int: Index of the newly added record in the data list.
        
        Raises:
            ValueError: If 'user' key is missing in the input data.
        """
        if "user" not in person_data:
            raise ValueError("Person must include 'user' key.")
        return self.create(person_data)
