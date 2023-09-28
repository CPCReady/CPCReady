# Instalacion

La instación de **CPCReady** es muy sencialla, tan solo se necesitan ciertos requisitos para poder instalarlos.

## Requisitos

| Software | URL |Version |
| ------ | ------ | ------ |
| Python | [Descarga](https://www.python.org/downloads/) | 3. 6 o superior (Recomendada =>3.10)|
| Visual Studio Code |[Descarga](https://www.python.org/downloads/) | Latest|

Para ver como instalar Python en todos los sistemas ver [este link ](https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/instalar-python/)

Una vez instalado Python en tu sistema operativo, comprobaremos si tenemos la herramienta **pip** instalada. Esta herramienta nos permitira instalar CPCReady y mas modulos que algun dia podamos necesitar. 

Para ello abriremos un terminal (si no sabes como hacerlo accede a [este link ](https://www.ionos.es/ayuda/correo/solucion-de-problemas-correo-basiccorreo-profesional/abrir-la-linea-de-comandos-terminal/#:~:text=Abrir%20la%20l%C3%ADnea%20de%20comandos%20en%20Windows,entrada%20con%20la%20tecla%20Enter.) para verlo.

Y ejecutaremos

> **NOTA: 
Dependiendo de los sistemas operativos, el comando puede ser pip o pip3**
>
```bash
pip --version
```
Si nos devuelve la versión podremos continuar con la instalacion. Si no consulta [Instalar Pip en tu Sistema Operativo](https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/).

## Instalar CPCReady

Para instalar CPCReady en nuestra maquina, desde un terminal ejecutaremos:

```bash
pip install cpcready
```
Esto nos instalara la ultima version del software que este disponible en los repositorios. Podremos comprobar la version instalada ejecutando

```bash
CPCReady --version
```

## Upgrade CPCReady

Si ya tubieramos una version instalada de **CPCReady** y queremos instalar la ultima ejecutaremos:

```bash
pip install cpcready --upgrade
```

### Windows

Haga clic en Inicio > Todos los programas > Accesorios > Abrir Línea de comandos.

Alternativamente, también puede acceder a la línea de comandos seleccionando Inicio > Ejecutar introduciendo "cmd" y confirmando su entrada con la tecla Enter.


### Linux

Dependiendo de la interfaz de tu sistema operativo linux (por ejemplo, GNOME, KDE, Xfce), el terminal se llamará de forma diferente. Busca información en google de como abrir terminal en tu distribucion favorita de linux.

### Mac OSX

En Mac OS X, accede al terminal a través de la carpeta Aplicaciones >Utilidades.




[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
- ✨Magic ✨

```sh
cd dillinger
npm i
node app
```

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |