from astropy.time import Time

def run_obliquity(sim):
    year = Time(sim["date"]).byear
    print(f"\n--- ميل المحور الأرضي: {sim['name']} ---")
    print(f"📍 التاريخ: {int(year)} ق.م")

    # نموذج تقريبي: الميل يتراوح بين 22.1° و 24.5° كل ~41,000 سنة
    # نستخدم دالة جيبية لتقريب التغير
    import numpy as np
    base = 23.3  # متوسط الميل
    amplitude = 1.2
    cycle = 41000
    angle = base + amplitude * np.sin(2 * np.pi * (year + 2000) / cycle)
    print(f"زاوية الميل التقريبية: {angle:.2f}°")