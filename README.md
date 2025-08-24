# Data Science Toolkit

Un framework modular y extensible para análisis de datos, machine learning y pipelines ETL.

## 🚀 Características

- **Data Engineering**: Pipelines ETL automatizados y escalables
- **Data Analysis**: Análisis exploratorio automático y visualizaciones interactivas
- **Machine Learning**: Preprocesamiento, entrenamiento y evaluación de modelos
- **Modular**: Arquitectura flexible que permite usar solo lo que necesites
- **Extensible**: Fácil de extender con nuevos extractores, transformadores y modelos

## 📁 Estructura del Proyecto

```
data-science-toolkit/
│
├── data/                          # Datos de ejemplo o tests
│   ├── raw/                       # Datos sin procesar
│   ├── processed/                 # Datos limpios/listos
│   └── external/                  # Fuentes externas (APIs, SQL dumps)
│
├── notebooks/                     # Jupyter Notebooks para demos o pruebas
│   ├── eda_examples.ipynb
│   ├── ml_models_demo.ipynb
│   └── etl_pipeline_demo.ipynb
│
├── src/                           # Código principal del framework
│   ├── data_engineering/          # ETL, pipelines y automatizaciones
│   ├── data_analysis/             # EDA y visualización
│   ├── machine_learning/          # Modelos y entrenamiento
│   └── utils/                     # Funciones auxiliares
│
├── tests/                         # Tests unitarios y de integración
├── docs/                          # Documentación del proyecto
├── requirements.txt               # Dependencias del proyecto
├── setup.py                       # Para empaquetar como librería
└── README.md                      # Esta guía
```

## 🛠️ Instalación

### Requisitos

- Python 3.8+
- pip

### Instalación desde el código fuente

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/data-science-toolkit.git
cd data-science-toolkit

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Instalar en modo desarrollo
pip install -e .
```

## 📖 Uso Rápido

### Análisis Exploratorio de Datos

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

### Pipeline ETL

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

### Machine Learning

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

## 🧪 Testing

```bash
# Ejecutar todos los tests
pytest

# Con cobertura
pytest --cov=src

# Tests específicos
pytest tests/test_eda.py
```

## 📚 Documentación

- [Arquitectura](docs/architecture.md) - Diseño del sistema
- [Ejemplos de Uso](docs/usage_examples.md) - Guías prácticas
- [Roadmap](docs/roadmap.md) - Plan de desarrollo

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🗺️ Roadmap

Ver [docs/roadmap.md](docs/roadmap.md) para el plan de desarrollo detallado.

## 📞 Contacto

- Autor: Tu Nombre
- Email: tu.email@ejemplo.com
- Proyecto: [https://github.com/tu-usuario/data-science-toolkit](https://github.com/tu-usuario/data-science-toolkit)
