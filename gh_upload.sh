#!/bin/bash

# Nombre del workflow a ejecutar
workflow_name="build.yml"

# Lanzar la compilación
gh workflow run $workflow_name

# Esperar unos segundos para asegurar que el workflow ha empezado
sleep 5

# Obtener el ID de la última ejecución del workflow
run_id=$(gh run list --workflow=$workflow_name --limit 1 --json databaseId -q '.[0].databaseId')

# Verificar que se obtuvo un run_id
if [ -z "$run_id" ]; then
  echo "No se pudo obtener el ID de la ejecución del workflow."
  exit 1
fi

# Esperar a que termine la compilación
gh run watch $run_id

# Verificar el estado final del run
status=$(gh run view $run_id --json status -q '.status')

if [ "$status" == "completed" ]; then
  conclusion=$(gh run view $run_id --json conclusion -q '.conclusion')
  echo "El workflow terminó con el estado: $conclusion"
  if [ "$conclusion" != "success" ]; then
    exit 1
  fi
else
  echo "El workflow no se completó."
  exit 1
fi


# Paso 1: Crear la nueva release
gh release create v1.0.0 --notes "Primera versión estable" --title "Release v1.0.0"

# Esto devolverá el ID de la nueva release, por ejemplo: 123456

# Paso 2: Subir el artefacto a la nueva release
gh release upload 123456 mi_artefacto.zip