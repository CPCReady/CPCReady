#!/bin/bash

# Preparar la estructura de directorios

# Crear el paquete
pkgbuild --root . \
         --identifier com.destroyer.cpcready \
         --version 1.0.0 \
         --install-location ~/CPCReady \
         --scripts scripts \
         CPCReady.pkg

echo "Paquete creado: CPCReady.pkg"

# Crear el archivo de distribución XML
cat <<EOF > distribution.xml
<?xml version="1.0" encoding="utf-8"?>
<installer-gui-script minSpecVersion="1">
    <title>CPCReady</title>
    <background file="example.png" mime-type="image/png" />
    <license file="LICENSE"/>
    <pkg-ref id="com.destroyer.cpcready">
        <bundle-version>1.0.0</bundle-version>
    </pkg-ref>
</installer-gui-script>
EOF

mkdir -p resources
echo "Your license text goes here." > resources/LICENSE

# Crear el instalador .pkg con productbuild
productbuild --distribution distribution.xml \
             --package-path . \
             --resources resources \
             --identifier com.destroyer.cpcready \
             --version 1.0.0 \
             CPCReady.pkg

echo "Instalador creado: CPCReady.pkg"