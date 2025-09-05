import subprocess
import sys
import os

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # Сброс цвета
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def run_pip_command(command: list):
    try:
        full_command = [sys.executable, '-m', 'pip'] + command
        print(f"{Colors.OKCYAN}▶ Выполняется команда: {' '.join(full_command)}{Colors.ENDC}")
        
        result = subprocess.run(
            full_command,
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        if result.stdout:
            print(result.stdout)
            
        print(f"\n{Colors.OKGREEN}✔ Команда успешно выполнена{Colors.ENDC}")
    
    except FileNotFoundError:
        print(f"{Colors.FAIL}❌ Ошибка: Команда 'pip' не найдена. Убедитесь, что Python и pip установлены и добавлены в PATH.{Colors.ENDC}")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}❌ Произошла ошибка при выполнении команды.{Colors.ENDC}")
        print(f"Код возврата: {e.returncode}")
        print(f"{Colors.WARNING}Сообщение от pip:{Colors.ENDC}\n{e.stderr}")
        
def install_package():
    package_name = input("Введите имя пакета для установки: ")
    if package_name:
        run_pip_command(['install', package_name])
    else:
        print(f"{Colors.WARNING}Имя пакета не может быть пустым.{Colors.ENDC}")
        
def uninstall_package():
    package_name = input("Введите имя пакета для удаления: ")
    if package_name:
        run_pip_command(['uninstall', '-y', package_name])
    else:
        print(f"{Colors.WARNING}Имя пакета не может быть пустым.{Colors.ENDC}")
        
def update_package():
    package_name = input("Введите имя пакета для обновления: ")
    if package_name:
        run_pip_command(['install', '--upgrade', package_name])
    else:
        print(f"{Colors.WARNING}Имя пакета не может быть пустым.{Colors.ENDC}")

def list_packages():
    print("Загрузка списка установленных пакетов...")
    run_pip_command(['list'])

def show_menu():
    print(f"\n{Colors.HEADER}{Colors.BOLD}--- Консольный Пакетный Менеджер ---{Colors.ENDC}")
    print("1. Установить пакет")
    print("2. Удалить пакет")
    print("3. Обновить пакет")
    print("4. Показать список установленных пакетов")
    print(f"5. {Colors.FAIL}Выход{Colors.ENDC}")
    return input(f"{Colors.OKBLUE}Выберите действие (1-5): {Colors.ENDC}")

def main():
    while True:
        choice = show_menu()
        if choice == '1':
            install_package()
        elif choice == '2':
            uninstall_package()
        elif choice == '3':
            update_package()
        elif choice == '4':
            list_packages()
        elif choice == '5':
            print(f"{Colors.OKCYAN}Завершение работы...{Colors.ENDC}")
            break
        else:
            print(f"{Colors.WARNING}Неверный выбор. Пожалуйста, введите число от 1 до 5.{Colors.ENDC}")
        
        input("\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()