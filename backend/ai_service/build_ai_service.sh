#!/usr/bin/env bash

IMAGE_NAME="ai-service"
IMAGE_TAG="v1"
PLATFORMS="linux/amd64,linux/arm64"
TAR_FILE="${IMAGE_NAME}_${IMAGE_TAG}.tar"

echo "=========================================="
echo "🐳 Construyendo imagen Docker multi-plataforma: $IMAGE_NAME:$IMAGE_TAG"
echo "Plataformas: $PLATFORMS"
echo "=========================================="

docker buildx build --platform $PLATFORMS -t "$IMAGE_NAME:$IMAGE_TAG" --load .

if [ $? -ne 0 ]; then
  echo "❌ Error al construir la imagen multi-plataforma"
  exit 1
fi

echo "✅ Imagen construida y cargada en el daemon local: $IMAGE_NAME:$IMAGE_TAG"

echo "=========================================="
echo "💾 Guardando la imagen en archivo: $TAR_FILE"
echo "=========================================="

docker save -o "$TAR_FILE" "$IMAGE_NAME:$IMAGE_TAG"

if [ $? -ne 0 ]; then
  echo "❌ Error al guardar la imagen en archivo"
  exit 1
fi

echo "✅ Imagen guardada correctamente en $TAR_FILE"