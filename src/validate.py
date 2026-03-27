# ─────────────────────────────────────────
# validate.py  —  Módulo 1
# Funciones puras de validación + sets globales
# ─────────────────────────────────────────

used_ids: set = set()       # IDs ya registrados
used_emails: set = set()    # Emails ya registrados


def validate_id(id: int) -> bool:
    """El ID debe ser un entero positivo y no repetido."""
    if not isinstance(id, int) or id <= 0:
        print(f"  [!] ID inválido: debe ser un entero positivo.")
        return False
    if id in used_ids:
        print(f"  [!] ID '{id}' ya existe. No se permiten duplicados.")
        return False
    return True


def validate_name(name: str) -> bool:
    """El nombre no puede estar vacío ni ser solo espacios."""
    if not isinstance(name, str) or not name.strip():
        print(f"  [!] Nombre inválido: no puede estar vacío.")
        return False
    return True


def validate_email(email: str) -> bool:
    """El email debe contener '@' y no estar repetido."""
    if not isinstance(email, str) or "@" not in email:
        print(f"  [!] Email inválido: debe contener '@'.")
        return False
    if email in used_emails:
        print(f"  [!] Email '{email}' ya registrado.")
        return False
    return True