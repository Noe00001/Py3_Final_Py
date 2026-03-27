from service import create_record, list_records

print("=" * 45)
print("  MODULO 1 - Estructura y validaciones base")
print("=" * 45)

create_record(1, "Ana Garcia",  "ana@mail.com")
create_record(2, "Luis Torres", "luis@mail.com")
create_record(3, "Maria Ruiz",  "maria@mail.com")

print("\n--- Intentos invalidos ---")

create_record(1, "Otro nombre", "otro@mail.com")
create_record(4, "Carlos",      "ana@mail.com")
create_record(5, "   ",         "vacio@mail.com")
create_record(-1, "Juan",       "juan@mail.com")

print("\n--- Lista final ---")
list_records()