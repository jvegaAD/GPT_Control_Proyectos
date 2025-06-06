diff --git a//dev/null b/backend/main.py
index 0000000000000000000000000000000000000000..e6e5f825c89449fe79c05cea10eca501b04f8059 100644
--- a//dev/null
+++ b/backend/main.py
@@ -0,0 +1,60 @@
+from fastapi import FastAPI, HTTPException
+from pydantic import BaseModel
+from typing import List, Optional
+
+app = FastAPI(title="Control de Proyectos")
+
+# ---- Modelos ----
+class Task(BaseModel):
+    id: int
+    responsable: str
+    tema: str
+    tarea: str
+    fecha_inicio: str
+    fecha_termino: str
+    avance_proyectado: float
+    avance_real: float
+    estado_avance: str
+    comentarios: Optional[str] = None
+
+# ---- Almacenamiento temporal ----
+# En una app real, estos datos se leerían y escribirían en un
+# archivo Excel en OneDrive mediante Microsoft Graph API.
+tasks_db: List[Task] = []
+
+# ---- Funciones simuladas para OneDrive ----
+def read_tasks_from_onedrive() -> List[Task]:
+    """Leer tareas desde Excel en OneDrive (simulado)."""
+    # TODO: implementar llamada real a Microsoft Graph API
+    return tasks_db
+
+def save_tasks_to_onedrive(tasks: List[Task]) -> None:
+    """Guardar tareas en Excel en OneDrive (simulado)."""
+    # TODO: implementar llamada real a Microsoft Graph API
+    pass
+
+# ---- Endpoints ----
+@app.on_event("startup")
+def startup_event():
+    # Cargar datos iniciales desde OneDrive al iniciar
+    global tasks_db
+    tasks_db = read_tasks_from_onedrive()
+
+@app.get("/tasks", response_model=List[Task])
+def list_tasks():
+    return tasks_db
+
+@app.post("/tasks", response_model=Task)
+def create_task(task: Task):
+    tasks_db.append(task)
+    save_tasks_to_onedrive(tasks_db)
+    return task
+
+@app.put("/tasks/{task_id}", response_model=Task)
+def update_task(task_id: int, updated: Task):
+    for index, task in enumerate(tasks_db):
+        if task.id == task_id:
+            tasks_db[index] = updated
+            save_tasks_to_onedrive(tasks_db)
+            return updated
+    raise HTTPException(status_code=404, detail="Tarea no encontrada")
