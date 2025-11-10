import os
from parser import load_config
from dispatcher import run_simulation

def main():
    print("🔭 بدء تشغيل AstroSim...")

    # تحديد مسار ملف الإعدادات
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')

    # تحميل إعدادات المحاكاة
    simulations = load_config(config_path)

    if not simulations:
        print("⚠️ لم يتم العثور على محاكيات صالحة في config.ini")
        return

    # تنفيذ كل محاكاة
    for sim in simulations:
        print(f"\n🚀 تشغيل المحاكاة: {sim['name']} ({sim['type']})")
        try:
            run_simulation(sim)
        except Exception as e:
            print(f"❌ خطأ أثناء تشغيل {sim['name']}: {e}")

    print("\n✅ تم الانتهاء من جميع المحاكيات.")

if __name__ == "__main__":
    main()
