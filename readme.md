# 🧪 Sistema Legacy de Orquestación de Pagos  
## Ejercicio de Análisis y Refactorización de Arquitectura

Este proyecto simula un **sistema real de orquestación de pagos multi-tenant**, utilizado por una fintech para procesar pagos a través de distintos medios externos.

El sistema **funciona correctamente** y puede ejecutarse desde consola, pero presenta **problemas estructurales intencionales** que dificultan su evolución, mantenimiento y escalabilidad.

El objetivo del ejercicio es **analizar el código existente, identificar los problemas de diseño y mejorar la arquitectura**, manteniendo el comportamiento funcional.

---

## 🎯 Objetivo del ejercicio

El equipo debe **mejorar la calidad del diseño del sistema** para que:

- Sea fácil agregar nuevos medios de pago
- Las reglas de negocio no estén duplicadas
- El código sea fácil de extender sin modificar componentes existentes
- Las responsabilidades estén claramente separadas
- El sistema sea más legible, testeable y mantenible

⚠️ **Restricción clave:**  
El resultado observable del sistema **no debe cambiar**.

---

## ▶️ Ejecución del sistema

El sistema debe ejecutarse **exclusivamente desde el punto de entrada definido**.

```bash
python main.py
