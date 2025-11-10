from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz
import matplotlib.pyplot as plt
import os
from core.astronomy import get_star_coords

def run_alignment(sim):
    print(f"\n--- محاكاة أمامية: {sim['name']} ---")
    time = Time(sim["date"], format="isot", scale="utc")

    location = EarthLocation(lat=float(sim["lat"]), lon=float(sim["lon"]))
    frame = AltAz(obstime=time, location=location)

    targets = [t.strip() for t in sim.get("targets", "").split(",") if t.strip()]
    if not targets:
        print("❌ لم يتم تحديد أهداف فلكية.")
        return

    altitudes = []
    azimuths = []

    for target in targets:
        try:
            star = get_star_coords(target, time)
            altaz = star.transform_to(frame)
            alt = altaz.alt.degree
            az = altaz.az.degree
            altitudes.append(alt)
            azimuths.append(az)
            print(f"🔹 {target}: ارتفاع {alt:.2f}°، زاوية أفقية {az:.2f}°")
        except Exception as e:
            print(f"⚠️ خطأ في {target}: {e}")

    if sim.get("plot", "false").lower() == "true":
        save_alignment_plot(sim["name"], targets, altitudes, azimuths)

def save_alignment_plot(name, targets, altitudes, azimuths):
    os.makedirs("output", exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(azimuths, altitudes, color="gold", edgecolors="black", s=100)

    for i, label in enumerate(targets):
        ax.text(azimuths[i], altitudes[i] + 1, label, ha="center", fontsize=9)

    ax.set_title(f"محاكاة {name}", fontsize=14)
    ax.set_xlabel("الزاوية الأفقية (°)")
    ax.set_ylabel("الارتفاع (°)")
    ax.grid(True)
    ax.set_xlim(0, 360)
    ax.set_ylim(0, 90)

    filename = f"output/{name}.png"
    fig.savefig(filename, dpi=300)
    plt.close(fig)
    print(f"🖼️ تم حفظ الرسم البياني: {filename}")