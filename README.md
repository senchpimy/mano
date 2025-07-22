# Mano

![Badge](https://img.shields.io/badge/License-MIT-blue) 
![Badge](https://img.shields.io/badge/Version-1.0.0-green)

**Mano** es un sistema de control de servomotores que replica la posición de los dedos de una mano humana en tiempo real. Utiliza visión por computadora con MediaPipe y OpenCV para detectar los gestos, y envía comandos vía serial a un microcontrolador Arduino que controla cinco servos, uno por cada dedo.

---

## 📸 Características

- Seguimiento en tiempo real de la mano con cámara web.
- Detección de cada dedo usando MediaPipe.
- Cálculo proporcional de la flexión de los dedos.
- Comunicación vía Serial con Arduino para controlar servomotores.
- Código modular y fácil de extender.

---

## 🚀 Instalación

### Python (PC)

1. Instala las dependencias:
```bash
pip install opencv-python mediapipe numpy pyserial
````

2. Ejecuta el script principal:

```bash
python main.py
```

> Asegúrate de que el archivo `hand.py` esté en el mismo directorio.

### Arduino

1. Abre el archivo `.ino` en el IDE de Arduino.
2. Sube el código a tu placa (ej: Arduino Uno).
3. Asegúrate de tener los servos conectados en los pines:

| Dedo    | Pin |
| ------- | --- |
| Pulgar  | D4  |
| Índice  | D5  |
| Medio   | D6  |
| Anular  | D7  |
| Meñique | D8  |

---

## 🧠 Lógica de funcionamiento

1. **Detección:** Se detectan los landmarks de la mano con `mediapipe.solutions.hands`.
2. **Distancia y normalización:** Se calcula la distancia entre las puntas de los dedos y sus respectivas articulaciones MCP. Estas distancias se normalizan con una regla de tres basada en la distancia entre la muñeca y el MCP del dedo medio.
3. **Mapeo a ángulos:** El valor resultante se convierte a un ángulo entre 0 y 180 grados.
4. **Serial:** Se envía un byte con el dedo (`T`, `I`, `M`, `R`, `P`) y tres dígitos representando el ángulo (`003` a `180`) al Arduino.
5. **Servo:** El Arduino interpreta el comando y mueve el servo correspondiente.

---

## 🧩 Ejemplo de datos enviados

```text
T090  # Pulgar a 90 grados
I045  # Índice a 45 grados
```

---

## 🛠 Archivos

* `main.py`: Script principal que lee la cámara y envía comandos.
* `hand.py`: Clase `hand` que implementa funciones `thumb()`, `index()`, etc., para enviar datos seriales.
* `Mano.ino`: Código de Arduino que recibe comandos y mueve servos.

---

## 📜 Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.

