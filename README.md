# Strathcona House Value Predictor
## DSCI522-2425-21-housing

List of contributors : Yajing Liu , Gilbert Akuja, Tianjiao Jiang, Thamer Aldawood 

## Summary: 

Our team will be working on predicting house prices using the 2023 Property Tax Assessment dataset from Strathcona County Open Data portal. The dataset provides a wealth of information about houses, including attributes like size, location, and other features. By leveraging this data, we aim to build a robust predictive model that accurately estimates house values.

We acquired our dataset from Strathcona County Open Data portal - 2023_Property_Tax_Assessment. The dataset can be found  
[here](https://opendata-strathconacounty.hub.arcgis.com/datasets/e3c5b04fccdc4ddd88059a8c0b6d8160_0/explore)

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

2. Using Docker:
Docker is used to create reproducible, sharable and shippable computing environments for our analysis. This may be useful for you if you are having issues installing the required packages or if you simply don't wish to have them on your local computer.
To use Docker, visit their website [here](https://www.docker.com/), create an account, and download and install a version that is compatible with your computer. 
Once Docker is installed, ensure it is running and navigate to where you cloned our repo and run the following command in your terminal:
```bash
docker-compose up
```
While your Docker container is running, you may follow the instructions within it to open a Jupyter Lab. Specifically, you want to copy the link that starts with "http://127.0.0.1:8888/lab?token=..." into your browser to access a Jupyter Lab instance on the Docker container through which you can run our analysis.

3. (Optional) If you prefer to use a local environment instead of Docker: 
set up the necessary packages for running the project, create a virtual environment by using `conda` with the environment file that was downloaded when you cloned our repo from the previous step. Navigate to where you cloned our repo and run the following command:
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

4. Using Makefile to run the project:

Activate the Conda Environment:
```
conda activate 522-group21-housing
```
Navigate to the root of this project on your computer using the command line and enter the following command to reset the project to a clean state
```
make clean
```
To run the analysis in its entirety, enter the following command in the terminal in the project root:
```
make all
```
Incase you run into any error while running make all, pip install module-name. Run make clean and then make all again.

5. When you are finished, stop and clean up the container by typing Ctrl + C in the terminal where you launched the container, and then type
```bash
docker-compose rm
```
(Optional)
In case you get some errors like:
```bash
ERROR: 
No such kernel named 522-group21-housing
Starting 522-group21-housing kernel...ERROR:
```
You can run following commands to address the issue:
(You don't need to run first command if you already in the environment: 522-group21-housing)
```bash
conda activate 522-group21-housing

python -m ipykernel install --user --name=522-group21-housing

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
  - click
  - quarto
  - [Docker](https://www.docker.com/)

## Support
If you encounter any issues while using this project, or if you have questions about the implementation, you can follow the steps below:
1. Reporting Issues:
 - Use the [Issues](https://github.com/UBC-MDS/DSCI522-2425-21-housing/issues) tab in this repository to report bugs, request new features, or raise any concerns.
 - Provide as much detail as possible, including steps to reproduce the issue, the environment you're running on, and relevant logs or screenshots.
2. Seeking Help:
 - Contact the contributors via email (tjqu2024@student.ubc.ca, yajing03@student.ubc.ca, thamerd@student.ubc.ca and gakuja@student.ubc.ca) if you have specific questions not covered in the documentation or issue tracker.
3. Contributing:
 - If you'd like to contribute to this project, please review the [CONTRIBUTING.md](https://github.com/UBC-MDS/DSCI522-2425-21-housing/blob/main/CONTRIBUTING.md) file for guidelines on how to get started. Contributions are welcome in the form of bug fixes, feature additions, or documentation improvements.


## License
This project is under the Creative Commons Attribution 4.0 International Public License. See the [License file](https://github.com/UBC-MDS/DSCI522-2425-21-housing/blob/main/LICENSE.md) for more details.

## Reference
County, Strathcona. 2023. “2023 Property Tax Assessment.” https://www.strathcona.ca/services/assessment/.
