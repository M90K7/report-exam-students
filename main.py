import sys  # اضافه کردن ماژول sys برای خواندن آرگومان‌ها

def readFile(fileName):
    # خواندن داده‌ها از فایل student.txt به صورت خط به خط
    with open(fileName, 'r') as file:
        for line in file:  # خواندن هر خط به صورت جریانی
            yield line.strip()  # حذف فضاهای اضافی و بازگشت خط

def my_final_grade_calculation(fileName):

    str_student_lines = readFile(fileName)  # خواندن داده‌ها به صورت جریانی
    # تبدیل رشته به دیکشنری با نام به عنوان کلید و نمرات به عنوان مقادیر
    records = {}
    for line in str_student_lines:  # تغییر: استفاده از text_student به عنوان یک جریان
        if not line:  # بررسی خط خالی
            continue  # اگر خط خالی بود، ادامه بده
        record = line.split(',')
        name = record[0].lower()  # تبدیل نام به حروف کوچک
        scores = list(map(int, map(str.strip, record[1:])))  # حذف فضاهای اضافی و تبدیل به عدد
        # records[name] = scores
        q = scores[1:7]
        q_sorted = sorted(q)  # مرتب‌سازی نمرات
        q_filtered = q_sorted[2:]  # حذف دو نمره پایین‌ترین
        q_average = sum(q_filtered) / len(q_filtered)  # محاسبه میانگین
        q_weight = q_average * 0.25  # محاسبه 25% ارزش کل نمره

        a = scores[7:10]
        a_sorted = sorted(a)  # مرتب‌سازی نمرات
        a_filtered = a_sorted[1:]  # حذف پایین‌ترین نمره
        a_average = sum(a_filtered) / len(a_filtered)  # محاسبه میانگین
        a_weight = a_average * 0.25  # محاسبه 25% ارزش کل نمره
        
        mid = scores[10]
        final = scores[11]

        # محاسبه 25% نمره میان ترم و نهایی
        mid_weight = mid * 0.25
        final_weight = final * 0.25
        
        # محاسبه نمره کل
        total_score = q_weight + a_weight + mid_weight + final_weight
        
        # بررسی نمره کل
        result = "pass" if total_score > 60 else "fail"  # بررسی وضعیت نمره
        
        records[name] = result

    print(records)  # برای نمایش نتایج

if __name__ == "__main__":
    file_name = sys.argv[1] if len(sys.argv) > 1 else 'student.txt'  # خواندن نام فایل از آرگومان خط فرمان
    my_final_grade_calculation(file_name)  # استفاده از نام فایل خوانده شده
