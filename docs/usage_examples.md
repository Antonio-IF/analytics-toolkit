# Ejemplos de Uso del Data Science Toolkit

## Instalación

```bash
pip install -r requirements.txt
```

## Uso Básico

### 1. Análisis Exploratorio de Datos

```python
from src.data_analysis.eda import EDA
from src.data_analysis.visualization import Visualization

# Crear instancia de EDA
eda = EDA()

# Analizar dataset
report = eda.analyze(dataframe)

# Generar visualizaciones
viz = Visualization()
viz.create_summary_plots(dataframe)
```

### 2. Pipeline ETL

```python
from src.data_engineering.pipeline import ETLPipeline

# Configurar pipeline
pipeline = ETLPipeline(
    source="database",
    destination="data_warehouse"
)

# Ejecutar pipeline
pipeline.run()
```

### 3. Machine Learning

```python
from src.machine_learning.models import MLModels
from src.machine_learning.preprocess import Preprocessor

# Preprocesar datos
preprocessor = Preprocessor()
X_processed = preprocessor.fit_transform(X)

# Entrenar modelo
model = MLModels()
model.train(X_processed, y)
```

## Notebooks de Ejemplo

- `eda_examples.ipynb`: Ejemplos de análisis exploratorio
- `ml_models_demo.ipynb`: Demostración de modelos ML
- `etl_pipeline_demo.ipynb`: Ejemplos de pipelines ETL
