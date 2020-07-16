# Config Lite
Implementación de configuraciones básicas de dispositivos de medición de energía y sus entidades básicas Clientes y Puntos de Medida

## Configuración de Entorno de Desarrollo
- Sistema operativo Windows 10 Enterprise
- Editor Visual Studio Code 1.47.1
- Lenguaje Python 3.7.6
- Postgres 12.3 sobre Docker 
- Librerías
  - Flask 1.1.2
  - Flask-SQLAlchemy 2.4.4
  - SQL Alchemy 1.3.18

## Implementación

### Servicio Rest para la Entidad Device ( Medidor )
La implementación incluye los siguientes métodos

*Creación de un nuevo medidor*
- **POST** /api/devices 

*Listado de medidores registrados*
- **GET** /api/devices 

*Consulta de un medidor por ID*
- **GET** /api/devices/{id} 

*Actualización de un medidor*
- **PUT** /api/devices/{id} 

*Borrado de un medidor por ID*
- **DELETE** /api/devices/{id}  


### Servicio Rest para la Entidad Client ( Cliente )
La implementación incluye los siguientes métodos

*Creación de un nuevo cliente*
- **POST** /api/clients 

*Listado de clientes registrados*
- **GET** /api/clients 

*Consulta de un cliente por ID*
- **GET** /api/clients/{id} 

*Actualización de un cliente*
- **PUT** /api/clients/{id} 

*Borrado de un cliente por ID*
- **DELETE** /api/clients/{id}  


### Servicio Rest para la Entidad Socket ( Punto de Medida )
La implementación incluye los siguientes métodos

*Creación de un nuevo socket*
- **POST** /api/sockets 

*Listado de sockets registrados*
- **GET** /api/sockets 

*Consulta de un socket por ID*
- **GET** /api/sockets/{id} 

*Actualización de un socket*
- **PUT** /api/sockets/{id} 

*Borrado de un socket por ID*
- **DELETE** /api/sockets/{id}  

