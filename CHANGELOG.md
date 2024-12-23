- [x] .DS_Store and .ipynb_checkpoints should not be committed.  
  - [Delete .DS_Store](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/c45c9c4b852133e87f6525a20f89c9cabfa11c6a)
  - [Delete .npm directory](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/97a8f9e1c4487d5a23b1beded7c5720c59e42b8e)
  - [Delete .ipynb_checkpoints directory](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/c3c3eed684d152ad938db47311e9e2837af2047b)
  - [Delete notebook/.ipynb_checkpoints directory](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/df8f354d7325337d12ff14c902b06533f1bda6b8)
- [x] The email under "enforcement" should be tied to the team
  - [Update CODE_OF_CONDUCT.md change to correct email address](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/eb096f6b0455227fe455cf19932b20d23d56cf54)
  - [Update CODE_OF_CONDUCT.md add email address](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/ee6150136289e88dd704c4ebdf2959d9b691ba3c)
- [x] Raw and processed/intermediate data are mixed in the data directory (they should be in subfolders, or at least clearly labelled).
  - [clean unused data files](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/6f615b20e301a3a6e3da2c60731cbde4d3bb772e)
- [x] Did not render report to PDF or HTML.
  - [edited scripts, README file, rendered to html and pdf](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/b0bcf45838a029477630037dbbbe2675fc10661b)
- [x] versions are missing from environment files(s) for some R or Python packages
  - [Added versions to packages](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/6f4dca7b4ee486b32cb888373e62f61e08367fb5)
- [x] Does not clearly report the major findings.
   - [Final PDF](https://github.com/UBC-MDS/DSCI522-2425-21-housing/blob/main/notebook/strathcona_house_value_predictor.pdf)
- [x] Does not discuss importance and limitations of findings.
    - [Final PDF](https://github.com/UBC-MDS/DSCI522-2425-21-housing/blob/main/notebook/strathcona_house_value_predictor.pdf)
- [x] Does not explain why this problem is important or interesting.
     - [Final PDF](https://github.com/UBC-MDS/DSCI522-2425-21-housing/blob/main/notebook/strathcona_house_value_predictor.pdf)
- [x] Did not reference the data set when referring to it.
  - [Update README.md with reference](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/52cd0164da6f8ef1c66d49df8ba11799c6daa9af)
- [x] Important methodology descriptions missing (e.g., did not explain in narrative what metric was being used for model parameter optimization).
  - [Final PDF](https://github.com/UBC-MDS/DSCI522-2425-21-housing/blob/main/notebook/strathcona_house_value_predictor.pdf)
- [x] Some key references are missing.
  - [Final PDF](https://github.com/UBC-MDS/DSCI522-2425-21-housing/blob/main/notebook/strathcona_house_value_predictor.pdf)
- [x] Many software or packages versions are not pinned in the environment specification file(s).
  - [Added versions to packages](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/6f4dca7b4ee486b32cb888373e62f61e08367fb5)
- [x] The platform key and value is missing from the  docker-compose.yml file, causing issues when running on different chip architectures.
  - [Update docker-compose.yml](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/444f5d78408213adc9c82802d2bb16340389d44a)
- [x] Latest tag was used for docker. This is not ideal because if the user has latest locally, but there is a newer version on the container registry, then Docker will not pull it.
  - [Update docker-publish.yml](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/afc5bab4263de4e51c9aafdb75286e9d40531abb)
- [x] Committing unnecessary files.
  - [Delete .DS_Store](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/c45c9c4b852133e87f6525a20f89c9cabfa11c6a)
  - [Delete .npm directory](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/97a8f9e1c4487d5a23b1beded7c5720c59e42b8e)
  - [Delete .ipynb_checkpoints directory](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/c3c3eed684d152ad938db47311e9e2837af2047b)
  - [Delete notebook/.ipynb_checkpoints directory](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/df8f354d7325337d12ff14c902b06533f1bda6b8)
- [x] Some branch names are not meaningful (they should reflect the work being done on the branch).
 - https://github.com/UBC-MDS/DSCI522-2425-21-housing/branches
- [x] GitHub issues were used somewhat for project communication.
  - [Issues](https://github.com/UBC-MDS/DSCI522-2425-21-housing/issues?q=)
- [x] error occurred when render to html and pdf
  - [preprocess_data.py](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/3dc7c01aa42c927a1ca5615e939ec1bb3983ed08)
  - [edited eda.py](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/3eb80a95c46d5e5531c5c5273803502ab856ee1c)
- [x] create a visualization for this that shows the pairwise correlation between the features and the targets. this can be done by importing altair_ally and using the aly.corr() method.
  - [Added new EDA, Dummy baseline, optimized model.](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/374a034b25663e9cf229b8556c4a2d58c3f2f173)
- [x] Baseline model for comparison
  - [Added new EDA, Dummy baseline, optimized model.](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/374a034b25663e9cf229b8556c4a2d58c3f2f173)
- [x] Spelling/Grammatical Errors in report
  - [corrected Grammatical Errors](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/4d374606e587411e009a0acba35dbdedfe3cccbd)
- [x] Importance of the Research Question
  - [added importance of question and limitations](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/df25a7b6b3a65f6d5b8a82a3edc992189a4e5265)
- [x] Limitations
  - [added importance of question and limitations](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/df25a7b6b3a65f6d5b8a82a3edc992189a4e5265)
- [x] The report does not include explicit guidelines for contributors or instructions for seeking support.
  - [Update README.md with support section](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/c32f9c993ba225ab212e2af818b8bb19a0c61d0f)
- [x] In the Summary section, some conclusions about the performance of the final model could have been included
  - [include evaluation of model performance](https://github.com/UBC-MDS/DSCI522-2425-21-housing/commit/7d3c785e52752c44ce9b8d01611952151a2dac15)
- [x] When creating the Ridge regression model, could have added a step to do a grid search to tune the hyperparameter.