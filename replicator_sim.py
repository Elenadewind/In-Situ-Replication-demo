python
import matplotlib.pyplot as plt
import numpy as np

class Replicator:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.copies = 0

    def replicate(self, others):
        if self.copies < 3:  # Лимит на 3 копии
            new = Replicator(self.x + np.random.randn(), self.y + np.random.randn())
            others.append(new)
            self.copies += 1
            return new
        return None

# Симуляция
nodes = [Replicator(0, 0)]
for step in range(5):
    new_nodes = []
    for node in nodes:
        new = node.replicate(nodes)
        if new:
            new_nodes.append(new)
    nodes.extend(new_nodes)

# Визуализация
plt.scatter([n.x for n in nodes], [n.y for n in nodes], s=20)
plt.title(f"Репликаторы после {step+1} шагов")
plt.show()
