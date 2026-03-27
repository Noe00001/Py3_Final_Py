# ─────────────────────────────────────────
# service.py  —  Módulo 1
# Lógica CRUD · datos en memoria (sin archivos aún)
# ─────────────────────────────────────────

from validate import validate_id, validate_name, validate_email
from validate import used_ids, used_emails

# ── Almacenamiento en memoria ──────────────
records: list[dict] = []


def create_record(id: int, name: str, email: str) -> bool:
    """
    Crea un nuevo registro si los datos son válidos.
    Retorna True si fue creado, False si fue rechazado.
    """
    if not validate_id(id):
        return False
    if not validate_name(name):
        return False
    if not validate_email(email):
        return False

    record = {"id": id, "name": name.strip(), "email": email.strip()}
    records.append(record)
    used_ids.add(id)
    used_emails.add(email)
    print(f"  [OK] Registro creado: {record}")
    return True


def list_records() -> None:
    """Imprime todos los registros almacenados en memoria."""
    if not records:
        print("  [i] No hay registros aún.")
        return

    print(f"\n  {'ID':<6} {'Nombre':<20} {'Email'}")
    print(f"  {'-'*6} {'-'*20} {'-'*25}")
    for r in records:
        print(f"  {r['id']:<6} {r['name']:<20} {r['email']}")
    print(f"\n  Total: {len(records)} registro(s)\n")