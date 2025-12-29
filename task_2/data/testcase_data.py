import random
import string
from datetime import datetime


def task_name():
    random_str = ''.join(
        random.choices(string.ascii_letters + string.digits, k=10))
    name = f'Test Task {random_str}_{datetime.now().strftime("%H%M%S")}'
    return name


def task_description(word_count=10):
    description = []
    for _ in range(word_count):
        word_length = random.randint(1, 8)
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        description.append(word)
    return ' '.join(description)


def project_name_id():
    return random.randint(1, 6)


def priority_name():
    list_priority = ["Low", "Medium", "High"]
    return list_priority[random.randint(0, 2)]


def executor_name_id():
    return random.randint(1, 7)


def status_name():
    list_status = ["Backlog", "InProgress", "Done"]
    return list_status[random.randint(0, 2)]


def dashboard_name():
    list_dashboard = ["Редизайн карточки товара", "Все",
                      "Оптимизация производительности", "Рефакторинг API",
                      "Миграция на новую БД", "Автоматизация тестирования",
                      "Переход на Kubernetes"]
    return list_dashboard[random.randint(0, 6)]
