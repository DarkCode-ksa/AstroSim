from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz
from core.astronomy import get_star_coords
import numpy as np

def run_inverse_alignment(sim):
    print(f"\n--- محاكاة عكسية: {sim['name']} ---")
    time = Time(sim["date"], format="isot", scale="utc")

    location = EarthLocation(lat=float(sim["lat"]), lon=float(sim["lon"]))
    frame = AltAz(obstime=time, location=location)

    az_target = float(sim.get("azimuth", 0.0))
    alt_target = float(sim.get("altitude", 0.0))
    tolerance = float(sim.get("tolerance", 1.0))

    # قائمة الأجرام المحتملة (نجوم، كواكب، أبراج)
    candidates = [
        "Sirius", "Betelgeuse", "Alnitak", "Alnilam", "Mintaka",
        "Regulus", "Aldebaran", "Sun", "Moon", "Mars", "Venus",
        "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpius", "Sagittarius", "Capricornus", "Aquarius", "Pisces"
    ]

    found = []

    for name in candidates:
        try:
            obj = get_star_coords(name, time)
            altaz = obj.transform_to(frame)
            alt = altaz.alt.degree
            az = altaz.az.degree

            if (abs(alt - alt_target) <= tolerance) and (abs(az - az_target) <= tolerance):
                found.append((name, alt, az))
        except Exception as e:
            print(f"⚠️ خطأ في {name}: {e}")

    if found:
        print(f"🔍 الأجرام ضمن ±{tolerance}° من الاتجاه ({az_target}°, {alt_target}°):")
        for name, alt, az in found:
            print(f"• {name}: ارتفاع {alt:.2f}°، زاوية أفقية {az:.2f}°")
    else:
        print("❌ لم يتم العثور على أجرام ضمن النطاق المحدد.")