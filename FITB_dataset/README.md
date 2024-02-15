# Instruction
The panel dataset contains commercial customers' financial information and days past due indicator from 2000 to 2020. The goal is to build a binary classifier to predict customers 90+ days past due **(90+DPD)** probability. 

1. Load both training and testing sets.
2. Winsorize **"feature_3"** by limiting the extreme values to 1 percentile (left tail) and 99 percentile (right tail) on the training set. Name it **"feature_3_winsor"**. Make appropriate treatments on the testing set.
3. Identify missing values for **"feature_3_winsor"**. Then, impute the missings with median value on the training set. Name the new feature **"feature_3_impute"**. Make appropriate treatments on the testing set.
4. Identify missing values for **"feature_2"**. Then, for each **"id"**, impute the missings with the value from previous year, if not available, use the value from next year. Name the new feature **"feature_2_impute"**. Make appropriate treatments on the testing set.
5. Standardize **"feature_1"**, **"feature_2_impute"**, **"feature_3_impute"**, **"feature_4"** for the training set. Make appropriate treatments on the testing set. Name the features **"feature_1_standard"**, **"feature_2_standard"**, **"feature_3_standard"**, **"feature_4_standard"**
6. Build a logistic regression on the training set to predict **'y'** being **(90+DPD)** using **"feature_1_standard"**, **"feature_2_standard"**, **"feature_3_standard"**, **"feature_4_standard"** as independent variables.
7. Report AUC on the **testing set**.
8. Report confusion matrix on the **testing set**.
9. Identify multicollinearity in the model. 
