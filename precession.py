from astropy.time import Time

def run_precession(sim):
    year = Time(sim["date"]).byear
    print(f"\n--- تمايل المحور الأرضي: {sim['name']} ---")
    print(f"📍 التاريخ: {int(year)} ق.م")

    # نموذج تقريبي: زاوية التمايل تتغير بمعدل ~50 arcsec/سنة
    # دورة كاملة ~26,000 سنة → زاوية التمايل ~360°
    cycle_years = 26000
    angle = (360 * ((year + 2000) % cycle_years)) / cycle_years
    print(f"زاوية التمايل التقريبية: {angle:.2f}°")