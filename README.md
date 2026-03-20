# Documentación:

# 🤖 Chat IA - Asistente Técnico

Sistema de chat interactivo funcional que conecta un frontend estático moderno con la API de Google Gemini a través de un backend robusto en FastAPI. Proporciona una interfaz intuitiva para conversaciones de IA con manejo completo de errores y configuración segura de credenciales.

---

## 📋 Tabla de Contenidos

1. [Descripción General](#descripción-general)
2. [Características Principales](#características-principales)
3. [Tecnologías Utilizadas](#tecnologías-utilizadas)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Requisitos Previos](#requisitos-previos)
6. [Instalación y Configuración](#instalación-y-configuración)
7. [Cómo Ejecutar el Proyecto](#cómo-ejecutar-el-proyecto)
8. [Descripción de Archivos](#descripción-de-archivos)
9. [Endpoints de la API](#endpoints-de-la-api)
10. [Configuración del Entorno](#configuración-del-entorno)
11. [Flujo de Funcionamiento](#flujo-de-funcionamiento)
12. [Manejo de Errores](#manejo-de-errores)
13. [Troubleshooting](#troubleshooting)
14. [Desarrollo y Contribuciones](#desarrollo-y-contribuciones)

---

## 📖 Descripción General

**Chat IA** es una aplicación web moderna que permite a los usuarios interactuar con el modelo de inteligencia artificial **Google Gemini** a través de una interfaz amigable. La aplicación actúa como un **asistente técnico experto en programación y desarrollo de software**, brindando respuestas contextuadas y de alta calidad.

El proyecto demuestra la integración completa de:
- Frontend moderno con JavaScript vanilla (sin dependencias externas de frameworks)
- Backend escalable y robusto con FastAPI
- Integración con APIs externas de Inteligencia Artificial
- Gestión segura de credenciales y variables de entorno

---

## ✨ Características Principales

- **🎨 Frontend Moderno y Responsivo**
  - Interfaz limpia y minimalista
  - Totalmente responsiva (funciona en móvil, tablet y desktop)
  - Animaciones suaves y transiciones visuales
  - Gradientes y estilos modernos

- **⚡ Backend FastAPI**
  - API rápida y eficiente basada en FastAPI
  - Documentación automática de API (Swagger)
  - Manejo robusto de excepciones
  - Validación de entrada

- **🤖 Integración con Google Gemini**
  - Utiliza el modelo `gemini-2.5-flash` de Google
  - Respuestas de alta calidad y contextuadas
  - API de Google genai para comunicación segura

- **🔐 Seguridad y Configuración**
  - Variables de entorno para gestión de credenciales
  - Validación de API keys
  - Manejo seguro de excepciones sin exponer detalles internos

- **📱 Experiencia de Usuario**
  - Indicador de carga mientras se procesa la respuesta
  - Auto-scroll para ver el último mensaje
  - Enter para enviar (Shift+Enter para nueva línea en el futuro)
  - Mensajes deshabilitados durante el procesamiento

---

## 🛠️ Tecnologías Utilizadas

| Componente | Tecnología | Versión |
|-----------|-----------|---------|
| **Backend** | Python 3.x | - |
| **Framework Web** | FastAPI | 0.135.1 |
| **Servidor Web** | Uvicorn | - |
| **IA** | Google Gemini API | 2.5-flash |
| **Cliente Google** | google-genai | 1.68.0 |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) | - |
| **Gestión de Entorno** | python-dotenv | - |

---

## 🏗️ Estructura del Proyecto

```
taller_repaso_parcial_practico_entornos/
├── main.py                      # Backend FastAPI principal
├── requirements.txt             # Dependencias Python
├── README.md                    # Este archivo (documentación)
├── .env.example                 # Plantilla de variables de entorno
├── .venv/                       # Entorno virtual de Python (no versionado)
├── __pycache__/                 # Cache de Python (no versionado)
└── static/                      # Archivos estáticos del frontend
    ├── index.html               # Página HTML principal
    ├── style.css                # Estilos CSS de la aplicación
    └── script.js                # Lógica JavaScript del cliente
```

---

## 📋 Requisitos Previos

Antes de instalar el proyecto, asegúrate de tener:

- **Python 3.8 o superior**
- **pip** (gestor de paquetes de Python)
- **Visual Studio Code** (opcional, para desarrollo)
- **Git** (para control de versiones)
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Conexión a Internet

### Verificar Requisitos

```bash
# Verificar versión de Python
python3 --version

# Verificar pip
pip3 --version
```

---

## 🚀 Instalación y Configuración

### Paso 1: Clonar o Descargar el Proyecto

```bash
# Si tienes el repositorio Git
git clone <URL_DEL_REPOSITORIO>
cd taller_repaso_parcial_practico_entornos

# O navega al directorio del proyecto
cd /home/danielagh98/entornosDeDesarrolloDeSoftware/taller_repaso_parcial_practico_entornos
```

### Paso 2: Crear un Entorno Virtual

```bash
# En Linux/Mac
python3 -m venv .venv
source .venv/bin/activate

# En Windows
python -m venv .venv
.venv\Scripts\activate
```

### Paso 3: Instalar Dependencias

```bash
# Actualizar pip (recomendado)
pip install --upgrade pip

# Instalar dependencias del proyecto
pip install -r requirements.txt
```

### Paso 4: Obtener API Key de Google Gemini

1. **Ir a Google AI Studio**: https://aistudio.google.com/apikey
2. **Crear una API Key**: Haz clic en "Create API Key"
3. **Copiar la clave**: Selecciona y copia tu API key

### Paso 5: Configurar Variables de Entorno

```bash
# Copiar el archivo de ejemplo
cp .env.example .env
```

Edita el archivo `.env` con tu editor favorito:

```bash
# Linux/Mac
nano .env
# o
vim .env

# Windows
notepad .env
```

Dentro del archivo `.env`, reemplaza el valor:

```env
GEMINI_API_KEY=tu_api_key_aqui
```

Por tu API key real:

```env
GEMINI_API_KEY=AIzaSyD...tu_clave_aqui...FeQ
```

⚠️ **Importante**: Nunca compartas tu API key. Añade `.env` a `.gitignore`.

---

## ▶️ Cómo Ejecutar el Proyecto

### Opción 1: Usando FastAPI CLI (Recomendado)

```bash
# Asegúrate de que el entorno virtual está activado
source .venv/bin/activate  # En Linux/Mac
# o
.venv\Scripts\activate     # En Windows

# Ejecutar la aplicación en modo desarrollo
fastapi dev main.py
```

La aplicación se iniciará en: **http://localhost:8000**

### Opción 2: Usando Uvicorn Directamente

```bash
# Activar entorno virtual
source .venv/bin/activate

# Ejecutar con Uvicorn
uvicorn main:app --reload

# Con opciones personalizadas
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Opción 3: Usando Python Directamente

```bash
python main.py
```

**Nota**: Esta opción requiere configuración adicional en el código.

### Acceder a la Aplicación

Una vez que el servidor esté ejecutándose:

1. **Interfaz de Chat**: http://localhost:8000
2. **Swagger API Docs**: http://localhost:8000/docs
3. **ReDoc (Documentación Alternativa)**: http://localhost:8000/redoc

---

## 📄 Descripción de Archivos

### `main.py` - Backend FastAPI

**Responsabilidad**: Servidor web y procesamiento de solicitudes

**Componentes principales**:

- **Importaciones**:
  - `FastAPI`: Framework web moderno
  - `StaticFiles`: Servir archivos estáticos (CSS, JavaScript)
  - `genai`: Cliente de Google Gemini
  - `dotenv`: Cargar variables de entorno

- **Variables Globales**:
  - `GEMINI_API_KEY`: Clave de API obtenida de variables de entorno

- **Instancia FastAPI**:
  ```python
  app = FastAPI(title="Chat IA - Asistente Simple")
  ```

- **Rutas**:
  - `GET /`: Sirve el archivo HTML principal
  - `GET /llm/{prompt}`: Procesa la solicitud de chat con Gemini
  - `/static`: Sirve archivos estáticos (CSS, JS)

**Funcionamiento**:
1. Recibe un prompt del usuario desde el frontend
2. Valida que la API key esté configurada
3. Envía el prompt al modelo Gemini
4. Devuelve la respuesta en formato JSON
5. Maneja errores y devuelve mensajes apropiados

---

### `static/index.html` - Frontend HTML

**Responsabilidad**: Estructura y contenido de la página web

**Estructura**:
- **Head**: Metadatos, estilos, configuración del navegador
- **Body**:
  - `.chat-header`: Encabezado con título y descripción
  - `.chat-messages`: Área de visualización de mensajes
  - `.chat-input-area`: Campo de entrada de usuario
  - `.loading-indicator`: Indicador de carga

**Elementos principales**:
- Input de texto (`#messageInput`): Donde el usuario escribe
- Botón de envío (`#sendButton`): Para enviar mensajes
- Contenedor de mensajes (`#chatMessages`): Área de chat
- Indicador de carga (`#loadingIndicator`): Muestra mientras se procesa

---

### `static/style.css` - Estilos CSS

**Responsabilidad**: Apariencia visual y diseño responsivo

**Características de Estilo**:

- **Color Scheme**:
  - Gradiente morado: De `#667eea` a `#764ba2`
  - Fondo claro: `#f8f9fa`
  - Texto: Colores apropiados para contraste

- **Componentes**:
  - `.container`: Contenedor principal (700px máx, 800px alto)
  - `.chat-header`: Encabezado con gradiente
  - `.chat-messages`: Área scrollable de mensajes
  - `.user-message`: Mensajes del usuario (derecha, azul)
  - `.bot-message`: Mensajes del bot (izquierda, blanco)
  - `.send-button`: Botón de envío
  - `.input-wrapper`: Contenedor de entrada

- **Animaciones**:
  - `slideIn`: Animación de entrada para nuevos mensajes
  - Transiciones suaves en botones
  - Shadow effects para profundidad

- **Responsividad**:
  - Media queries para móvil
  - Padding y max-width adaptativos
  - Flex layout para adaptarse a diferentes tamaños

---

### `static/script.js` - Lógica JavaScript

**Responsabilidad**: Interactividad del frontend y comunicación con el backend

**Funciones principales**:

1. **`handleSendMessage()`**:
   - Captura el mensaje del usuario
   - Valida que no esté vacío
   - Deshabilita inputs durante el procesamiento
   - Realiza fetch al endpoint `/llm/{prompt}`
   - Maneja errores
   - Re-habilita inputs

2. **`addMessageToChat(message, sender)`**:
   - Crea un elemento div para el mensaje
   - Asigna clases CSS según el remitente
   - Añade el contenido al DOM
   - Auto-scroll al último mensaje

**Event Listeners**:
- Click en botón: Enviar mensaje
- Keypress (Enter): Enviar mensaje
- Keypress (Shift+Enter): Nueva línea (preparado para el futuro)

**Flujo de Datos**:
```
Usuario escribe → Click/Enter → handleSendMessage() → 
fetch(/llm/{prompt}) → addMessageToChat() → Usuario ve respuesta
```

---

### `requirements.txt` - Dependencias Python

**Descripción**: Lista de todas las librerías Python necesarias

**Dependencias principales**:
- **fastapi**: Framework web
- **uvicorn**: Servidor ASGI
- **google-genai**: Cliente de Google Gemini
- **python-dotenv**: Gestión de variables de entorno
- **google-auth**: Autenticación a Google
- **httptools**: Soporte HTTP mejorado

**Para instalar**:
```bash
pip install -r requirements.txt
```

---

### `.env.example` - Plantilla de Configuración

**Descripción**: Archivo de ejemplo para variables de entorno

**Contenido**:
```env
GEMINI_API_KEY=tu_api_key_aqui
```

**Uso**:
1. Copiar a `.env`
2. Reemplazar valores
3. No compartir en repositorios públicos

---

## 🔌 Endpoints de la API

### 1. Endpoint Raíz

```http
GET /
```

**Descripción**: Sirve la página principal del chat

**Respuesta**:
- ✅ **200**: Devuelve `index.html`
- Tipo: `text/html`

**Ejemplo**:
```bash
curl http://localhost:8000/
```

---

### 2. Endpoint de Chat con IA

```http
GET /llm/{prompt}
```

**Descripción**: Procesa un mensaje y devuelve la respuesta de Gemini

**Parámetros**:
- `prompt` (string, requerido): Mensaje del usuario (en la URL, URL-encoded)

**Respuesta Exitosa (200)**:
```json
{
  "Respuesta": "Aquí está la respuesta del modelo Gemini..."
}
```

**Respuesta de Error - API Key No Configurada**:
```json
{
  "Respuesta": "❌ Error: GEMINI_API_KEY no configurada. Por favor, configura tu API key en el archivo .env"
}
```

**Respuesta de Error - Excepción**:
```json
{
  "Respuesta": "Error al procesar la solicitud: [detalle del error]. Por favor, intenta de nuevo más tarde."
}
```

**Ejemplos**:

```bash
# Pregunta simple
curl "http://localhost:8000/llm/Hola%20¿Cómo%20estás?"

# Pregunta técnica
curl "http://localhost:8000/llm/¿Cuál%20es%20la%20diferencia%20entre%20GET%20y%20POST?"

# Con espacios especiales (URL-encoded)
curl "http://localhost:8000/llm/Explícame%20qué%20es%20una%20API"
```

**Desde JavaScript**:
```javascript
fetch('/llm/¿Cuál es la capital de Francia?')
  .then(response => response.json())
  .then(data => console.log(data.Respuesta))
  .catch(error => console.error('Error:', error));
```

---

## ⚙️ Configuración del Entorno

### Variables de Entorno

El proyecto utiliza un archivo `.env` para gestionar configuraciones sensibles.

**Archivo `.env.example`**:
```env
GEMINI_API_KEY=tu_api_key_aqui
```

**Cómo Configurar**:

1. **Crear el archivo `.env`**:
   ```bash
   cp .env.example .env
   ```

2. **Editar `.env`**:
   ```env
   GEMINI_API_KEY=AIzaSyD_XXXXXXXXXX_XXXXXXXXXXXX
   ```

3. **Variables Cargadas Automáticamente**:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

**Seguridad**:
- ✅ Nunca compartir archivos `.env` en repositorios públicos
- ✅ Añadir `.env` a `.gitignore`
- ✅ Usar `.env.example` como plantilla solo
- ✅ Variables de entorno del sistema en producción

**Cómo Obtener la API Key**:

1. Ir a: https://aistudio.google.com/apikey
2. Hacer clic en **"Create API Key"**
3. Seleccionar o crear proyecto
4. Copiar la clave generada
5. Pegarla en `.env`

---

## 🔄 Flujo de Funcionamiento

### Diagrama de Flujo General

```
┌─────────────────────────────┐
│   Usuario escribe mensaje   │
│   en el frontend            │
└──────────────┬──────────────┘
               │
               ▼
        ┌─────────────┐
        │ JavaScript  │
        │ addEvent    │
        │ Listener    │
        └──────┬──────┘
               │
               ▼
        ┌──────────────────┐
        │ Validar mensaje  │
        │ no esté vacío    │
        └──────┬───────────┘
               │
               ▼
    ┌──────────────────────┐
    │ Deshabilitar inputs  │
    │ Mostrar spinner      │
    └──────┬───────────────┘
           │
           ▼
   ┌─────────────────────┐
   │ Fetch a /llm/{msg}  │
   │ (URL-encoded)       │
   └──────┬──────────────┘
          │
          ▼
   ┌──────────────────────┐
   │ FastAPI recibe       │
   │ solicitud GET        │
   └──────┬───────────────┘
          │
          ▼
   ┌──────────────────────────┐
   │ Validar GEMINI_API_KEY   │
   │ configurada              │
   └──────┬───────────────────┘
          │
          ▼
   ┌──────────────────────────┐
   │ Crear cliente Gemini     │
   │ con API key              │
   └──────┬───────────────────┘
          │
          ▼
   ┌──────────────────────────┐
   │ Enviar prompt a Gemini   │
   │ (modelo 2.5-flash)       │
   └──────┬───────────────────┘
          │
          ▼ (con respuesta)
   ┌──────────────────────────┐
   │ Extraer texto respuesta   │
   │ o mensaje de error       │
   └──────┬───────────────────┘
          │
          ▼
   ┌──────────────────────────┐
   │ Retornar JSON:           │
   │ {"Respuesta": "..."}     │
   └──────┬───────────────────┘
          │
          ▼
   ┌──────────────────────────┐
   │ JavaScript procesa JSON  │
   │ Extrae respuesta         │
   └──────┬───────────────────┘
          │
          ▼
   ┌──────────────────────────┐
   │ addMessageToChat()       │
   │ Mostrar respuesta bot    │
   └──────┬───────────────────┘
          │
          ▼
   ┌──────────────────────────┐
   │ Habilitar inputs         │
   │ Ocultar spinner          │
   │ Scroll al último mensaje │
   └──────────────────────────┘
```

### Paso a Paso Detallado

**1. Frontend**:
   - Usuario escribe: "¿Qué es Python?"
   - Presiona Enter o click en Enviar
   - `handleSendMessage()` se ejecuta

**2. Validación**:
   - Verifique que el mensaje no esté vacío
   - Mostrar el mensaje del usuario en el chat
   - Deshabilitar input/botón

**3. Solicitud HTTP**:
   - Construir URL: `/llm/¿Qué es Python?`
   - Codificar especiales: `/llm/%C2%BFQu%C3%A9%20es%20Python%3F`
   - Realizar `fetch()` GET

**4. Backend - Recepción**:
   - FastAPI recibe en endpoint `@app.get("/llm/{prompt}")`
   - Decodificar parámetro URL
   - Validar API key

**5. Backend - Procesamiento**:
   - Crear cliente Gemini con API key
   - Enviar prompt al modelo `gemini-2.5-flash`
   - Esperar respuesta

**6. Backend - Respuesta**:
   - Extraer texto de respuesta
   - Crear JSON: `{"Respuesta": "Python es un lenguaje..."}`
   - Devolver 200 OK

**7. Frontend - Procesamiento**:
   - Recibir JSON
   - Obtener `data.Respuesta`
   - Llamar `addMessageToChat(respuesta, 'bot')`

**8. Frontend - Mostrar**:
   - Crear div con clase `bot-message`
   - Añadir párrafo con texto
   - Añadir al DOM
   - Auto-scroll
   - Habilitar inputs nuevamente

---

## ⚠️ Manejo de Errores

### Errores Posibles y Soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| API Key no configurada | `.env` no existe o no tiene GEMINI_API_KEY | Crear `.env` con API key válida |
| API Key inválida | Clave expirada o incorrecta | Obtener nueva clave en Google AI Studio |
| Error de conexión | Sin conexión a Internet | Verificar conexión de red |
| Puerto 8000 en uso | Otra aplicación usando puerto | Cambiar puerto: `fastapi dev main.py --port 8001` |
| ModuleNotFoundError | Dependencias no instaladas | Ejecutar `pip install -r requirements.txt` |
| Entorno virtual no activado | Python no encuentra paquetes | Activar entorno: `source .venv/bin/activate` |

### Manejo en Código

**Backend**:
```python
try:
    # Validar API key
    if not GEMINI_API_KEY:
        return {"Respuesta": "❌ Error: GEMINI_API_KEY no configurada..."}
    
    # Crear cliente y enviar solicitud
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(...)
    
except Exception as e:
    # Capturar cualquier error
    error_message = f"Error al procesar la solicitud: {str(e)}..."
    return {"Respuesta": error_message}
```

**Frontend**:
```javascript
try {
    const response = await fetch(`/llm/${encodeURIComponent(userMessage)}`);
    
    if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`);
    }
    
    const data = await response.json();
    addMessageToChat(data.Respuesta, 'bot');
    
} catch (error) {
    console.error('Error:', error);
    addMessageToChat('❌ Error: No pude procesar tu solicitud...', 'bot');
}
```

---

## 🔧 Troubleshooting

### Problema: El servidor no inicia

**Síntomas**:
- Error al ejecutar `fastapi dev main.py`
- `Command not found: fastapi`

**Soluciones**:
```bash
# 1. Verificar que el entorno virtual está activado
source .venv/bin/activate

# 2. Reinstalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# 3. Usar uvicorn directamente
uvicorn main:app --reload
```

---

### Problema: Error "API Key no configurada"

**Síntomas**:
- Respuesta: "❌ Error: GEMINI_API_KEY no configurada"

**Soluciones**:
```bash
# 1. Verificar que .env existe
cat .env

# 2. Verificar que tiene GEMINI_API_KEY
grep GEMINI_API_KEY .env

# 3. Obtener nueva API key en:
# https://aistudio.google.com/apikey

# 4. Reiniciar el servidor después de cambiar .env
# Ctrl+C en la terminal
# fastapi dev main.py
```

---

### Problema: Puerto 8000 en uso

**Síntomas**:
- Error: `Address already in use`

**Soluciones**:
```bash
# 1. Encontrar proceso usando puerto 8000
lsof -i :8000

# 2. Matar proceso (reemplazar PID)
kill -9 <PID>

# 3. O usar otro puerto
fastapi dev main.py --port 8001
```

---

### Problema: El frontend no carga

**Síntomas**:
- Página en blanco en http://localhost:8000
- Error 404

**Soluciones**:
```bash
# 1. Verificar que static/index.html existe
ls -la static/index.html

# 2. Verificar permisos
chmod 644 static/index.html

# 3. Revisar logs del servidor para más detalles
```

---

### Problema: Mensajes vacíos del bot

**Síntomas**:
- El bot responde pero sin texto

**Soluciones**:
1. Verificar que `response.text` no es None
2. Comprobar límites de uso de API de Gemini
3. Revisar que el modelo `gemini-2.5-flash` está disponible
4. Verificar logs de error en consola

---

## 👨‍💻 Desarrollo y Contribuciones

### Estructura para Desarrollo

```bash
# Clonar proyecto
git clone <URL>
cd taller_repaso_parcial_practico_entornos

# Crear rama de desarrollo
git checkout -b feature/nueva-caracteristica

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar en modo desarrollo
fastapi dev main.py
```

### Mejoras Futuras Sugeridas

- [ ] **Historial de Conversaciones**: Guardar chats en base de datos
- [ ] **Roles de Usuario**: Diferentes tipos de asistentes (técnico, general, etc.)
- [ ] **Themes**: Modo oscuro/claro configurable
- [ ] **Exportar Chat**: Descargar conversaciones como PDF/TXT
- [ ] **Autenticación**: Sistema de usuarios con login
- [ ] **Rate Limiting**: Limitar solicitudes por usuario
- [ ] **WebSocket**: Chat bidireccional en tiempo real
- [ ] **Modelos Alternativos**: Soporte para múltiples LLMs
- [ ] **Búsqueda Web**: Información actualizada en respuestas
- [ ] **Tests Unitarios**: Cobertura de pruebas

### Como Contribuir

1. **Fork** del repositorio
2. **Crear rama**: `git checkout -b feature/nueva-func`
3. **Hacer cambios** y **commit**: `git commit -m "Descripción"`
4. **Push**: `git push origin feature/nueva-func`
5. **Pull Request**: Describir cambios claramente

### Estándares de Código

- **Python**: Seguir PEP 8
- **JavaScript**: Usar camelCase para funciones
- **CSS**: Usar BEM o similar para clases
- **Commits**: Mensajes descriptivos en presente

---

## 📚 Referencias y Recursos

- **FastAPI**: https://fastapi.tiangolo.com
- **Google Gemini API**: https://ai.google.dev
- **Uvicorn**: https://www.uvicorn.org
- **Python dotenv**: https://github.com/theskumar/python-dotenv
- **MDN Web Docs**: https://developer.mozilla.org

---

## 📝 Notas Adicionales

### Información Técnica

- **Modelo IA**: Google Gemini 2.5-flash (modelo ligero y rápido)
- **Base de Datos**: Sin base de datos (aplicación sin estado)
- **Autenticación**: Solo API key de Google
- **Escalabilidad**: Preparado para agregar caché/BD

### Información de Contacto

Para preguntas o sugerencias sobre el proyecto, consulta la documentación de FastAPI y Google Gemini.

---

## 📄 Licencia

Este proyecto es de uso educativo para el taller "Repaso Parcial Práctico de Entornos de Desarrollo".

---

**Última actualización**: 19 de marzo de 2026

# Instalar dependencias
pip install -r requirements.txt
```

### 3. Ejecutar el Servidor

```bash
# Opción 1: Con uvicorn directamente
uvicorn main:app --reload

# Opción 2: Con el módulo python
python -m uvicorn main:app --reload
```

El servidor estará disponible en: **http://localhost:8000**

## 📡 Endpoints API

### GET `/`
Sirve la interfaz del chat (index.html)

**Respuesta**: Archivo HTML

---

### GET `/llm/{prompt}`
Procesa el mensaje del usuario y devuelve la respuesta de Gemini

**Parámetro**:
- `prompt` (string): Mensaje del usuario (se envía codificado en la URL)

**Ejemplo de Solicitud**:
```javascript
fetch('/llm/¿Cómo se usa async await en JavaScript?')
  .then(res => res.json())
  .then(data => console.log(data))
```

**Respuesta JSON**:
```json
{
  "Respuesta": "Async/await es una forma moderna y legible de manejar promesas en JavaScript..."
}
```

## 🎨 Frontend - Funcionalidades

### HTML (static/index.html)
- Contenedor responsivo para el chat
- Histórico de mensajes con scroll automático
- Campo de entrada con botón de envío
- Indicador de carga visual

### CSS (static/style.css)
- Diseño gradiente moderno (azul-púrpura)
- Diferenciación visual clara entre mensajes del usuario y la IA
- Animaciones suave (slideIn, pulse)
- Totalmente responsivo para móbiles
- Scrollbar personalizado

### JavaScript (static/script.js)
- Captura de texto del input
- Envío de mensajes con Enter o clic en botón
- Peticiones asincrónicas con fetch
- Validación de entrada
- Manejo de errores
- Autocompletado y enfoque del input

## 💻 Backend - Características Clave

### FastAPI (main.py)
- **Servicio de archivos estáticos**: Sirve HTML, CSS y JS desde `/static`
- **Endpoint raíz**: Devuelve la interfaz del chat
- **Endpoint LLM**: Procesa prompts con Gemini
- **System Prompt**: Configuración profesional de la IA
- **Gestión de errores**: Try-catch con mensajes informativos
- **Variables de entorno**: Configuración segura de credenciales

### Configuración de Gemini
```python
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Eres un asistente técnico experto en programación..."
)
```

**System Prompt**: La IA está configurada para:
- Actuar como experto en programación
- Proporcionar respuestas precisas y profesionales
- Usar ejemplos de código cuando sea apropiado
- Indicar claramente cuando no está segura

## 🔐 Seguridad

- ✅ API key almacenada en variables de entorno (NO en código)
- ✅ `.env` no debe incluirse en control de versiones
- ✅ Manejo seguro de excepciones sin exponer detalles internos
- ✅ Validación de entrada en el frontend y backend

## 📦 Dependencias Principales

- `fastapi`: Framework web moderno
- `uvicorn`: Servidor ASGI
- `google-genai`: Librería oficial para Gemini
- `python-dotenv`: Gestión de variables de entorno

## 🛠️ Desarrollo

### Activa el modo recarga automática
```bash
uvicorn main:app --reload
```

El servidor reiniciará automáticamente con cada cambio en `main.py`

### Ejecuta en un puerto diferente
```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

## ❓ Solución de Problemas

### Error: "GOOGLE_API_KEY no configurada"
- Crea el archivo `.env` con tu API key
- Asegúrate de que `python-dotenv` esté instalado

### Error: "404 Not Found" en archivos estáticos
- Verifica que la carpeta `static/` exista con los archivos HTML, CSS y JS
- Revisa que los paths sean correctos en las importaciones

### Error: "ImportError: No module named 'google'"
```bash
pip install google-genai
```

### Slow response from Gemini
- El primer request puede tardar más (inicio en frío)
- Verifica tu conexión a internet
- Considera usar `gemini-1.5-flash` en lugar de `gemini-pro` para respuestas más rápidas

## 📖 Ejemplos de Uso

### Desde el navegador
1. Abre `http://localhost:8000`
2. Escribe tu pregunta: "¿Cómo crear un endpoint en FastAPI?"
3. Presiona Enter o haz clic en "Enviar"
4. Espera la respuesta de la IA

### Desde cURL
```bash
curl "http://localhost:8000/llm/Explica%20el%20patrón%20MVC"
```

## 📝 Licencia

Este proyecto está disponible bajo licencia MIT.

## 👨‍💻 Autor

Desarrollado como sistema de chat IA para asistencia técnica en programación.
