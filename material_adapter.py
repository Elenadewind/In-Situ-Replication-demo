python
import numpy as np

# База данных материалов (пример)
materials_db = {
    'SiO2': {'conductivity': 0.1, 'melting_point': 1700},
    'Fe': {'conductivity': 10, 'melting_point': 1500},
}

# Шаблон детали (требует материал с conductivity >= 5)
target_props = {'conductivity': 8}

# ИИ‑алгоритм: поиск ближайшего аналога
def find_substitute(target, db):
    best = None
    best_score = float('inf')
    for mat, props in db.items():
        score = abs(props['conductivity'] - target['conductivity'])
        if score < best_score:
            best, best_score = mat, score
    return best

substitute = find_substitute(target_props, materials_db)
print("Заменитель:", substitute)  # Например, 'Fe'
