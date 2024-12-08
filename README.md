# Strathcona House Value Predictor
## DSCI522-2425-21-housing

List of contributors : Yajing Liu , Gilbert Akuja, Tianjiao Jiang, Thamer Aldawood 

## Summary: 

Our team will be working on predicting house prices using the 2023 Property Tax Assessment dataset from Strathcona County Open Data portal. The dataset provides a wealth of information about houses, including attributes like size, location, and other features. By leveraging this data, we aim to build a robust predictive model that accurately estimates house values.

We acquired our dataset from Strathcona County Open Data portal - 2023_Property_Tax_Assessment. The dataset can be found at 
https://opendata-strathconacounty.hub.arcgis.com/datasets/e3c5b04fccdc4ddd88059a8c0b6d8160_0/explore

## Introduction:

The team will be using `Ridge` which is a linear model to predict the value of houses. Ridge is a regularization model that is used for predictive modeling and mitigates over fitting and improves model stability especially when features are highly correlated. Ridge helps create robust model that generalize well to new data.
The question we aim to answer: Can we predict house prices using publicly available housing data , and which features most influence the predictions?
Data description: For this project we are going to use the  2023 Property Tax Assessment from Strathcona County Open Data portal. The data set contains the following attributes related to the different houses. The variables we selected for the model are: <br>
                `meters` - numeric variable that show the size of the house <br>
                `garage` - categorical variable where Y means there is a garage and N means no garage. <br>
                `firepl` - categorical variable where Y means there is a fireplace and N means no fireplace<br>
                `bdevl` - categorical variable where Y meas the building was evaluated and N means it was not evaluated<br>
The data set was chosen for its rich feature set, adequate sample size, and public availability making it suitable for building a predictive model.

## Report
The final report can be found
[here](https://github.com/UBC-MDS/DSCI522-2425-21-housing/blob/main/notebook/strathcona_house_value_predictor.html).

## Setup and Run Analysis
1. To run our analysis, you must first clone our repo to your local machine. To do this, open your machine's terminal and navigate to a desired directory to clone the repo into, then run the following command:
```bash
git clone https://github.com/UBC-MDS/DSCI522-2425-21-housing.git
```

2. To set up the necessary packages for running the project, create a virtual environment by using `conda` with the environment file that was downloaded when you cloned our repo from the previous step. Navigate to where you cloned our repo and run the following command:
```bash
conda env create --file environment.yaml
```
This will setup all required packages.
Then activate the environment using:
```bash
conda activate 522-group21-housing
```
(Optional) If you cannot use the `Python [conda env:522-group21-housing]` kernel, please run the following code:
```bash
conda install nb_conda_kernels
```

3. Using Docker:
Docker is used to create reproducible, sharable and shippable computing environments for our analysis. This may be useful for you if you are having issues installing the required packages or if you simply don't wish to have them on your local computer.
To use Docker, visit their website [here](https://www.docker.com/), create an account, and download and install a version that is compatible with your computer. 
Once Docker is installed, ensure it is running and navigate to where you cloned our repo and run the following command in your terminal:
```bash
docker-compose up
```
While your Docker container is running, you may follow the instructions within it to run the analysis through it. Specifically, you want to copy the link that starts with "http://127.0.0.1:8888/lab?token=..." into your browser to access a Jupyter Lab instance on the Docker container through which you can run our analysis.

4. To run the analysis,open a terminal and run the following commands:

```
python scripts/load_data.py \
    --url="https://hub.arcgis.com/api/v3/datasets/e3c5b04fccdc4ddd88059a8c0b6d8160_0/downloads/data?format=csv&spatialRefId=3776&where=1%3D1" \
    --write-to=data/raw

python scripts/clean_data.py \
    --raw-data=data/raw/Raw_2023_Property_Tax_Assessment.csv \
    --seed=522 \
    --write-to=data/processed

python scripts/eda.py \
    --processed-data=data/processed/Clean_2023_Property_Tax_Assessment.csv \
    --plot-to=results/figures

python scripts/fit_breast_cancer_classifier.py \
    --training-data=data/processed/cancer_train.csv \
    --preprocessor=results/models/cancer_preprocessor.pickle \
    --columns-to-drop=data/processed/columns_to_drop.csv \
    --pipeline-to=results/models \
    --plot-to=results/figures \
    --seed=523


python scripts/evaluate_breast_cancer_predictor.py \
	--scaled-test-data=data/processed/cancer_test.csv \
	--pipeline-from=results/models/cancer_pipeline.pickle \
	--results-to=results/tables \
	--seed=524

quarto render notebook/strathcona_house_value_predictor.qmd --to html
quarto render notebook/strathcona_house_value_predictor.qmd --to pdf
```


## Dependencies:
  - python=3.11
  - vegafusion=1.6.9
  - vega_datasets
  - scipy
  - scikit-learn
  - conda-lock
  - altair-all=5.4.*
  - pandas
  - ipykernel
  - nb_conda_kernels
  - [Docker](https://www.docker.com/) 
  - [VS Code](https://code.visualstudio.com/download)
  - [VS Code Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)


## License
This project is under the Creative Commons Attribution 4.0 International Public License. See the [License file](https://github.com/UBC-MDS/DSCI522-2425-21-housing/blob/main/LICENSE.md) for more details.
 
