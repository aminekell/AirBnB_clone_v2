import MySQLdb

def get_record_count():
    # الاتصال بقاعدة البيانات
    db = MySQLdb.connect(host="localhost",
                         user="hbnb_test",
                         passwd="hbnb_test_pwd",
                         db="hbnb_test_db")
    cursor = db.cursor()

    # تنفيذ استعلام لحساب عدد السجلات
    cursor.execute("SELECT COUNT(*) FROM states")
    count = cursor.fetchone()[0]

    # إغلاق الاتصال
    db.close()

    return count

def add_state():
    # الاتصال بقاعدة البيانات
    db = MySQLdb.connect(host="localhost",
                         user="hbnb_test",
                         passwd="hbnb_test_pwd",
                         db="hbnb_test_db")
    cursor = db.cursor()

    # تنفيذ أمر لإضافة حالة جديدة
    cursor.execute("INSERT INTO states (name) VALUES ('California')")
    db.commit()

    # إغلاق الاتصال
    db.close()

# الحصول على عدد السجلات قبل الإضافة
initial_count = get_record_count()
print(f"عدد السجلات قبل الإضافة: {initial_count}")

# إضافة حالة جديدة
add_state()

# الحصول على عدد السجلات بعد الإضافة
new_count = get_record_count()
print(f"عدد السجلات بعد الإضافة: {new_count}")

# التحقق من النتيجة
if new_count == initial_count + 1:
    print("الاختبار ناجح!")
else:
    print("الاختبار فشل!")

