# Introduccion a la Logica de Programacion y Algoritmos con Python

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## Descripcion

Bootcamp intensivo de Python disenado para estudiantes sin experiencia previa en programacion. Este programa forma parte del **Programa StudIA de la Alcaldia de Medellin**, enfocado en desarrollar habilidades fundamentales en logica de programacion, algoritmos y desarrollo web con Python.

## Instructor

**Miguel Angel Carrillo**
- GitHub: [@miguelcmo](https://github.com/miguelcmo)
- Ingeniero Electronico
- Especialista en Desarrollo de Software

## Objetivos del Bootcamp

- Comprender los fundamentos de la programacion y la logica computacional
- Dominar la sintaxis y estructuras de datos de Python
- Aplicar principios de Programacion Orientada a Objetos (POO)
- Desarrollar aplicaciones web funcionales con Flask
- Implementar proyectos completos desde el diseno hasta el deployment

## Estructura del Programa

### Informacion General
- **Duracion total:** 60 horas
- **Modalidad:** Hibrida (Virtual + Presencial)
  - 8 sesiones virtuales (32 horas) - Teoria y conceptos
  - 6 sesiones presenciales (24 horas) - Desarrollo de proyectos
  - 1 sesion final (4 horas) - Presentaciones y Demo Day

## Contenido del Repositorio

```
pythonBootcamp/
│
├── S01_variablesAndDataTypes/
│   ├── 01variables.py              # Variables y nomenclatura
│   ├── 02keywords.py               # Palabras reservadas de Python
│   ├── 03booleanValuesAndLogicOperators.py  # Operadores logicos
│   ├── 04functions.py              # Funciones basicas
│   └── 05userInput.py              # Entrada de usuario
│
├── S02_controlStructures/
│   ├── 01ifConditional.py          # Estructuras condicionales
│   ├── 02forLoop.py                # Bucle for
│   ├── 03rangeAndWhile.py          # Range y bucle while
│   └── x[1-5]codeChallenge.py      # Desafios de codigo
│
├── S03_listsAndDictionaries/
│   ├── 01lists.py                  # Listas y metodos
│   ├── 02dictionaries.py           # Diccionarios
│   └── x[1-5]codeChallenge.py      # Desafios de codigo
│
└── bootcamp_python_programa_completo.md  # Programa detallado
```

## Programa por Fases

### Fase 1: Fundamentos de Python (Sesiones 1-4)

**Sesion 1 - Virtual: Introduccion a Python y Primeros Pasos**
- Variables y tipos de datos
- Strings y manipulacion
- Input del usuario

**Sesion 2 - Virtual: Estructuras de Control**
- Condicionales (if, elif, else)
- Bucles (for, while)
- Listas basicas

**Sesion 3 - Virtual: Estructuras de Datos**
- Diccionarios
- Tuplas
- Sets
- Estructuras anidadas

**Sesion 4 - Virtual: Funciones y Modularizacion**
- Definicion de funciones
- Parametros y argumentos
- Modulos y paquetes
- Lambda y funciones de orden superior

### Fase 2: Programacion Orientada a Objetos (Sesiones 5-6)

**Sesion 5 - Virtual: Introduccion a POO**
- Clases y objetos
- Atributos y metodos
- Constructor `__init__`

**Sesion 6 - Virtual: POO Avanzada**
- Herencia
- Encapsulamiento
- Polimorfismo
- Metodos especiales

### Fase 3: Desarrollo de Proyecto (Sesiones 7-9)

**Sesion 7 - Presencial: Inicio del Proyecto**
- Definicion y planificacion
- Setup del entorno
- Modelo de datos

**Sesion 8 - Virtual: Archivos, Excepciones y Testing**
- Manejo de archivos (JSON, CSV)
- Try-except
- Testing con pytest

**Sesion 9 - Presencial: Desarrollo del Backend**
- Logica de negocio
- Persistencia de datos
- CRUD completo

### Fase 4: Desarrollo Web (Sesiones 10-16)

**Sesion 10 - Virtual: Introduccion a Flask**
- Fundamentos web
- HTML y CSS basicos
- Routing y templates

**Sesion 11 - Virtual: Flask Intermedio**
- Formularios
- Sesiones
- Integracion con backend

**Sesion 12 - Virtual: Base de Datos**
- SQL basico
- SQLAlchemy ORM
- Migraciones

**Sesion 13 - Presencial: Desarrollo del Frontend**
- Interfaces de usuario
- Templates con Jinja2
- Estilizado con Bootstrap

**Sesion 14 - Presencial: Integracion**
- Conectar todos los componentes
- Funcionalidades avanzadas
- Testing integral

**Sesion 15 - Presencial: Deployment**
- Pulido final
- Documentacion
- Deployment en produccion

**Sesion 16 - Presencial: Demo Day**
- Presentaciones finales
- Feedback y cierre
- Entrega de certificados

## Empezando

### Requisitos Previos

- **Python 3.11+** ([Descargar aqui](https://www.python.org/downloads/))
- **VS Code** ([Descargar aqui](https://code.visualstudio.com/)) o PyCharm
- **Git** ([Descargar aqui](https://git-scm.com/))
- Navegador web moderno (Chrome, Firefox)

### Instalacion

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/miguelcmo/pythonBootcamp.git
   cd pythonBootcamp
   ```

2. **Crear entorno virtual:**
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias (para fases avanzadas):**
   ```bash
   pip install flask flask-sqlalchemy flask-wtf flask-migrate pytest python-dotenv
   ```

### Ejecutar los Ejemplos

```bash
# Navegar a la carpeta de la sesion
cd S01_variablesAndDataTypes

# Ejecutar un archivo Python
python 01variables.py
```

## Ejemplos de Uso

### Variables y Tipos de Datos
```python
# Declaracion de variables
nombre = "Miguel"
edad = 25
altura = 1.80
es_estudiante = True

# Imprimir variables
print(f"Hola, soy {nombre} y tengo {edad} anos")
```

### Listas
```python
# Crear y manipular listas
frutas = ['manzana', 'banana', 'cereza']
frutas.append('datil')
print(frutas)  # ['manzana', 'banana', 'cereza', 'datil']

# List comprehension
cuadrados = [x * x for x in range(6)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25]
```

### Diccionarios
```python
# Crear diccionario
estudiante = {
    'nombre': 'Ana',
    'edad': 22,
    'carrera': 'Ingenieria'
}

# Acceder a valores
print(estudiante['nombre'])  # Ana
```

### Funciones
```python
# Definir funcion
def saludar(nombre):
    return f"Hola, {nombre}!"

# Llamar funcion
mensaje = saludar("Miguel")
print(mensaje)  # Hola, Miguel!
```

### Clases (POO)
```python
# Definir clase
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre} y tengo {self.edad} anos"

# Crear objeto
estudiante = Estudiante("Ana", 22)
print(estudiante.presentarse())
```

## Desafios de Codigo

Cada sesion incluye desafios practicos para reforzar el aprendizaje. Los archivos de desafios estan marcados con `x[N]codeChallenge.py`.

### Ejemplo de Desafio
```python
# Desafio: Crear una funcion que calcule el factorial de un numero
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

## Proyectos Finales

Los estudiantes trabajaran en equipos para desarrollar uno de los siguientes proyectos:

### 1. Sistema de Gestion de Biblioteca
- CRUD de libros y usuarios
- Sistema de prestamos
- Dashboard con estadisticas

### 2. Aplicacion de Gestion de Tareas
- Tableros estilo Kanban
- Categorias y prioridades
- Multiples usuarios

### 3. Sistema de Reservas
- Calendario de disponibilidad
- Gestion de recursos
- Panel de administracion

### 4. Tienda Online Simple
- Catalogo de productos
- Carrito de compras
- Sistema de ordenes

### 5. Blog Personal
- CRUD de posts
- Sistema de comentarios
- Categorias y tags

## Tecnologias y Herramientas

- **Lenguaje:** Python 3.11+
- **Framework Web:** Flask
- **ORM:** SQLAlchemy
- **Testing:** pytest
- **Frontend:** HTML5, CSS3, Bootstrap
- **Control de Versiones:** Git & GitHub
- **Editor:** VS Code / PyCharm

## Recursos Adicionales

### Documentacion Oficial
- [Python Documentation](https://docs.python.org)
- [Flask Documentation](https://flask.palletsprojects.com)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org)

### Tutoriales Recomendados
- [Real Python](https://realpython.com) - Tutoriales y articulos
- [W3Schools Python](https://www.w3schools.com/python/) - Referencia rapida
- [Bootstrap Documentation](https://getbootstrap.com) - Framework CSS

### Libros
- "Python Crash Course" - Eric Matthes
- "Flask Web Development" - Miguel Grinberg
- "Automate the Boring Stuff with Python" - Al Sweigart

## Contribuir

Las contribuciones son bienvenidas. Si encuentras algun error o tienes sugerencias:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Contacto

**Miguel Angel Carrillo**
- GitHub: [@miguelcmo](https://github.com/miguelcmo)
- Proyecto: [Python Bootcamp](https://github.com/miguelcmo/pythonBootcamp)

## Licencia

Este proyecto esta bajo la Licencia MIT - ver el archivo LICENSE para mas detalles.

## Agradecimientos

- **Programa StudIA - Alcaldia de Medellin** por el apoyo y la oportunidad de formar nuevos desarrolladores
- Todos los estudiantes que participan activamente en el bootcamp
- La comunidad de Python por sus excelentes recursos educativos

---

**Dale una estrella a este repositorio si te resulta util!**

**Listo para comenzar tu viaje en Python?** Empieza con [S01_variablesAndDataTypes/01variables.py](S01_variablesAndDataTypes/01variables.py)
