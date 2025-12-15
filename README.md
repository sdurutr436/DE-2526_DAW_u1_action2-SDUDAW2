# Documentación Automática con GitHub Actions

## a) Herramienta de generación de documentación

Utilicé Doxygen integrado en el workflow de GitHub Actions ubicado en `.github/workflows/doxygen.yml`. El workflow se ejecuta automáticamente en cada push a main y genera la documentación HTML en el directorio `doc/html`.

## b) Documentación de componentes

El código actual no tiene documentación estructurada. Doxygen procesa el código Python sin docstrings y genera documentación básica a partir de las firmas de función. El archivo `main.py` contiene:

```python
def saludo(nombre: str):
    return f"Hola, {nombre}!"
```

Esta función ha sido procesada por Doxygen y aparece en `doc/html/main_8py.html`, aunque sin comentarios estructurados. No he utilizado un estilo de documentación específico porque el código carece de docstrings.

## c) Multiformato

He configurado Doxygen para generar documentación en formato LaTeX además de HTML. La configuración en `doc/Doxyfile` especifica `GENERATE_LATEX = YES`. Sin embargo, el workflow actual en `.github/workflows/doxygen.yml` solo hace commit del directorio `doc/html`, por lo que la documentación LaTeX se genera pero no se persiste en el repositorio. El comando `doxygen doc/Doxyfile` genera ambos formatos localmente.

## d) Colaboración

GitHub facilita el mantenimiento de la documentación mediante varios mecanismos. Cuando varias personas colaboran, se utilizan Pull Requests que permiten revisar cambios antes de integrarlos. Las GitHub Actions ejecutan checks de CI que validan la generación correcta de documentación. La protección de ramas en main impide pushes directos, obligando a pasar por el proceso de revisión. Los reviews permiten que otros desarrolladores aprueben o soliciten cambios en la documentación antes de su publicación.

## e) Control de versiones

Mensajes de commit del proyecto:

```workflows automáticos que regeneran la documentación en cada push. Cuando colaboran varias personas, se pueden usar Pull Requests para revisar cambios antes de integrarlos. Las GitHub Actions ejecutan checks de CI que validan la generación correcta de documentación. La protección de ramas en main puede configurarse para impedir pushes directos y requerir revisiones mediante PR. Los code reviews permiten que otros desarrolladores aprueben o soliciten cambios en código y
d2fcc59 Update Doxygen documentation
0bf1897 Update README con estado de tests
d44b259 Añadido cambio a yaml para que pueda añadir los cambios a main en lugar de github publish
78a1cad Update README con estado de tests
ecb5724 Cambiado doxygen para representar mejor los cambios
```

Son claros y descriptivos porque especifican exactamente qué se modificó. "Update Doxygen documentation" indica actualización de documentación, "Añadido cambio a yaml" especifica el archivo modificado y su propósito, y "Cambiado doxygen para representar mejor los cambios" explica la mejora realizada.

## f) Accesibilidad y seguridad

Las medidas de seguridad disponibles en GitHub incluyen:

1. Control de visibilidad del repositorio mediante configuración privada o pública
2. Gestión de permisos mediante roles de GitHub que controlan quién puede escribir, leer o administrar
3. Protección de ramas que puede configurarse para requerir revisiones antes de merge
4. Uso del token automático `secrets.GITHUB_TOKEN` en workflows para operaciones de git sin exponer credenciales
5. Configuración de permisos específicos en workflows con `permissions: contents: write` que limita las capacidades del workflow solo a escritura de contenido

## g) Instalación y uso documentados

El funcionamiento del workflow de documentación se encuentra en `.github/workflows/doxygen.yml`. Este workflow ejecuta los siguientes comandos:

- `sudo apt-get install -y doxygen graphviz` para instalar las herramientas necesarias
- `doxygen doc/Doxyfile` para generar la documentación

La configuración de Doxygen está en `doc/Doxyfile`, que especifica generar documentación en formato HTML (persistida en el repositorio bajo `doc/html`) y LaTeX (generada pero no commitada). La herramienta procesa archivos Python y genera documentación navegable.

## h) Integración continua
procesos de verificación y generación de artefactos en cada cambio del código fuente. El workflow de documentación se dispara automáticamente con el evento `push` a las ramas main y master:

```yaml
on:
  push:
    branches:
      - main
      - master
```

El workflow ejecuta cuatro pasos: checkout del código, instalación de Doxygen y Graphviz, generación de documentación mediante `doxygen doc/Doxyfile`, y commit automático de los archivos HTML generados. Adicionalmente, existe un segundo workflow en `.github/workflows/ci.yaml` que ejecuta tests con pytest y actualiza el README, también disparado por push a main y opcionalmente mediante `workflow_dispatch`
El workflow ejecuta cuatro pasos: checkout del código, instalación de Doxygen y Graphviz, generación de documentación y commit automático de los cambios. Esto garantiza que la documentación esté siempre actualizada con el código fuente.


