# Predictive Modeling of ICU Patient Outcomes Using Autoencoders

This project explores predictive modeling for ICU patient outcomes using clinical time-series summary features and deep learning. The work focuses on preparing ICU patient data, engineering preprocessing pipelines for mixed clinical variables, and experimenting with neural network models, including autoencoder-based reconstruction methods and multi-output prediction models.

## Project Overview

ICU datasets often contain incomplete, heterogeneous patient measurements such as vital signs, lab values, demographics, ventilation status, and unit type. This project uses a filtered ICU dataset to model important patient outcomes, including in-hospital mortality and length of stay.

The notebooks walk through data loading, missing-value analysis, feature preprocessing, model construction, and evaluation. The autoencoder notebook trains a neural network to learn compact representations of ICU patient profiles and uses reconstruction behavior as part of the outcome modeling workflow.

## Key Features

- Preprocessing of ICU clinical variables, including demographic, vital sign, laboratory, and ventilation features
- Handling of missing values using scikit-learn preprocessing pipelines
- Encoding of categorical and ordinal clinical features
- Autoencoder implementation with TensorFlow/Keras
- Functional API model for multi-output prediction of patient outcomes
- Evaluation using classification metrics such as accuracy, precision, and recall

## Repository Contents

- `ICU_filtered.csv` - Filtered ICU dataset with 7,886 patient records
- `ICU_Autoencoder.ipynb` - Autoencoder-based modeling workflow for ICU outcome analysis
- `ICU_FunctionalAPI.ipynb` - TensorFlow/Keras Functional API model for mortality and length-of-stay prediction
- `ICU_Pipeline.ipynb` - scikit-learn preprocessing pipeline for clinical data preparation

## Dataset

The dataset includes patient-level ICU features such as age, gender, ICU unit indicators, first recorded vital signs, lab measurements, mechanical ventilation status, urine output, length of stay, and in-hospital death.

Primary outcome fields:

- `In_hospital_death`
- `Length_of_stay`

## Technologies Used

- Python
- pandas
- NumPy
- scikit-learn
- TensorFlow/Keras
- Matplotlib

## How to Run

Open the notebooks in Jupyter Notebook, JupyterLab, or VS Code and run them in this order:

1. `ICU_Pipeline.ipynb`
2. `ICU_FunctionalAPI.ipynb`
3. `ICU_Autoencoder.ipynb`

If needed, update the dataset path inside the notebooks to point to the local `ICU_filtered.csv` file in this folder.

## Project Goal

The goal is to investigate how deep learning methods, especially autoencoders, can support predictive analysis of ICU patient outcomes by learning meaningful latent representations from noisy and incomplete clinical data.
