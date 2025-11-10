Proyecto Django — Playground Final

Instrucciones para ejecutar (local):

1. Crear virtualenv e instalar requisitos:
   python -m venv .venv
   .venv\Scripts\activate   (Windows)  -- o: source .venv/bin/activate (Linux/Mac)
   python -m pip install --upgrade pip
   pip install -r requirements.txt

2. Configurar base de datos (por defecto sqlite). No subir db.sqlite3 al repo.

3. Crear migraciones y migrar:
   python manage.py makemigrations
   python manage.py migrate

4. Crear superusuario:
   python manage.py createsuperuser

5. Servir archivos media en desarrollo:
   python manage.py runserver

Abrir http://127.0.0.1:8000

Cambiar SECRET_KEY en config/settings.py antes de publicar.
