import subprocess

def run_tests():
    result = subprocess.run(["python", "-m", "unittest", "discover", "-s", ".", "-p", "tests.py"])
    return result.returncode == 0

def deploy():
    print("Deployed")

def main():
    print("Крок 1: Запуск юніт-тестів для застосунка...")
    if run_tests():
        print("Крок 2: Симуляція деплою застосунка")
        deploy()
    else:
        print("Деплой не запущений, оскільки є помилки у тестах.")

if __name__ == "__main__":
    main()
