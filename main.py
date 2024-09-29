def main():
    text_student = """tom, 10, 20 , 0 , 100 , 0 , 100, 70, 80, 90, 0, 80, 85
mary, 0, 50, 66, 40, 10, 60, 70, 80, 90, 100, 80, 85
joan, 0, 80, 40, 10, 50, 60, 7, 80, 90, 0, 80, 5"""

    
    # تبدیل رشته به دیکشنری با نام به عنوان کلید و نمرات به عنوان مقادیر
    records = {
        record[0].lower(): list(map(lambda x: int(x.strip()), record[1:]))  # تبدیل نام به حروف کوچک و حذف فضاهای اضافی
        for record in (line.split(',') for line in text_student.splitlines())
    }


    for name, scores in records.items():
      q = scores[1:7]
      q_sorted = sorted(q)  # مرتب‌سازی نمرات
      q_filtered = q_sorted[2:]  # حذف دو نمره پایین‌ترین
      q_average = sum(q_filtered) / len(q_filtered)  # محاسبه میانگین
      q_weighted = q_average * 0.25  # محاسبه 25% ارزش کل نمره

      a = scores[7:10]
      a_sorted = sorted(a)  # مرتب‌سازی نمرات
      a_filtered = a_sorted[1:]  # حذف پایین‌ترین نمره
      a_average = sum(a_filtered) / len(a_filtered)  # محاسبه میانگین
      a_weighted = a_average * 0.25  # محاسبه 25% ارزش کل نمره
      
      mid = scores[10]
      final = scores[11]

      # محاسبه 25% نمره میان ترم و نهایی
      mid_weighted = mid * 0.25
      final_weighted = final * 0.25
      
      # محاسبه نمره کل
      total_score = q_weighted + a_weighted + mid_weighted + final_weighted
      
      # بررسی نمره کل
      result = "pass" if total_score > 60 else "fail"  # بررسی وضعیت نمره
      
      records[name] = result

    print(records)  # برای نمایش نتایج

if __name__ == "__main__":
    main()
