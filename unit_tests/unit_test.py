import unittest
from src.classmodul.redis import Redis

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.redis_store = Redis()
        self.redis_store.data = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3',
            'key4': 'value1',
            'key5': 'value1',
            'key6': 'value2'
        }

    def test_set_not_existing_key(self):
        not_existing_key = {'key30': 'value30'}
        expected_result = self.redis_store.data.copy() | not_existing_key
        for key, value in not_existing_key.items():
            self.redis_store.set(key, value)
        self.assertDictEqual(self.redis_store.data, expected_result)

    def test_set_existing_key(self):
        existing_key = {'key1': 'value2'}
        expected_result = self.redis_store.data.copy() | existing_key
        for key, value in existing_key.items():
            self.redis_store.set(key, value)
        self.assertDictEqual(self.redis_store.data, expected_result)

    def test_sets_existing_keys(self):
        existing_keys = {
            'key1': 'value4',
            'key2': 'value5',
            'key3': 'value6'
        }
        expected_result = self.redis_store.data.copy() | existing_keys
        for key, value in existing_keys.items():
            self.redis_store.set(key, value)
        self.assertDictEqual(self.redis_store.data, expected_result)

    def test_sets_not_existing_keys(self):
        not_existing_keys = {
            'key30': 'value30',
            'key31': 'value31',
            'key32': 'value32'
        }
        expected_result = self.redis_store.data.copy() | not_existing_keys

        for key, value in not_existing_keys.items():
            self.redis_store.set(key, value)

        self.assertDictEqual(self.redis_store.data, expected_result)

    def test_get_existing_keys(self):
        expected_value1 = self.redis_store.data['key1']
        expected_value2 = self.redis_store.data['key2']
        expected_value3 = self.redis_store.data['key3']

        self.assertEqual(self.redis_store.get('key1'), expected_value1)
        self.assertEqual(self.redis_store.get('key2'), expected_value2)
        self.assertEqual(self.redis_store.get('key3'), expected_value3)

    def test_get_not_existing_keys(self):
        self.assertEqual(self.redis_store.get('key300'), 'NULL')
        self.assertEqual(self.redis_store.get('key200'), 'NULL')
        self.assertEqual(self.redis_store.get('key100'), 'NULL')

    def test_unset_key(self):
        expected_result = self.redis_store.data.copy()
        del expected_result['key1']

        self.redis_store.unset('key1')

        self.assertDictEqual(self.redis_store.data, expected_result)

    def test_unset_keys(self):
        expected_result = self.redis_store.data.copy()
        del expected_result['key1']
        del expected_result['key2']
        del expected_result['key3']

        self.redis_store.unset('key1')
        self.redis_store.unset('key2')
        self.redis_store.unset('key3')

        self.assertDictEqual(self.redis_store.data, expected_result)

    def test_unset_not_existing_key(self):
        expected_result = self.redis_store.data.copy()
        self.redis_store.unset('key30')
        self.assertDictEqual(self.redis_store.data, expected_result)

    def test_unset_not_existing_keys(self):
        expected_result = self.redis_store.data.copy()

        self.redis_store.unset('key30')
        self.redis_store.unset('key31')
        self.redis_store.unset('key32')
        self.assertDictEqual(self.redis_store.data, expected_result)

    def test_numequalto_existing_values(self):
       self.assertEqual(self.redis_store.numequalto('value1'), 3)
       self.assertEqual(self.redis_store.numequalto('value2'), 2)
       self.assertEqual(self.redis_store.numequalto('value3'), 1)

    def test_numequalto_not_existing_values(self):
       self.assertEqual(self.redis_store.numequalto('value30'), 0)
       self.assertEqual(self.redis_store.numequalto('value31'), 0)
       self.assertEqual(self.redis_store.numequalto('value32'), 0)

if __name__ == '__main__':
    unittest.main()
