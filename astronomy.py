from astropy.coordinates import SkyCoord, get_sun, get_moon, get_body
from astropy.time import Time
import astropy.units as u
from astropy.coordinates import solar_system_ephemeris

def get_star_coords(name, time=None):
    catalog = {
        # نجوم محددة
        "Alnitak": ("05h40m45.5s", "-01d56m33s"),
        "Alnilam": ("05h36m12.8s", "-01d12m06s"),
        "Mintaka": ("05h32m00.4s", "-00d17m57s"),
        "Sirius": ("06h45m08.9s", "-16d42m58s"),
        "Betelgeuse": ("05h55m10.3s", "+07d24m25s"),
        "Regulus": ("10h08m22.3s", "+11d58m02s"),
        "Aldebaran": ("04h35m55.2s", "+16d30m33s"),
        "MilkyWay": ("17h45m40.04s", "-29d00m28.1s"),

        # الأبراج الفلكية (مواقع تقريبية)
        "Aries": ("02h30m00s", "+20d00m00s"),
        "Taurus": ("04h30m00s", "+20d00m00s"),
        "Gemini": ("06h30m00s", "+20d00m00s"),
        "Cancer": ("08h30m00s", "+20d00m00s"),
        "Leo": ("10h30m00s", "+20d00m00s"),
        "Virgo": ("12h30m00s", "+00d00m00s"),
        "Libra": ("14h30m00s", "-10d00m00s"),
        "Scorpius": ("16h30m00s", "-30d00m00s"),
        "Sagittarius": ("18h30m00s", "-30d00m00s"),
        "Capricornus": ("20h30m00s", "-20d00m00s"),
        "Aquarius": ("22h30m00s", "-10d00m00s"),
        "Pisces": ("00h30m00s", "+10d00m00s")
    }

    name = name.strip().lower()

    if time is None:
        raise ValueError("يجب تمرير الوقت لحساب موقع الأجرام الديناميكية.")

    solar_bodies = [
        "sun", "moon", "mercury", "venus", "earth", "mars",
        "jupiter", "saturn", "uranus", "neptune", "pluto"
    ]

    if name in solar_bodies:
        with solar_system_ephemeris.set("builtin"):
            return get_body(name, time)

    for k in catalog:
        if k.lower() == name:
            ra, dec = catalog[k]
            return SkyCoord(ra=ra, dec=dec, frame="icrs")

    return SkyCoord.from_name(name)