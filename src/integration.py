import validate

def generate_fake_records(*args, **kwargs):
    try:
        from faker import Faker
    except ImportError:
        print("Faker no está instalado. Ejecuta: pip install faker")
        return False

    count  = kwargs.get("count",  10)
    locale = kwargs.get("locale", "es_MX")

    fake = Faker(locale)

    valid_ids = [u.get("id") for u in validate.users if isinstance(u.get("id"), int)]
    next_id   = max(valid_ids) + 1 if valid_ids else validate.id_counter

    generated = []
    for i in range(count):
        user = {
            "id":     next_id + i,
            "name":   fake.name(),
            "email":  fake.email(),
            "age":    fake.random_int(min=1, max=99),
            "status": fake.random_element(["activo", "inactivo"]),
        }
        generated.append(user)

    validate.users.extend(generated)
    validate.id_counter = next_id + count
    display_fields = args if args else ("name", "email")
    print(f"\n{count} registros generados (locale={locale}):")
    for u in generated:
        summary = "  |  ".join(f"{f}: {u.get(f, '?')}" for f in display_fields)
        print(f"  [{u['id']}]  {summary}")

    return True
