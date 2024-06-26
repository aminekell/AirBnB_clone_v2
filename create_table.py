import MySQLdb

def create_table():
    # الاتصال بقاعدة البيانات
    db = MySQLdb.connect(host="localhost",
                         user="hbnb_test",
                         passwd="hbnb_test_pwd",
                         db="hbnb_test_db")
    cursor = db.cursor()

    # إنشاء الجدول إذا لم يكن موجودًا
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS states (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );
    """)

    # إغلاق الاتصال
    db.close()

# إنشاء الجدول
create_table()
print("تم إنشاء الجدول بنجاح!")

