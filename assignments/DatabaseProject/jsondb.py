import json

class JsonDB:
    """
    Base class for a simple JSON "database" with generic CRUD operations.
    Stores data in-memory and persists it to a JSON file.
    """

    def __init__(self, filepath):
        """
        Initialize the database by loading JSON data from the file.

        Args:
            filepath (str): Path to the JSON file storing the data.
        """
        self.filepath = filepath
        self.data = []
        self._load_data()

    def _load_data(self):
        """
        Load JSON data from the file into self.data.
        If the file is missing or invalid, initialize with an empty list.
        """
        try:
            with open(self.filepath, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = []
        except json.JSONDecodeError:
            self.data = []

    def _save_data(self):
        """
        Save the current self.data list back to the JSON file.
        """
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=2)

    def create(self, record):
        """
        Add a new record to the database and save to file.

        Args:
            record (dict): The record to add.

        Returns:
            int: Index of the newly added record.
        """
        self.data.append(record)
        self._save_data()
        return len(self.data) - 1  # Return new record index

    def read(self, **filters):
        """
        Search for records matching all given filter key-value pairs.

        Args:
            filters: Arbitrary keyword arguments for filtering records.

        Returns:
            list: List of matching records.
        """
        results = []
        for record in self.data:
            if all(record.get(k) == v for k, v in filters.items()):
                results.append(record)
        return results

    def update(self, record_id, updated_data):
        """
        Update an existing record by its index with provided data.

        Args:
            record_id (int): Index of the record to update.
            updated_data (dict): Data to update the record with.

        Returns:
            dict: The updated record.

        Raises:
            ValueError: If record_id is invalid (out of range).
        """
        if 0 <= record_id < len(self.data):
            self.data[record_id].update(updated_data)
            self._save_data()
            return self.data[record_id]
        else:
            raise ValueError(f"Record with index {record_id} not found.")

    def delete(self, record_id):
        """
        Remove a record by its index and save changes.

        Args:
            record_id (int): Index of the record to delete.

        Returns:
            dict: The deleted record.

        Raises:
            ValueError: If record_id is invalid (out of range).
        """
        if 0 <= record_id < len(self.data):
            deleted = self.data.pop(record_id)
            self._save_data()
            return deleted
        else:
            raise ValueError(f"Record with index {record_id} not found.")
