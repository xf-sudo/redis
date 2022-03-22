class Redis:

    #list of commands to run basic operations
    basic_commands = ['GET', 'SET', 'UNSET', 'NUMEQUALTO', 'END']

    #list of commands to operate a trasaction
    transactional_commands = ['BEGIN', 'COMMIT', 'ROLLBACK']

    def __init__(self):
        self.data = dict()

    def set(self, key, value):
        """
        Set Function to associate a key with a value
        :param key: associated key to store
        :param value: associated value to store
        """
        self.data[key] = value

    def get(self, key):
        """
        Get Function to retrieve the value associated to a specific key
        :param key: the key to retrieve your value
        :return: returns the value associated to a specific key
        """
        return self.data[key] if key in self.data else 'NULL'

    def unset(self, key):
        """
        Unset Function to delete a key value pair by a specific key
        :param key: the key to be deleted
        """
        if key in self.data:
            del self.data[key]

    def numequalto(self, value_to_search):
        """
        Numequalto Function to obtain the number of keys that are associated
         with a given value
        :param value_to_search: the value to be searched
        :return: Returns the number of keys associated with a specific value
        """
        return sum(value_to_search == value for value in self.data.values())
