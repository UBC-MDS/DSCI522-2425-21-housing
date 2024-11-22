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

## Discussion:

Our findings suggest that the 10 houses in 2023_Property_Assessment_Predictions.csv are expected to be valued at:
1. $527,136
2. $451,522
3. $390,751
4. $224,816
5. $654,274
6. $419,325
7. $328,692
8. $498,644
9. $400,551
10. $453,980

We have also noticed that there is a correlation between a house's price and its property's size, whether or not it has a garage, fireplace, basement, and whether or not the building has been evaluated.
This is consistent with our expectations as the larger a property is, and the more features it has (basement, garage, etc.) the higher its value becomes.
This also raises further questions such as what other features of a house or property affect its value? characteristics for future consideration include: Number of bedrooms, number of bathrooms, indoor space, outdoor space, and number of floors.

## References:
1. Strathcona Country Open Data, 2023 Property Tax Assessment. - Retrieved 2024.
https://opendata-strathconacounty.hub.arcgis.com/datasets/e3c5b04fccdc4ddd88059a8c0b6d8160_0/explore
2. Altair Tutorial, Exploratory Data Visualization with Altair. - Retrieved 2024.
https://altair-viz.github.io/altair-tutorial/README.html
3. Scikit Learn, Model selection and evaluation. - Retrieved 2024.
https://scikit-learn.org/stable/model_selection.html
4. FastExpert, How Much Value Does a Garage Add to a House?. - Retrieved 2024.
https://www.fastexpert.com/blog/how-much-value-does-a-garage-add-to-a-house/