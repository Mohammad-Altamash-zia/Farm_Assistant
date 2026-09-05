# config.py

# -----------------------------
# MODEL PATHS
# -----------------------------

DISEASE_MODEL = "models/disease.onnx"
PEST_MODEL = "models/pest.onnx"
NUTRITION_MODEL = "models/nutrition.onnx"
STAGE_MODEL = "models/stage.onnx"


# -----------------------------
# DIRECTORIES
# -----------------------------

IMAGE_DIR = "received_images"
RESULT_DIR = "results"


# -----------------------------
# DETECTION SETTINGS
# -----------------------------

IMAGE_SIZE = 640

DISEASE_CONF = 0.40
PEST_CONF = 0.35
NUTRITION_CONF = 0.45
STAGE_CONF = 0.45


# NMS IoU threshold
IOU = 0.45


# -----------------------------
# QUEUE
# -----------------------------

MAX_QUEUE_SIZE = 3


# -----------------------------
# NUTRITION CLASSES
# -----------------------------

NUTRITION_ALLOWED = {
    "healthy",
    "magnesium deficiency",
    "nitrogen deficiency",
    "potassium deficiency"
}