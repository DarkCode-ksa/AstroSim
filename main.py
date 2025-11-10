from core.parser import load_config
from core.validator import validate_simulation
from core.dispatcher import dispatch_simulation

def main():
    print("🔭 AstroSim – منصة المحاكاة الفلكية والجيوفيزيائية\n")
    simulations = load_config("config.ini")
    log = []

    for sim in simulations:
        sim_type = sim.get("type", "").strip().lower()
        sim_name = sim.get("name", "غير معروفة")

        print(f"\n🧪 تشغيل: {sim_name} ({sim_type})")

        if not validate_simulation(sim):
            log.append((sim_name, "❌ فشل التحقق"))
            continue

        try:
            dispatch_simulation(sim)
            log.append((sim_name, "✅ تم التنفيذ"))
        except Exception as e:
            print(f"❌ خطأ أثناء التنفيذ: {e}")
            log.append((sim_name, f"❌ خطأ: {e}"))

    print("\n📋 سجل المحاكيات:")
    for name, status in log:
        print(f"• {name}: {status}")

if __name__ == "__main__":
    main()