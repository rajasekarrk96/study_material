@echo off
:: Create the main folder for Data Science Libraries
mkdir "Data_Science_Libraries"

:: Change to the main directory
cd "Data_Science_Libraries"

:: 1. Core Libraries
mkdir "01_Core_Libraries"
cd "01_Core_Libraries"
mkdir "NumPy"
mkdir "Pandas"
mkdir "Matplotlib"
mkdir "Seaborn"
cd ..

:: 2. Visualization
mkdir "02_Visualization"
cd "02_Visualization"
mkdir "Plotly"
mkdir "Bokeh"
mkdir "Altair"
mkdir "Dash"
mkdir "ggplot"
cd ..

:: 3. Machine Learning
mkdir "03_Machine_Learning"
cd "03_Machine_Learning"
mkdir "Scikit-learn"
mkdir "XGBoost"
mkdir "LightGBM"
mkdir "CatBoost"
mkdir "TensorFlow"
mkdir "PyTorch"
mkdir "Keras"
cd ..

:: 4. Data Preprocessing
mkdir "04_Data_Preprocessing"
cd "04_Data_Preprocessing"
mkdir "Scipy"
mkdir "FeatureTools"
mkdir "Category_Encoders"
mkdir "Data_Cleaning_Tools"
mkdir "Data_Imputation_Tools"
cd ..

:: 5. Deep Learning
mkdir "05_Deep_Learning"
cd "05_Deep_Learning"
mkdir "TensorFlow"
mkdir "PyTorch"
mkdir "Keras"
mkdir "HuggingFace"
mkdir "FastAI"
cd ..

:: 6. NLP
mkdir "06_NLP"
cd "06_NLP"
mkdir "NLTK"
mkdir "SpaCy"
mkdir "Gensim"
mkdir "Transformers_HuggingFace"
mkdir "TextBlob"
cd ..

:: 7. Big Data and Distributed
mkdir "07_Big_Data_and_Distributed"
cd "07_Big_Data_and_Distributed"
mkdir "Apache_Spark"
mkdir "Dask"
mkdir "Ray"
mkdir "Hadoop"
cd ..

:: 8. AutoML
mkdir "08_AutoML"
cd "08_AutoML"
mkdir "H2O.ai"
mkdir "Auto-sklearn"
mkdir "TPOT"
mkdir "MLJar"
mkdir "PyCaret"
cd ..

:: 9. Model Interpretability
mkdir "09_Model_Interpretability"
cd "09_Model_Interpretability"
mkdir "SHAP"
mkdir "LIME"
mkdir "ELI5"
cd ..

:: 10. Reinforcement Learning
mkdir "10_Reinforcement_Learning"
cd "10_Reinforcement_Learning"
mkdir "OpenAI_Gym"
mkdir "Stable_Baselines3"
mkdir "RLlib"
cd ..

:: 11. Specialized Libraries
mkdir "11_Specialized_Libraries"
cd "11_Specialized_Libraries"
mkdir "Biopython"
mkdir "Geopandas"
mkdir "PyCaret"
mkdir "Folium"
mkdir "PySAL"
cd ..

echo Folder structure for Data Science Libraries created successfully!
pause
