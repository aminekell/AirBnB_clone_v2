import unittest
import MySQLdb

class TestMySQL(unittest.TestCase):

    def setUp(self):
        self.db = MySQLdb.connect(host="localhost",
                                  user="hbnb_test",
                                  passwd="hbnb_test_pwd",
                                  db="hbnb_test_db")
        self.cursor = self.db.cursor()

    def tearDown(self):
        self.db.close()

    def get_record_count(self):
        self.cursor.execute("SELECT COUNT(*) FROM states")
        count = self.cursor.fetchone()[0]
        return count

    def add_state(self):
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")
        self.db.commit()

    def test_add_state(self):
        # الحصول على عدد السجلات قبل الإضافة
        initial_count = self.get_record_count()

        # إضافة حالة جديدة
        self.add_state()

        # الحصول على عدد السجلات بعد الإضافة
        new_count = self.get_record_count()

        # التحقق من أن العدد زاد بواحدة
        self.assertEqual(new_count, initial_count + 1)

if __name__ == '__main__':
    unittest.main()

