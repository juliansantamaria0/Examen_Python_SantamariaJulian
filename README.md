# examen python



------

# Autor



Julian Andres Santamaria Bustamante

------

# Tabla de Contenidos



------

- Características Principales
- Estructura del Proyecto
- Flujo de Ejecución

------

## Características Principales

- **Gestion de ingredientes** 
- **Guardar historial de ingredientes** 
- **Ver historial de ingredientes** 
- **Gestion por categorias**
- **Gestion por hamburguesas**  
- **Gestion de los chef** 

------

## Estructura del Proyecto



```
examen_python
├── data/
│   └── json
├── contrllers/            
│   └── controladores del programa
├── models/                   
│   └── elementos.py
├── ui/
│   └── menu.py   
├── utils/
│   ├── file_handler(1,2,3,4).py             
│   └── helpers.py             
└── main.py          
```



------

## Flujo de Ejecución



El flujo de la aplicación sigue una arquitectura modular y centralizada. ┌───────────────────┐ │ Usuario │ └───────┬───────────┘ │ ▼ ┌───────────────────┐ │ main.py   Bucle principal del programa └───────┬───────────┘ │ ▼ ┌───────────────────┐ │ utils/menu.py │ ← Muestra menú y recibe la opción del usuario └───────┬───────────┘ │ ▼ ┌───────────────────────────────┐ │ controllers/*.py │ ← Ejecuta la lógica de negocio según la opción└───────┬───────────────────────┘ │ ▼┌───────────────────┐│ utils/file_handler(1,2,3,4) │ ← Carga o guarda datos en los archivos JSON└───────┬───────────┘ │ ▼┌───────────────────┐│ data/*.json │ ← Almacenamiento persistente de la información└───────────────────┘

------

## ejemplo

​                MENU PRINCIPAL                           

​    1. gestion de ingredientes                                     

2. guardar historial de ingredientes                          

3. ver historial de ingredientes                           

4. gestion por categorias                                    

5. gestion de las hamburguesas                              

6. gestion de los chef                               

7. salir                                                                                                                                                                                                                                                                         

nombre del ingrediente: 1
descripcion del ingrediente: 1
stock del ingrediente: 1
precio del ingrediente: 1
el elemento ha sido añadido a la coleccion
ingredientes guardada correctamente.

Presiona Enter para continuar...