# BAUFER - Reportes de Venta Personalizados

Módulo personalizado para Odoo 19.0 que adapta las cotizaciones y reportes de venta al diseño corporativo de BAUFER con estilo SAP.

## Características

### 🎨 Diseño Profesional
- Logo corporativo BAUFER
- Colores institucionales (azul #003D7A y naranja #FF6200 inspirados en GULF)
- Diseño limpio y estructurado estilo SAP
- Tipografía profesional

### 🚗 Campos de Vehículos
Agrega información detallada del vehículo en las cotizaciones:
- Marca
- Modelo
- Patente
- VIN (Vehicle Identification Number)

### 👤 Información de Contacto Mejorada
- Sucursal del cliente
- Nombre del contacto
- Email del contacto (con validación)
- Teléfono del contacto

### 📋 Tabla de Productos Mejorada
- Columna de código de producto
- Columna de origen (SAIC, Europa, Asia, Nacional, EEUU, Otro)
- Descuentos visibles
- Formato de precios en pesos chilenos

### 📄 Reporte PDF Personalizado
- Header con información de empresa
- Datos del cliente organizados
- Información del vehículo destacada
- Tabla de productos con todos los detalles
- Sección de totales clara con descuentos

## Requisitos

- Odoo 19.0 Enterprise
- Módulo `sale_management` instalado

## Instalación

1. El módulo se despliega automáticamente al hacer push al repositorio
2. Actualizar la lista de módulos en Odoo
3. Buscar "BAUFER - Reportes de Venta Personalizados"
4. Hacer click en "Instalar"

## Uso

### Crear una cotización con información de vehículo

1. Ir a **Ventas** → **Pedidos** → **Cotizaciones**
2. Crear nuevo
3. Seleccionar cliente
4. Completar los campos de **🚌 Información del Vehículo**
5. Completar **👤 Información de Contacto** si es necesario
6. Agregar líneas de pedido
7. Seleccionar origen para cada producto

### Generar PDF personalizado

1. Desde la cotización, click en **Imprimir** → **Cotización**
2. Se generará un PDF con el diseño BAUFER

## Autor

**BAUFER - Inversiones Séneca SpA.**
- RUT: 77.912.335-9
- Email: contacto@baufer.cl
- Dirección: El Bosque Norte 200, Oficina 701, Providencia, Chile

## Licencia

LGPL-3

## Versión

1.0.0 - Compatible con Odoo 19.0

