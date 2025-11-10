def validate_simulation(sim):
    required = {
        "alignment": ["name", "lat", "lon", "date", "targets"],
        "inverse_alignment": ["name", "lat", "lon", "date", "azimuth", "altitude"],
        "polar_motion": ["name", "date", "location"],
        "magnetic_field": ["name", "date", "location"]
    }
    sim_type = sim.get("type", "").lower()
    if sim_type not in required:
        print(f"❌ نوع غير معروف: {sim_type}")
        return False
    missing = [f for f in required[sim_type] if f not in sim]
    if missing:
        print(f"❌ المحاكاة '{sim.get('name')}' تفتقد: {', '.join(missing)}")
        return False
    return True