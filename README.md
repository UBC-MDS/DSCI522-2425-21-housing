# DSCI522-2425-21-housing

List of contributors : Yajing Liu , Gilbert Akuja, Tianjiao Jiang, Thamer Aldawood 

## Summary: 

Our team will be working on predicting house prices using the 2023 Property Tax Assessment dataset from Strathcona County Open Data portal. The dataset provides a wealth of information about houses, including attributes like size, location, and other features. By leveraging this data, we aim to build a robust predictive model that accurately estimates house values.

We acquired our dataset from Strathcona County Open Data portal - 2023_Property_Tax_Assessment. The dataset can be found at 
https://opendata-strathconacounty.hub.arcgis.com/datasets/e3c5b04fccdc4ddd88059a8c0b6d8160_0/explore

## Introduction:

The team will be using `Ridge` which is a linear model to predict the value of houses. Ridge is a regularization model that is used for predictive modeling and mitigates over fitting, improves model stability especially when features are highly correlated. Ridge helps create robust model that generalize well to new data.
The question we aim to answer: Can we predict house prices using publicly available housing data , and which features most influence the predictions?
Data description: For this project we are going to use the  2023 Property Tax Assessment from Strathcona County Open Data portal. The data set contains the following attributes related to the different houses. The variables we selected for the model are: <br>
                `meters` - numeric variable that show the size of the house <br>
                `garage` - categorical variable where Y means there is a garage and N means no garage. <br>
                `firepl` - categorical variable where Y means there is a fireplace and N means no fireplace<br>
                `bdevl` - categorical variable where Y meas the building was evaluated and N means it was not evaluated<br>
The data set was chosen for its rich feature set, adequate sample size, and public availability making it suitable for building a predictive model.

## Dependencies:
  - python>=3.11,<3.13
  - pip
  - ipykernel
  - nb_conda_kernels
  - otter-grader=6.*
  - altair-all=5.4.*
  - vegafusion<2
  - vega_datasets
  - scipy
  - matplotlib>=3.2.2
  - scikit-learn
  - requests>=2.24.0
  - graphviz
  - python-graphviz
  - eli5
  - shap
  - jinja2
  - lightgbm
  - spacy
  - xgboost
  - catboost
  - nltk
  - imbalanced-learn
  - pip:
    - mglearn
    - spacymoji
    - altair_ally>=0.1.1
https://scikit-learn.org/stable/model_selection.html
4. FastExpert, How Much Value Does a Garage Add to a House?. - Retrieved 2024.
https://www.fastexpert.com/blog/how-much-value-does-a-garage-add-to-a-house/
