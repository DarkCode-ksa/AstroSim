from astropy.time import Time

def run_polar_motion(sim):
    year = Time(sim["date"]).byear
    print(f"\n--- حركة الأقطاب: {sim['name']} ---")
    print(f"📍 التاريخ: {int(year)} ق.م")
    print("⚠️ النموذج تقريبي: لا توجد بيانات دقيقة قبل 1900 م")
    deviation = 0.5 * ((year + 2000) / 10000)  # نموذج افتراضي
    print(f"انحراف القطب التقريبي: {deviation:.2f}°")