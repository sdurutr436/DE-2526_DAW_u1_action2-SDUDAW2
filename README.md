d2fcc59 Update Doxygen documentation
0bf1897 Update README con estado de tests
d44b259 Añadido cambio a yaml para que pueda añadir los cambios a main en lugar de github publish
78a1cad Update README con estado de tests
ecb5724 Cambiado doxygen para representar mejor los cambios


# Proyecto: Documentación Automática y CI con GitHub Actions

En este repositorio he implementado un flujo de integración continua (CI) que ejecuta tests, genera documentación en varios formatos y registra automáticamente los cambios en el repositorio. El objetivo es dejar el proyecto listo para el trabajo en equipo, donde cada cambio dispare el pipeline, actualice la documentación y facilite la revisión y el despliegue.

**Enlace a la documentación generada:**
https://sdurutr436.github.io/DE-2526_DAW_u1_action2-SDUDAW2/doc/html/

## a) Herramienta de generación de documentación

He utilizado **Doxygen** como herramienta de generación de documentación automática para el código Python. La configuración se encuentra en el archivo `doc/Doxyfile`. El workflow de GitHub Actions está definido en `.github/workflows/doxygen.yml` y ejecuta Doxygen automáticamente en cada push a las ramas `main` o `master`, generando la documentación HTML en `doc/html` y LaTeX en `doc/latex`.

## b) Documentación de componentes

He documentado la función principal del proyecto utilizando docstrings en formato Google Style, que es compatible con Doxygen. Ejemplo extraído de `main.py`:

```python
def saludo(nombre: str):
    """
    Devuelve un saludo personalizado.

    Args:
        nombre (str): Nombre de la persona a saludar.

    Returns:
        str: Saludo personalizado.
    """
    return f"Hola, {nombre}!"
```

El estilo utilizado es **Google Style** para Python, que estructura los argumentos y el valor de retorno de forma clara. Doxygen procesa estos docstrings y genera la documentación correspondiente, que puede consultarse en el HTML generado.

## c) Multiformato

La documentación se genera en dos formatos:

- **HTML**: Navegable, ubicada en `doc/html` y publicada automáticamente en GitHub Pages.
- **LaTeX**: Ubicada en `doc/latex`, permite generar PDF si se compila con una herramienta como `pdflatex`.

La configuración relevante en `doc/Doxyfile` es:

```
GENERATE_HTML = YES
GENERATE_LATEX = YES
```

El workflow ejecuta:

```
doxygen doc/Doxyfile
```

Esto produce ambos formatos. El commit automático solo incluye el HTML, pero el LaTeX queda disponible localmente para su conversión a PDF.

## d) Colaboración

GitHub facilita el trabajo colaborativo mediante:

- **Pull Requests**: Permiten proponer cambios y revisarlos antes de integrarlos en la rama principal.
- **Protección de ramas**: Se puede configurar para que solo se pueda hacer merge tras pasar los checks de CI y recibir aprobación de revisores.
- **Checks automáticos**: Los workflows de GitHub Actions validan que los tests pasen y que la documentación se genere correctamente en cada push o PR.
- **Historial y trazabilidad**: Cada cambio queda registrado y es fácilmente revisable por el equipo.

Por ejemplo, si un colaborador propone una mejora en la documentación, debe abrir un Pull Request. El pipeline se ejecuta automáticamente, y solo si los tests y la generación de documentación son correctos, se puede aprobar el merge.

## e) Control de versiones

El control de versiones se gestiona con Git y GitHub. Ejemplo de mensajes de commit utilizados en este proyecto:

```
d2fcc59 Update Doxygen documentation
0bf1897 Update README con estado de tests
d44b259 Añadido cambio a yaml para que pueda añadir los cambios a main en lugar de github publish
78a1cad Update README con estado de tests
ecb5724 Cambiado doxygen para representar mejor los cambios
```

Estos mensajes son claros y descriptivos, ya que indican exactamente qué se ha modificado. Por ejemplo, "Update Doxygen documentation" deja claro que se ha actualizado la documentación generada automáticamente, y "Añadido cambio a yaml" especifica el archivo y el propósito del cambio.

## f) Accesibilidad y seguridad

Para garantizar la seguridad y la accesibilidad del repositorio, he aplicado las siguientes medidas:

1. **Control de visibilidad**: El repositorio puede configurarse como privado o público según las necesidades del equipo.
2. **Gestión de permisos**: GitHub permite asignar roles (admin, write, read) a los colaboradores.
3. **Protección de ramas**: Se puede exigir que los cambios pasen por revisión y CI antes de integrarse en la rama principal.
4. **Uso de secrets**: Los workflows utilizan el token `secrets.GITHUB_TOKEN` para operaciones seguras sin exponer credenciales.
5. **Permisos mínimos en workflows**: En el workflow se limita el permiso a `contents: write` para evitar operaciones innecesarias.

## g) Instalación y uso documentados

### Requisitos
- Python 3.x
- pytest (para ejecutar los tests)
- Doxygen y Graphviz (para generar la documentación)

### Ejecución de tests
Para ejecutar los tests y actualizar el estado en el README:

```
python update_readme.py
```

Esto ejecuta los tests definidos en `test_main.py` y actualiza la sección correspondiente en el README con el resultado y la fecha/hora.

### Generación de documentación
Para generar la documentación localmente:

```
doxygen doc/Doxyfile
```

La documentación HTML se genera en `doc/html` y la LaTeX en `doc/latex`.

### Funcionamiento del workflow
El workflow de documentación está en `.github/workflows/doxygen.yml` y ejecuta automáticamente la generación y commit de la documentación en cada push a main/master.

## h) Integración continua

El workflow implementado es un ejemplo de integración continua (CI) porque automatiza la verificación y generación de artefactos en cada cambio del código fuente. El workflow se dispara automáticamente con el evento `push` a las ramas main y master:

```yaml
on:
  push:
    branches:
      - main
      - master
```

El pipeline realiza los siguientes pasos:

1. Checkout del código
2. Instalación de Doxygen y Graphviz
3. Generación de la documentación con `doxygen doc/Doxyfile`
4. Commit y push automático de la documentación HTML generada

Esto garantiza que la documentación esté siempre actualizada y disponible para el equipo, y que cualquier error en la generación se detecte de inmediato.


