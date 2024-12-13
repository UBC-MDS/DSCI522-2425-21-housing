# Makefile for Strathcona House Value Predictor

# Variables
RAW_DATA_URL = https://hub.arcgis.com/api/v3/datasets/e3c5b04fccdc4ddd88059a8c0b6d8160_0/downloads/data?format=csv&spatialRefId=3776&where=1%3D1
RAW_DATA_DIR = data/raw
PROCESSED_DATA_DIR = data/processed
RESULTS_DIR = results
PLOTS_DIR = $(RESULTS_DIR)/figures
MODELS_DIR = $(RESULTS_DIR)/models
PREDICTIONS_DIR = $(RESULTS_DIR)/tables
RAW_DATA_FILE = $(RAW_DATA_DIR)/Raw_2023_Property_Tax_Assessment.csv
CLEAN_DATA_FILE = $(PROCESSED_DATA_DIR)/Clean_2023_Property_Tax_Assessment.csv
TRAIN_DATA_FILE = $(PROCESSED_DATA_DIR)/train.csv
TEST_DATA_FILE = $(PROCESSED_DATA_DIR)/test.csv
PREPROCESSOR_FILE = $(MODELS_DIR)/preprocessor.pickle
PREDICTIONS_FILE = $(PREDICTIONS_DIR)/ten_houses_predictions.csv
EDA_SCRIPT = scripts/eda.py
PREPROCESS_SCRIPT = scripts/preprocess_data.py
MODEL_FITTING_SCRIPT = scripts/model_fitting.py
PREDICTIONS_SCRIPT = scripts/predictions.py
CLEAN_SCRIPT = scripts/clean_data.py
LOAD_SCRIPT = scripts/load_data.py
REPORT = notebook/strathcona_house_value_predictor.qmd

# Targets

.PHONY: all clean

all: eda model predict report

# Download raw data
$(RAW_DATA_FILE):
	mkdir -p $(RAW_DATA_DIR)
	python $(LOAD_SCRIPT) --url $(RAW_DATA_URL) --write-to $(RAW_DATA_DIR)

# Clean and preprocess data
$(CLEAN_DATA_FILE): $(RAW_DATA_FILE)
	mkdir -p $(PROCESSED_DATA_DIR)
	python $(CLEAN_SCRIPT) --raw-data $(RAW_DATA_FILE) --seed 123 --write-to $(PROCESSED_DATA_DIR)

# Preprocess the data
$(PREPROCESSOR_FILE): $(TRAIN_DATA_FILE)
	mkdir -p $(MODELS_DIR)
	python $(PREPROCESS_SCRIPT) --train-data $(TRAIN_DATA_FILE) --write-to $(MODELS_DIR)

# Generate exploratory data analysis plots
eda: $(CLEAN_DATA_FILE)
	mkdir -p $(PLOTS_DIR)
	python $(EDA_SCRIPT) --processed-data $(CLEAN_DATA_FILE) --plot-to $(PLOTS_DIR)

# Train model and cross-validate
model: $(TRAIN_DATA_FILE) $(TEST_DATA_FILE) $(PREPROCESSOR_FILE)
	python $(MODEL_FITTING_SCRIPT) --train-data $(TRAIN_DATA_FILE) --test-data $(TEST_DATA_FILE) \
		--preprocessor $(PREPROCESSOR_FILE) --results-to $(MODELS_DIR)

# Generate predictions
predict: $(PREPROCESSOR_FILE)
	mkdir -p $(PREDICTIONS_DIR)
	python $(PREDICTIONS_SCRIPT) --model-file $(MODELS_DIR)/ridge_pipeline.pickle \
		--output-file $(PREDICTIONS_FILE) --plot-to $(PLOTS_DIR)/predictions_visualization.png

# Render the final report
report: predict
	quarto render $(REPORT)

# Clean up generated files
clean:
	rm -rf results/figures/*.png \
	       results/models/*.pickle \
	       results/tables/*.csv \
	       data/processed/*.csv \
	       notebook/*.html \
	       notebook/*.pdf
	@echo "Cleaned all generated files. Ready to run 'make all'."
