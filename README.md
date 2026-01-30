# In-Situ-Replication-demo
# In‑Situ Replication Simulator

Демонстрация концепции «репликации на месте»: как ИИ передаёт, адаптирует и собирает объекты из местных ресурсов.

## Что внутри

- **template_transmission.py** — симулятор передачи шаблона через шумный канал.
- **material_adapter.py** — подбор аналогов материалов с помощью ИИ.
- **replicator_sim.py** — визуализация роста сети репликаторов.
- **app.py** + **templates/upload.html** — веб‑интерфейс для загрузки шаблонов.

## Как запустить

1. Скопируйте репозиторий:  
   ```bash
   git clone https://github.com/[Elenadewind]/in-situ-replication-demo.git
2. Установите зависимости:

bash
pip install numpy tensorflow matplotlib flask
3. Запустите нужный скрипт (см. разделы ниже).

Демо

## Демо

Веб‑интерфейс доступен *локально* после запуска проекта:

1. Клонируйте репозиторий:  
   ```bash
   git clone https://github.com/Elenadewind/in-situ-replication-demo.git
2. Установите зависимости:

bash
pip install -r requirements.txt
3. Запустите сервер:

bash
python app.py
Откройте в браузере:
http://127.0.0.1:5000

Онлайн‑демо пока не развёрнуто. 
