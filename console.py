import unittest
import MySQLdb
from console import HBNBCommand

@unittest.skipIf(storage_type != 'db', "not using database storage")
class TestDatabaseActions(unittest.TestCase):
    def setUp(self):
        self.db = MySQLdb.connect(
            host='localhost',
            user='hbnb_test',
            passwd='hbnb_test_pwd',
            db='hbnb_test_db'
        )
        self.cursor = self.db.cursor()

    def tearDown(self):
        self.cursor.close()
        self.db.close()

    def test_create_state(self):
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        initial_count = self.cursor.fetchone()[0]
        
        # Execute console command
        HBNBCommand().onecmd('create State name="California"')
        
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        new_count = self.cursor.fetchone()[0]
        
        self.assertEqual(new_count, initial_count + 1)

if __name__ == "__main__":
    unittest.main()
