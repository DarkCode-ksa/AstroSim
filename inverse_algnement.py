def run_inverse_alignment(sim):
    """
    يبحث عن جرم سماوي في اتجاه معين بناءً على التاريخ والموقع.
    """
    direction = sim.get('direction', 'north')
    date = sim.get('date', 'غير محدد')
    lat = sim.get('lat', '؟')
    lon = sim.get('lon', '؟')

    print(f"🔍 البحث عن جرم سماوي في اتجاه {direction} بتاريخ {date} عند الموقع ({lat}, {lon})")

    # محاكاة وهمية للنتيجة
    result = {
        'name': 'Sirius',
        'azimuth': 101.3,
        'altitude': 45.7
    }

    print(f"✅ تم العثور على {result['name']} عند زاوية {result['azimuth']}° وارتفاع {result['altitude']}°")
