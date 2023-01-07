
## Descripcion

Simple GitHub Action  que se puede utilizar para comprobar si una la receta barlel es la correcta.

## Inputs

None

## Outputs 

None

## Examplo de uso

```yml
name: Receta Workflow
on:
  pull_request:
    branches:
      - main

jobs:
  test_la_receta: 
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dev dependencies
        run: pip install -r requirements.txt
      - name: Test la receta sugerida
        run: | 
          pytest -q test_receta.py 
```
## Limitaciones y errores

Este GitHub Action necesita de unsa mejora del `test_receta.py `. 
Por lo tanto, debe adicionar mas.
