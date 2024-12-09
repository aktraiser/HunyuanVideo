# Guide d'installation HunyuanVideo

## Prérequis
- Ubuntu 22.04 ou plus récent
- NVIDIA GPU avec CUDA 12.0 ou plus récent
- Docker installé

## 1. Installation

### 1.1 Cloner le dépôt
```
bash
git clone https://github.com/Tencent/HunyuanVideo.git
cd HunyuanVideo
```

### 1.2 Lancer le conteneur Docker
```
bash
docker pull hunyuanvideo/hunyuanvideo:cuda_12
docker run -itd \
--gpus all \
--init \
--net=host \
--uts=host \
--ipc=host \
--name hunyuanvideo \
--security-opt=seccomp=unconfined \
--ulimit=stack=67108864 \
--ulimit=memlock=-1 \
--privileged \
hunyuanvideo/hunyuanvideo:cuda_12
```

### 1.3 Se connecter au conteneur
```
bash
docker exec -it hunyuanvideo bash
```
### 1.4 Préparer l'environnement dans le conteneur
```
bash
cd /workspace
git clone https://github.com/Tencent/HunyuanVideo.git
cd HunyuanVideo
pip install -r requirements.txt
```
## 2. Téléchargement des modèles

### 2.1 Créer les dossiers nécessaires
```
bash
mkdir -p ckpts/hunyuan-video-t2v-720p/transformers/
mkdir -p ckpts/text_encoder
mkdir -p ckpts/text_encoder_2
```
### 2.2 Télécharger les modèles
#### Télécharger le modèle principal
```
bash
huggingface-cli download tencent/HunyuanVideo --local-dir ./ckpts
```
#### Télécharger l'encodeur de texte LLM
```
bash
huggingface-cli download xtuner/llava-llama-3-8b-v1_1-transformers --local-dir ./ckpts/llava-llama-3-8b-v1_1-transformers
```
#### Prétraiter l'encodeur LLM
```
python hyvideo/utils/preprocess_text_encoder_tokenizer_utils.py \
--input_dir ckpts/llava-llama-3-8b-v1_1-transformers \
--output_dir ckpts/text_encoder
```
#### Télécharger l'encodeur CLIP
```
bash
huggingface-cli download openai/clip-vit-large-patch14 --local-dir ./ckpts/text_encoder_2
```

## 3. Générer une vidéo

### 3.1 Commande de base
```
bash
python sample_video.py \
--video-size 720 1280 \
--video-length 129 \
--prompt "A dog running on grass" \
--flow-reverse \
--use-cpu-offload \
--save-path ./results
```
### 3.2 Options principales
- `--video-size`: Taille de la vidéo (hauteur largeur)
- `--video-length`: Nombre de frames
- `--prompt`: Description textuelle de la vidéo
- `--flow-reverse`: Active le flux inversé
- `--use-cpu-offload`: Utilise le CPU pour décharger la mémoire GPU
- `--save-path`: Dossier de sauvegarde des résultats
- `--infer-steps`: Nombre d'étapes d'inférence (défaut: 50)
- `--cfg-scale`: Échelle de guidance (défaut: 1.0)
- `--embedded-cfg-scale`: Échelle de guidance embarquée (défaut: 6.0)

## Structure des dossiers

HunyuanVideo/
└── ckpts/
├── hunyuan-video-t2v-720p/
│ ├── transformers/
│ └── vae/
├── text_encoder/
└── text_encoder_2/

## Notes
- La génération d'une vidéo peut prendre plusieurs minutes selon votre GPU
- Les vidéos générées seront sauvegardées dans le dossier spécifié par `--save-path`
- Assurez-vous d'avoir suffisamment d'espace disque (~40GB) pour les modèles
