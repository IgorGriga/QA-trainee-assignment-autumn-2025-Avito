## Структура проекта


    QA-trainee-assignment-autumn-2025-Avito
    ├── task_1
    │   ├── bugs.md
    │   └── bugs.png
    ├── task_2
    │   ├── base
    │   │   ├── __init__.py
    │   │   ├── base_page.py
    │   │   └── locators.py
    │   ├── data
    │   │   ├── __init__.py
    │   │   └── testcase_data.py
    │   ├── images
    │   │   ├── BR1.png
    │   │   └── BR2.png
    │   ├── pages
    │   │   ├── __init__.py
    │   │   ├── create_task_page.py
    │   │   ├── open_task_page.py
    │   │   ├── project_board_page.py
    │   │   └── search_task_page.py
    │   ├── tests
    │   │   ├── __init__.py
    │   │   ├── test_create_task.py
    │   │   ├── test_open_task.py
    │   │   ├── test_project_board.py
    │   │   └── test_search_task.py
    │   ├── __init__.py
    │   ├── BUGS.md
    │   ├── conftest.py
    │   └── TESTCASES.md
    ├── .gitignore
    ├── README.md
    └── requirements.txt

<br>

## Инструкция

1. Скопируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале
    ```  
    git clone https://github.com/IgorGriga/QA-trainee-assignment-autumn-2025-Avito.git
    ```  
    Или скачайте zip-архив по [ссылке](https://github.com/IgorGriga/QA-trainee-assignment-autumn-2025-Avito/archive/refs/heads/main.zip) и распакуйте его

2. Убедитесь, что на вашем компьютере установлен Python. В командной строке/терминале выполните команду
    ```  
    python --version || python3 --version
    ```    
    Если он не установлен, то установите с официального [сайта Python](https://www.python.org/downloads/), выбрав подходящую версию для вашей операционной системы, и пройдите шаг сначала. В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH".

3. Через командную строку/терминал перейдите в корневую директорию проекта, выполнив команду
   ```  
   cd C:\путь\к\проекту\QA-trainee-assignment-autumn-2025-Avito
   ```
4. Создайте виртуальное окружение
    ```
    python3 -m venv .venv
    ```
5. Активируйте окружение  
    macOS или Linux
    ```
    source .venv/bin/activate
    ```
    Windows
    ```
    .venv\Scripts\activate
    ```
6. Установите необходимые зависимости из файла `requirements.txt`, выполнив команду
   ```  
   pip install -r requirements.txt
   ```  
   если она не выполняется, то попробуйте
   ```  
   pip3 install -r requirements.txt
   ```
7. Наконец, запустите тесты, выполнив команду
   ```  
   pytest -v
   ```
**Важные замечания:**
- Тесты используют **Selenium 4+** и запускаются в браузере **Google Chrome**.
- Начиная с Selenium 4.6, веб-драйвер (chromedriver) скачивается и обновляется **автоматически** с помощью Selenium Manager — вручную ничего устанавливать не нужно.
- Убедитесь, что у вас установлен **Google Chrome** актуальной версии (рекомендуется последняя стабильная версия).
- При первом запуске тестов может потребоваться несколько секунд на автоматическую загрузку chromedriver.
