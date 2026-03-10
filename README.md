# 🏛️ IA Soberana Jalisco 2026: Servidor de IA Local

Este repositorio contiene la arquitectura de software y los scripts de despliegue para el programa **"IA Soberana"**. El objetivo es habilitar un nodo central de procesamiento de Inteligencia Artificial para abastecer a 15 estaciones de trabajo basadas en Raspberry Pi 5.

---

## 🚀 Alcance del Proyecto
El proyecto implementa un entorno de ejecución de Modelos de Lenguaje de Gran Escala (LLMs) como **Qwen3** y **Llama 3**, optimizados para hardware NVIDIA local, eliminando la dependencia de APIs externas y garantizando la privacidad de los datos.

### Características Principales:
* **Motor de Inferencia:** [Ollama](https://ollama.ai/) para la gestión de modelos.
* **Interfaz de Usuario:** [Open-WebUI](https://github.com/open-webui/open-webui) (Dockerizado).
* **Conectividad:** Túneles seguros vía **Cloudflare Zero Trust**.
* **Red:** Segmentación por VLANs mediante **Ubiquiti UniFi Gateway**.

---

## 🛠️ Requerimientos del Sistema (Servidor)

### Hardware Recomendado:
* **GPU:** NVIDIA RTX 5070 Ti (16GB VRAM) o superior.
* **CPU:** AMD Ryzen 9 9900X (12 núcleos).
* **RAM:** 128GB DDR5.
* **SO:** Ubuntu Server 24.04 LTS.

### Software Necesario:
* NVIDIA Drivers (550+)
* Docker & Docker Compose
* Python 3.11+
* Cloudflared (Cloudflare Tunnel)

---

## 📦 Instalación Rápida

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/acidkeyxyz/python-ai-course.git](https://github.com/acidkeyxyz/python-ai-course.git)
   cd ia-soberana-jalisco
   python3 ollama-client.py
```