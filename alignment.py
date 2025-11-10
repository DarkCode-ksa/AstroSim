from astronomy import get_star_coords
import matplotlib.pyplot as plt

def run_alignment(sim):
    coords = get_star_coords(sim['targets'], sim['date'])
    lat = float(sim['lat'])
    lon = float(sim['lon'])

    if sim.get('plot', False):
        plt.figure()
        for star, (az, alt) in coords.items():
            plt.plot(az, alt, 'o', label=star)
        plt.xlabel('Azimuth')
        plt.ylabel('Altitude')
        plt.title(f"Alignment: {sim['name']}")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"output/{sim['name']}.png")
        plt.close()

    print(f"✅ تم تنفيذ محاذاة {sim['name']} بنجاح.")
