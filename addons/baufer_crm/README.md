# BAUFER - CRM Personalizado

Módulo que personaliza el CRM de Odoo según el blueprint de procesos BAUFER.

## Características

### Pipeline Personalizado
Estados según proceso BAUFER:
- Nuevo
- En Cadencia (Intento 1-7)
- Conectado
- Calificado (BANT)
- Cotización en Preparación
- Cotización Enviada
- Negociación
- Ganado / Perdido

### Score BANT
Sistema de calificación de leads basado en:
- **Budget** (Presupuesto): ¿Tiene presupuesto?
- **Authority** (Autoridad): ¿Es el decisor?
- **Need** (Necesidad): ¿Qué tan urgente?
- **Timeline** (Plazo): ¿Cuándo planea comprar?

### Automatizaciones
- Actividad automática de primer contacto (SLA 15 min)
- Asignación automática por territorio
- Creación automática de sale order al ganar
- Validaciones de datos mínimos

### Campos Adicionales
- Incoterm previsto
- Necesidad documentada
- Checklist de discovery
- Territorio comercial
- Origen del lead
- Fecha de primer contacto

## Requisitos

- Odoo 19.0 Enterprise
- Módulos: `crm`, `sale_crm`, `baufer_sale_report`

## Instalación

1. Asegurar que `baufer_sale_report` esté instalado primero
2. Instalar `baufer_crm`
3. Los stages se crearán automáticamente

## Uso

1. Los leads nuevos reciben automáticamente una actividad de primer contacto
2. Completar el Score BANT en el tab "Calificación BANT"
3. Documentar la necesidad y seleccionar incoterm
4. Seguir el pipeline hasta ganar la oportunidad
5. Al ganar, se crea automáticamente el sale order

## Autor

**BAUFER - Inversiones Séneca SpA.**

## Versión

1.0.0 - Compatible con Odoo 19.0

