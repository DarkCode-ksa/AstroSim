from astropy.time import Time
from astropy.coordinates import get_body_barycentric
from astropy.coordinates import solar_system_ephemeris
import numpy as np

def run_distance(sim):
    print(f"\n--- حساب المسافة: {sim['name']} ---")
    time = Time(sim["date"], format="isot", scale="utc")
    body1 = sim.get("body1", "").strip().lower()
    body2 = sim.get("body2", "").strip().lower()

    if not body1 or not body2:
        print("❌ يجب تحديد body1 و body2 في config.ini")
        return

    try:
        with solar_system_ephemeris.set("builtin"):
            pos1 = get_body_barycentric(body1, time)
            pos2 = get_body_barycentric(body2, time)
            distance = (pos1 - pos2).norm().to("AU").value
            print(f"📏 المسافة بين {body1.capitalize()} و {body2.capitalize()} في {time.isot}: {distance:.6f} AU")
    except Exception as e:
        print(f"❌ خطأ أثناء الحساب: {e}")