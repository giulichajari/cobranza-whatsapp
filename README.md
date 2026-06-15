# Sistema de Cobranza WhatsApp

## Objetivo

Sistema para automatizar la gestión de clientes y el envío de recordatorios de pago mediante WhatsApp para servicios IPTV.
Sistema de Cobranza y Gestión de Clientes IPTV
Objetivo

Desarrollar una plataforma integral para la gestión de clientes y automatización de cobranzas en servicios IPTV.

El sistema está orientado a empresas que administran cientos de clientes activos y necesitan optimizar los procesos de seguimiento de pagos, notificaciones de vencimiento y control de cobranzas.

La solución permitirá centralizar la información de clientes, automatizar recordatorios de pago mediante WhatsApp, registrar estados de cobranza y generar reportes operativos para mejorar la eficiencia administrativa.

Problema a Resolver

Muchas empresas de IPTV gestionan sus clientes mediante planillas de cálculo y procesos manuales de seguimiento.

Esto genera problemas como:

Olvido de envíos de recordatorios.
Demoras en la cobranza.
Falta de seguimiento de clientes morosos.
Dificultad para escalar la operación a cientos de clientes.
Pérdida de tiempo en tareas administrativas repetitivas.

El sistema busca automatizar estos procesos para reducir tareas manuales y mejorar la tasa de cobranza.
## Tecnologías

- Python 3.13
- FastAPI
- UV
- SQLAlchemy
- SQLite (desarrollo)
- PostgreSQL (producción)
- JWT Authentication
- Pydantic
- APScheduler

## Arquitectura

Patrón MVC:


app/
├── controllers/
├── models/
├── services/
├── repositories/
├── routes/
├── middleware/
└── core/


## Características

- API REST
- Autenticación JWT
- Rutas protegidas
- Gestión de clientes
- Gestión de pagos
- Recordatorios automáticos
- Registro de envíos
- Documentación Swagger

## Estado del Proyecto

### Etapa 1
- [x] Inicialización con UV
- [x] FastAPI configurado
- [x] Endpoint /health

### Etapa 2
- [ ] Base de datos
- [ ] Modelo Cliente
- [ ] CRUD de clientes

### Etapa 3
- [ ] Scheduler
- [ ] Recordatorios automáticos

### Etapa 4
- [ ] Integración WhatsApp
- [ ] Dashboard