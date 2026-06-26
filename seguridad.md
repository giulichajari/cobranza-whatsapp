# Etapa 6 - Seguridad Avanzada

## Objetivo

Implementar una capa de seguridad profesional sobre la API existente sin modificar la arquitectura del proyecto.

La aplicación ya dispone de:

* FastAPI
* SQLAlchemy ORM
* JWT básico
* CORS
* SlowAPI
* Logging
* Arquitectura modular (Controllers, Services, Repositories, Models, Routes)

El objetivo es evolucionar esta implementación hacia un entorno de producción.

---

# Requisitos

## 1. Variables de entorno

Eliminar todas las credenciales hardcodeadas.

Utilizar un archivo `.env` para almacenar:

* SECRET_KEY
* JWT_ALGORITHM
* ACCESS_TOKEN_EXPIRE_MINUTES
* DATABASE_URL
* WHATSAPP_API_KEY (placeholder)
* WHATSAPP_PHONE_ID (placeholder)

Utilizar `python-dotenv` o `pydantic-settings`.

No dejar secretos dentro del código fuente.

---

## 2. Modelo Usuario

Crear una nueva entidad Usuario utilizando SQLAlchemy.

Campos sugeridos:

* id
* username
* nombre
* email
* password_hash
* rol
* activo
* created_at

No almacenar contraseñas en texto plano.

---

## 3. Hash de contraseñas

Implementar hash utilizando bcrypt mediante `passlib` o una librería equivalente.

Debe existir:

* función para generar hash
* función para verificar contraseña

Nunca comparar contraseñas directamente.

---

## 4. Login contra Base de Datos

Modificar el endpoint `/auth/login`.

Actualmente el login utiliza credenciales hardcodeadas.

Debe reemplazarse por:

* búsqueda del usuario en MySQL
* validación mediante bcrypt
* verificar que el usuario esté activo
* generar JWT únicamente si la autenticación es correcta

---

## 5. Dependencia de autenticación

Crear una dependencia reutilizable para obtener el usuario autenticado a partir del JWT.

Debe:

* validar el token
* verificar expiración
* obtener el usuario desde la base de datos
* lanzar HTTP 401 cuando corresponda

Evitar duplicar código entre rutas.

---

## 6. Proteger Endpoints

Aplicar autenticación JWT a los siguientes módulos:

* Clientes
* Pagos
* Configuración

Solo usuarios autenticados podrán acceder.

---

## 7. Roles

Agregar soporte para roles.

Roles mínimos:

Administrador

* acceso total

Operador

* consultar clientes
* registrar pagos
* no puede eliminar clientes
* no puede modificar configuraciones

Implementar dependencias reutilizables para validar permisos.

---

## 8. Mejorar JWT

El token debe contener información mínima:

* sub
* username
* rol
* exp

No almacenar información sensible.

---

## 9. Manejo de errores

Responder correctamente con:

401 Unauthorized

cuando el token sea inválido.

403 Forbidden

cuando el usuario no tenga permisos.

No exponer información sensible en los mensajes de error.

---

## 10. CORS

Actualmente se permite cualquier origen.

Modificar la configuración para leer los dominios permitidos desde variables de entorno.

Ejemplo:

ALLOWED_ORIGINS=[http://localhost:3000,https://miapp.com](http://localhost:3000,https://miapp.com)

---

## 11. Configuración centralizada

Crear un módulo de configuración para evitar acceder directamente a variables de entorno desde distintas partes del proyecto.

Toda la configuración debe obtenerse desde una única clase o archivo.

---

## 12. Organización

Mantener la arquitectura actual.

Ejemplo:

src/
└── app/
├── auth/
│   ├── jwt.py
│   ├── auth_routes.py
│   ├── dependencies.py
│   ├── password.py
│   └── security.py
├── controllers/
├── repositories/
├── services/
├── routes/
├── models/
├── schemas/
├── middleware/
├── database/
└── config/

No romper la estructura existente.

---

# Buenas prácticas

Aplicar tipado estático.

Agregar docstrings cuando sea apropiado.

Seguir principios SOLID.

Evitar duplicación de código.

Mantener separación de responsabilidades.

Utilizar inyección de dependencias de FastAPI.

---

# Restricciones

* No modificar la lógica existente salvo cuando sea necesario para integrar la seguridad.
* No eliminar endpoints existentes.
* Mantener compatibilidad con Swagger/OpenAPI.
* El código debe quedar listo para futuras integraciones con frontend y automatización por WhatsApp.

---

# Resultado esperado

Al finalizar esta etapa, la API deberá contar con:

* Autenticación JWT basada en usuarios almacenados en MySQL.
* Contraseñas protegidas mediante bcrypt.
* Variables de entorno para toda la configuración sensible.
* Endpoints protegidos mediante autenticación.
* Sistema de roles (Administrador y Operador).
* Configuración centralizada.
* CORS configurable.
* Código limpio, modular y preparado para un entorno de producción.
