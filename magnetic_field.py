from astropy.time import Time

def run_magnetic_field(sim):
    year = Time(sim["date"]).byear
    print(f"\n--- المجال المغناطيسي: {sim['name']} ---")
    print(f"📍 التاريخ: {int(year)} ق.م")
    print("⚠️ النموذج تقريبي: لا توجد بيانات دقيقة قبل 1900 م")
    intensity = 50 - 0.01 * abs(year + 2000)
    inclination = 60 + 5 * ((year + 2000) / 10000)
    declination = -2 + 0.5 * ((year + 2000) / 10000)
    print(f"الشدة: {intensity:.2f} µT | الميل: {inclination:.2f}° | الانحراف: {declination:.2f}°")