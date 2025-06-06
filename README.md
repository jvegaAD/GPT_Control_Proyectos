
# 🚀 App Web Control de Proyectos con Carta Gantt 📊

## 🎯 Características
- Visualización de carta Gantt con tareas:  
  **ID, Responsable, Tema, Tarea, Fecha Inicio, Fecha Término, Avance Proyectado, Avance Real, Estado de Avance, Comentarios**
- Filtrar por responsable y tema.
- Gráficos de avance proyectado y real.
- Clasificación por avance: 🟩 Adelantado | 🟦 En curso | 🟥 Atrasado | ⬜ No iniciado.
- Edición y registro de tareas, comentarios y estado desde la web.
- Sincronización automática con Excel en OneDrive (Microsoft Graph API).
- Toda la información persiste en el Excel, no en BD local.
- Autenticación con cuenta Microsoft.

---

## 🛠️ Tecnologías sugeridas
- Backend: Python (Django/FastAPI) o Node.js
- Frontend: React, Vue o similar + Gantt (ej: react-gantt-tasks, dhtmlx-gantt)
- API: Microsoft Graph

---

## 📄 Columnas principales
- ID
- Responsable
- Tema
- Tarea
- Fecha Inicio
- Fecha Término
- Avance Proyectado
- Avance Real
- Estado de Avance
- Comentarios

---

## 🌟 Extras opcionales
- Exportar reportes en PDF o Excel
- Carga masiva desde Excel
- Notificaciones por email al cambiar estado

---

## 🗂️ Esquema Base de Datos (Django ORM)
```python
class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    responsable = models.CharField(max_length=100)
    tema = models.CharField(max_length=200)
    tarea = models.CharField(max_length=400)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    avance_proyectado = models.DecimalField(max_digits=5, decimal_places=2)
    avance_real = models.DecimalField(max_digits=5, decimal_places=2)
    estado_avance = models.CharField(max_length=50)
    comentarios = models.TextField(blank=True, null=True)
```

---

## 🔗 Integración con OneDrive (Python + Graph API)
```python
import requests
access_token = 'TU_TOKEN_AQUI'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
excel_url = "https://graph.microsoft.com/v1.0/me/drive/root:/ruta/archivo.xlsx:/workbook/worksheets('Sheet1')/usedRange"
response = requests.get(excel_url, headers=headers)
data = response.json()
# Consultar Graph API para PATCH/POST
```

---

## 💻 Front-end recomendado
- React + react-gantt-tasks / dhtmlx-gantt
- API REST al backend
- Backend manipula Excel en OneDrive

---

## 📝 Diagrama de Flujo
```
Usuario (web) → Frontend (React) → Backend (API Python/Node) → OneDrive Excel (Microsoft Graph API)
                                                      ↑
                                            Autenticación Microsoft
```

---

## 🎨 Clasificación de Estado de Avance
- 🟩 Adelantado: avance real > proyectado
- 🟦 En curso: avance real == proyectado
- 🟥 Atrasado: avance real < proyectado
- ⬜ No iniciado: avance real == 0

---

## 📋 Resumen
App web editable con carta Gantt, sincronización en tiempo real con Excel de OneDrive, filtros útiles para gestión y autenticación vía Microsoft.
