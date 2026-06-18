# Sistema de Cobranza WhatsApp

## Objetivo

Desarrollar una plataforma para la gestión de clientes y automatización de cobranzas para servicios IPTV.

El sistema permitirá administrar clientes, registrar pagos, automatizar recordatorios de vencimiento mediante WhatsApp y generar información útil para optimizar el proceso de cobranza.

Actualmente el proyecto se encuentra en desarrollo siguiendo una arquitectura modular basada en FastAPI y SQLAlchemy.

---

# Problema a Resolver

Muchas empresas de IPTV administran sus clientes mediante planillas de cálculo o procesos manuales.

Esto genera problemas como:

* Olvido de recordatorios de pago.
* Demoras en la cobranza.
* Falta de seguimiento de clientes morosos.
* Escasa trazabilidad de pagos realizados.
* Dificultad para escalar la operación a cientos de clientes.
* Exceso de tareas administrativas repetitivas.

El objetivo del sistema es automatizar estos procesos para mejorar la eficiencia operativa y aumentar la tasa de cobranza.

---

# Tecnologías Utilizadas

* Python
* FastAPI
* SQLAlchemy ORM
* MySQL
* Pydantic
* Uvicorn
* SlowAPI
* APScheduler (próximamente)

---

# Arquitectura

El proyecto utiliza una arquitectura modular organizada por responsabilidades.

```text
src/
└── app/
    ├── controllers/
    ├── models/
    ├── routes/
    ├── schemas/
    ├── database/
    ├── middleware/
    ├── services/
    └── repositories/
```

### Componentes

**Controllers**

* Contienen la lógica de negocio.

**Models**

* Representan las tablas de la base de datos mediante SQLAlchemy.

**Routes**

* Definen los endpoints REST expuestos por la API.

**Schemas**

* Validan los datos de entrada y salida mediante Pydantic.

**Database**

* Gestiona la conexión y sesiones de base de datos.

**Middleware**

* Implementa funcionalidades transversales como seguridad y control de tráfico.

---

# Funcionalidades Implementadas

## API REST

La aplicación expone endpoints REST documentados automáticamente mediante Swagger/OpenAPI.

Documentación disponible en:

```text
http://localhost:8000/docs
```

---

# Estado del Proyecto

## Etapa 1 - Configuración Inicial

### Objetivo

Crear la estructura base del proyecto y preparar el entorno de desarrollo.

### Implementaciones

* Inicialización del proyecto con Python.
* Configuración de FastAPI.
* Configuración de Uvicorn.
* Organización inicial de carpetas.
* Endpoint de verificación de estado (`/`).
* Generación automática de documentación Swagger.

### Resultado

La API quedó preparada para recibir nuevas funcionalidades y exponer endpoints REST.

---

## Etapa 2 - Gestión de Clientes

### Objetivo

Implementar la persistencia de datos y el manejo de clientes.

### Implementaciones

#### Base de Datos

* Configuración de MySQL.
* Creación de conexión mediante SQLAlchemy.
* Gestión de sesiones de base de datos.

#### Modelo Cliente

Se creó la entidad Cliente con los siguientes atributos:

* ID
* Nombre
* Teléfono
* Email
* Fecha de vencimiento
* Estado activo/inactivo

#### Schemas Pydantic

Validación de:

* Creación de clientes.
* Actualización de clientes.
* Respuestas de la API.

#### CRUD Completo

Se implementaron las operaciones:

* Crear cliente
* Listar clientes
* Obtener cliente por ID
* Actualizar cliente
* Eliminar cliente

#### Persistencia

Todos los datos quedan almacenados en MySQL utilizando SQLAlchemy ORM.

### Resultado

La API ya permite administrar clientes de forma completa mediante operaciones CRUD.

---

## Etapa de Seguridad y Buenas Prácticas

### Objetivo

Agregar mecanismos básicos de protección, monitoreo y robustez para preparar la API para un entorno real.

### Implementaciones

#### CORS

Se incorporó middleware CORS para controlar el acceso desde aplicaciones frontend.

Beneficios:

* Evita bloqueos del navegador.
* Permite integrar futuros dashboards web.
* Controla qué dominios pueden consumir la API.

#### Rate Limiting

Se implementó SlowAPI para limitar la cantidad de solicitudes permitidas por cliente.

Beneficios:

* Previene abuso de la API.
* Reduce riesgos de ataques automatizados.
* Protege recursos del servidor.

#### Logging

Se configuró registro automático de eventos.

Se almacenan:

* Inicio de la aplicación.
* Consultas realizadas.
* Creación de clientes.
* Actualizaciones.
* Eliminaciones.
* Errores y advertencias.

Beneficios:

* Auditoría.
* Diagnóstico de problemas.
* Monitoreo de actividad.

#### Manejo de Excepciones

Se implementó control de errores mediante:

* HTTPException.
* Captura de errores SQLAlchemy.
* Rollback automático de transacciones.

Beneficios:

* Mayor estabilidad.
* Evita corrupción de datos.
* Respuestas HTTP consistentes.

### Resultado

La API cuenta con medidas básicas de seguridad y observabilidad utilizadas en entornos profesionales.

---

# Próximas Etapas

## Etapa 3 - Gestión de Pagos

### Objetivo

Registrar y administrar los pagos realizados por los clientes.

### Implementaciones previstas

* Modelo Pago.
* CRUD de pagos.
* Relación Cliente → Pagos.
* Historial de pagos.
* Estados de cobranza.

---

## Etapa 4 - Automatización

### Objetivo

Automatizar tareas de cobranza.

### Implementaciones previstas

* APScheduler.
* Ejecución de tareas programadas.
* Detección de vencimientos.
* Generación automática de recordatorios.

---

## Etapa 5 - Integración WhatsApp

### Objetivo

Enviar recordatorios automáticos a los clientes.

### Implementaciones previstas

* Integración con API de WhatsApp.
* Plantillas de mensajes.
* Registro de envíos.
* Reintentos automáticos.

---

## Etapa 6 - Seguridad Avanzada

### Objetivo

Fortalecer la protección de la API.

### Implementaciones previstas

* Variables de entorno (.env).
* API Keys.
* JWT Authentication.
* Roles y permisos.

---

## Etapa 7 - Dashboard y Reportes

### Objetivo

Incorporar visualización y métricas.

### Implementaciones previstas

* Dashboard administrativo.
* Reportes de cobranza.
* Reportes de morosidad.
* Exportación de datos.
* Indicadores operativos.

---

# Características Técnicas Destacadas

* Arquitectura modular.
* FastAPI.
* SQLAlchemy ORM.
* MySQL.
* Validación con Pydantic.
* Middleware de seguridad.
* Rate Limiting.
* Logging y auditoría.
* Manejo robusto de excepciones.
* Documentación Swagger/OpenAPI.
* Base preparada para automatización y escalabilidad.

---

# Autor

Proyecto desarrollado como práctica profesional de Backend utilizando Python y FastAPI, aplicando conceptos de arquitectura, persistencia de datos, seguridad y automatización de procesos.
