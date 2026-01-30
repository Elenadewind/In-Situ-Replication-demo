```python
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Генерируем шаблон (матрица параметров конструкции)
template = np.random.rand(10, 10)

# 2. Имитируем передачу с ошибками
noisy_signal = template + np.random.normal(0, 0.1, template.shape)

# 3. Модель ИИ для восстановления
model = Sequential([
 Dense(64, activation='relu', input_shape=(10,)),
 Dense(10, activation='linear')
])
model.compile(optimizer='adam', loss='mse')
model.fit(noisy_signal, template, epochs=10, verbose=0)

# 4. Восстанавливаем шаблон
recovered = model.predict(noisy_signal)
print("Ошибка восстановления:", np.mean(np.abs(recovered - template)))
