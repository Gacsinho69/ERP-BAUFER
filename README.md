# BAUFER ERP - Odoo 19.0

Sistema ERP personalizado para **BAUFER - Inversiones Séneca SpA.** basado en Odoo 19.0 Enterprise.

## 🚀 ¡LISTO PARA ODOO.SH!

Este repositorio está **100% configurado** para conectarse directamente con Odoo.sh.

### 📋 Instalación en 3 pasos:

1. **Ve a [Odoo.sh](https://www.odoo.sh)** e inicia sesión
2. **Crea proyecto nuevo** → Conecta este repo: `Gacsinho69/ERP-BAUFER`
3. **Espera el build** → Instala módulo `baufer_sale_report` desde Apps

¡Y listo! Tus cotizaciones tendrán el diseño minimalista automáticamente.

---

## 🎯 Módulos Personalizados

### 📊 baufer_sale_report (v19.0.2.0.0)
**Cotizaciones profesionales con diseño minimalista**

- ✅ Diseño minimalista profesional
- ✅ Colores GULF (Azul #003D7A, Naranja #FF6200)
- ✅ Campos de vehículo (Marca, Modelo, Patente, VIN)
- ✅ Tabla limpia sin bordes excesivos
- ✅ Total destacado en azul
- ✅ PDF optimizado para impresión

**Dependencias:** `sale_management`

---

### 🎯 baufer_crm (v19.0.1.0.0)
**CRM con calificación BANT**

- ✅ Sistema de scoring BANT automático
- ✅ Pipeline personalizado para B2B
- ✅ Automatizaciones de seguimiento
- ✅ Campos: Incoterm, Territorio, Discovery

**Dependencias:** `crm`, `sale_crm`, `baufer_sale_report`

---

## 📁 Estructura

```
addons/
├── baufer_sale_report/    # Cotizaciones minimalistas
└── baufer_crm/            # CRM personalizado
```

---

## 🎨 Preview

Abre `preview_cotizacion.html` en tu navegador para ver el diseño sin Odoo.

---

## 👥 BAUFER

**Inversiones Séneca SpA.**
RUT: 77.912.335-9
El Bosque Norte 200, Of. 701, Providencia
contacto@baufer.cl | www.baufer.cl