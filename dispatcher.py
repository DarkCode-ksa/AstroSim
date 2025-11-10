from alignment import run_alignment
from inverse_alignment import run_inverse_alignment
from distance import run_distance
from obliquity import run_obliquity
from magnetic_field import run_magnetic_field
from validator import validate_simulation

def run_simulation(sim):
    """
    ينفذ نوع المحاكاة المحدد في config.ini بناءً على المفتاح 'type'.
    """
    if not validate_simulation(sim):
        print(f"⚠️ المحاكاة {sim['name']} غير صالحة، تم تخطيها.")
        return

    sim_type = sim.get('type', '').lower()

    if sim_type == 'alignment':
        run_alignment(sim)

    elif sim_type == 'inverse_alignment':
        run_inverse_alignment(sim)

    elif sim_type == 'distance':
        run_distance(sim)

    elif sim_type == 'obliquity':
        run_obliquity(sim)

    elif sim_type == 'magnetic_field':
        run_magnetic_field(sim)

    else:
        print(f"❌ نوع المحاكاة غير مدعوم: {sim_type}")
