import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score
import joblib

# Cargar los datos
data = pd.read_csv(r"Inputs/dataset_alpha_betha.csv")
to_predict = pd.read_csv(r"Inputs/to_predict.csv")

# Reemplazar valores vacíos (espacios, cadenas vacías, None, NaN)
data.replace([' ', '', None], np.nan, inplace=True)
to_predict.replace([' ', '', None], np.nan, inplace=True)

# Verificar si hay NaN en el dataset antes de continuar
print("Cantidad de valores NaN por columna en los datos de entrada:")
print(data.isnull().sum())

# Preprocesamiento (manejo de columnas numéricas y categóricas)
# Identificar las columnas numéricas y categóricas
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = data.select_dtypes(include=['object']).columns.tolist()

# Excluir 'autoID', 'Demand' y 'Class' que no son relevantes para la predicción
numerical_cols = [col for col in numerical_cols if col not in ['autoID', 'Demand', 'Class']]
categorical_cols = [col for col in categorical_cols if col not in ['autoID', 'Demand', 'Class']]

# Asegurarnos de que las columnas numéricas sean de tipo float
for col in numerical_cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Dividir los datos en características y etiquetas
X = data.drop(['Demand', 'Class'], axis=1)
y_class = data["Class"]
y_demand = data['Demand']

# Imputación de valores faltantes antes de la división
imputer_num = SimpleImputer(strategy='mean')
X[numerical_cols] = imputer_num.fit_transform(X[numerical_cols])

imputer_cat = SimpleImputer(strategy='most_frequent')
X[categorical_cols] = imputer_cat.fit_transform(X[categorical_cols])

# Verificar si hay NaN después de la imputación
print("Cantidad de valores NaN por columna después de imputar en los datos de entrada:")
print(X.isnull().sum())

# Dividir en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_class_train, y_class_test, y_demand_train, y_demand_test = train_test_split(X, y_class, y_demand, test_size=0.2, random_state=42)

# Verificar si hay NaN en el conjunto de entrenamiento
print("Cantidad de valores NaN por columna en los datos de entrenamiento:")
print(X_train.isnull().sum())

# Pipeline para predecir la clase
pipeline_class = Pipeline([
    ('preprocessor', ColumnTransformer([
        ('num', Pipeline([
            ('scaler', StandardScaler())  # Escalado de las características numéricas
        ]), numerical_cols),
        ('cat', Pipeline([
            ('onehot', OneHotEncoder(handle_unknown='ignore'))  # Codificación One-Hot de las características categóricas
        ]), categorical_cols)
    ])),
    ('classifier', RandomForestClassifier(random_state=42))  # Clasificador RandomForest
])

# Entrenar el modelo para predecir la clase
pipeline_class.fit(X_train, y_class_train)

# Pipeline para predecir la demanda
pipeline_demand = Pipeline([
    ('preprocessor', ColumnTransformer([
        ('num', Pipeline([
            ('scaler', StandardScaler())  # Escalado de las características numéricas
        ]), numerical_cols),
        ('cat', Pipeline([
            ('onehot', OneHotEncoder(handle_unknown='ignore'))  # Codificación One-Hot de las características categóricas
        ]), categorical_cols)
    ])),
    ('regressor', RandomForestRegressor(random_state=42))  # Regresor RandomForest para la predicción de la demanda
])

# Entrenar el modelo para predecir la demanda
pipeline_demand.fit(X_train, y_demand_train)

# Guardar los modelos entrenados
joblib.dump(pipeline_class, 'modelo_class.pkl')
joblib.dump(pipeline_demand, 'modelo_demand.pkl')

# Evaluación de los modelos
y_class_pred = pipeline_class.predict(X_test)
y_demand_pred = pipeline_demand.predict(X_test)

# Métricas de clasificación
print("Métricas de clasificación para la clase:")
print(classification_report(y_class_test, y_class_pred))

# Métricas de regresión
print("Métricas de regresión para la demanda:")
print(f"MSE: {mean_squared_error(y_demand_test, y_demand_pred)}")
print(f"R2: {r2_score(y_demand_test, y_demand_pred)}")

# Realizar predicciones sobre los datos de 'to_predict'
X_to_predict = to_predict.drop(['Class'], axis=1, errors='ignore')  # Si no tiene columna 'Class', ignorarla

# Imputación para 'to_predict'
X_to_predict[numerical_cols] = imputer_num.transform(X_to_predict[numerical_cols])
X_to_predict[categorical_cols] = imputer_cat.transform(X_to_predict[categorical_cols])

# Verificar si hay NaN en 'to_predict' después de la imputación
print("Cantidad de valores NaN por columna en los datos de 'to_predict' después de imputar:")
print(X_to_predict.isnull().sum())

# Realizar las predicciones
y_class_pred_to_predict = pipeline_class.predict(X_to_predict)
y_demand_pred_to_predict = pipeline_demand.predict(X_to_predict)

# Agregar las predicciones al dataframe 'to_predict'
to_predict['Class'] = y_class_pred_to_predict
to_predict['Demand'] = y_demand_pred_to_predict

# Guardar las predicciones en un archivo
to_predict.to_csv('predicciones.csv', index=False)
print("Las predicciones han sido guardadas en 'predicciones.csv'.")