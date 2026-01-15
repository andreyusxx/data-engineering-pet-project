import csv
import random
from faker import Faker
import os
from datetime import datetime, timedelta

# Ініціалізація генератора фейкових даних
fake = Faker()

# Налаштування
NUM_USERS = 100        # Створимо 100 клієнтів
NUM_ORDERS = 500       # Створимо 500 замовлень
DATA_DIR = 'data'      # Папка для збереження файлів

# Створюємо папку data, якщо її немає
os.makedirs(DATA_DIR, exist_ok=True)

def generate_users():
    """Генерує CSV файл з користувачами"""
    print(f"Generating {NUM_USERS} users...")
    file_path = os.path.join(DATA_DIR, 'users.csv')
    
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Заголовки (назви стовпців)
        writer.writerow(['user_id', 'first_name', 'last_name', 'email', 'address', 'created_at'])
        
        for i in range(1, NUM_USERS + 1):
            writer.writerow([
                i,
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                fake.address().replace('\n', ', '), # Прибираємо переноси рядків в адресі
                fake.date_time_between(start_date='-1y', end_date='now') # Дата реєстрації за останній рік
            ])
    print(f"✅ Users saved to {file_path}")

def generate_orders():
    """Генерує CSV файл із замовленнями"""
    print(f"Generating {NUM_ORDERS} orders...")
    file_path = os.path.join(DATA_DIR, 'orders.csv')
    
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['order_id', 'user_id', 'order_date', 'status', 'total_amount'])
        
        for i in range(1, NUM_ORDERS + 1):
            writer.writerow([
                i,
                random.randint(1, NUM_USERS), # Випадковий юзер від 1 до 100
                fake.date_time_between(start_date='-1y', end_date='now'),
                random.choice(['completed', 'processing', 'cancelled', 'shipped']),
                round(random.uniform(10.0, 500.0), 2) # Сума від 10 до 500
            ])
    print(f"✅ Orders saved to {file_path}")

if __name__ == "__main__":
    generate_users()
    generate_orders()