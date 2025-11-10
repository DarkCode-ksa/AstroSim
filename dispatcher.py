from core.alignment import run_alignment
from core.inverse_alignment import run_inverse_alignment
from core.precession import run_precession
from core.obliquity import run_obliquity
from core.polar_motion import run_polar_motion
from core.magnetic_field import run_magnetic_field
from core.distance import run_distance

def dispatch_simulation(sim):
    sim_type = sim.get("type", "").strip().lower()
    handlers = {
        "alignment": run_alignment,
        "inverse_alignment": run_inverse_alignment,
        "precession": run_precession,
        "obliquity": run_obliquity,
        "polar_motion": run_polar_motion,
        "magnetic_field": run_magnetic_field,
        "distance": run_distance
    }

    if sim_type in handlers:
        handlers[sim_type](sim)
    else:
        raise ValueError(f"نوع غير مدعوم: {sim_type}")