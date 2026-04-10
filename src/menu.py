from colorama import Fore, Back, Style, init
import validate
from service import new_register, list_records, search_records, update_record, delete_record
from file import load_data, save_data
from integration import generate_fake_records, export_report, fetch_api_users

init(autoreset=True)


def load_users_into_memory():
    """Sincroniza usuarios e id_counter desde el archivo JSON."""
    initial_users = load_data()
    validate.users.clear()
    validate.users.extend(initial_users)

    valid_ids = [
        user.get("id")
        for user in initial_users
        if isinstance(user, dict) and isinstance(user.get("id"), int)
    ]
    validate.id_counter = max(valid_ids) + 1 if valid_ids else 1


load_users_into_memory()

while True:
    print(f"\n{Fore.CYAN}{Back.BLACK}{'='*40}")
    print(f"{Fore.CYAN}{Back.BLACK}  Menú de Gestión de Usuarios")
    print(f"{Fore.CYAN}{Back.BLACK}{'='*40}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}  1. Crear usuario")
    print(f"{Fore.GREEN}  2. Listar registros")
    print(f"{Fore.GREEN}  3. Buscar registros")
    print(f"{Fore.GREEN}  4. Actualizar usuario")
    print(f"{Fore.GREEN}  5. Eliminar usuario")
    print(f"{Fore.YELLOW}  6. Guardar datos")
    print(f"{Fore.CYAN}{Back.BLACK}{'─'*40}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}  7. Generar registros falsos (Faker)")
    print(f"{Fore.MAGENTA}  8. Exportar reporte CSV   (Pandas)")
    print(f"{Fore.MAGENTA}  9. Importar usuarios API  (Requests)")
    print(f"{Fore.CYAN}{Back.BLACK}{'─'*40}{Style.RESET_ALL}")
    print(f"{Fore.RED}  0. Salir{Style.RESET_ALL}")

    option = input(f"\n{Fore.LIGHTBLUE_EX}Seleccione una opción: {Style.RESET_ALL}")

    if option == "1":
        user_created = new_register()
        if user_created:
            print(f"{Fore.GREEN}✓ Usuario creado en memoria. Use la opción 6 para guardarlo.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ No se pudo crear el usuario.{Style.RESET_ALL}")

    elif option == "2":
        list_records()

    elif option == "3":
        search_records()

    elif option == "4":
        update_record()

    elif option == "5":
        delete_record()

    elif option == "6":
        if save_data(validate.users):
            print(f"{Fore.GREEN}✓ Datos guardados correctamente.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}✗ No se pudieron guardar los datos.{Style.RESET_ALL}")

    elif option == "7":
        try:
            count = int(input(f"{Fore.MAGENTA}¿Cuántos registros deseas generar? (default 10): {Style.RESET_ALL}") or 10)
        except ValueError:
            count = 10
        ok = generate_fake_records("name", "email", "status", count=count, locale="es_MX")
        if ok:
            print(f"{Fore.GREEN}✓ Registros en memoria. Use la opción 6 para guardarlos.{Style.RESET_ALL}")
