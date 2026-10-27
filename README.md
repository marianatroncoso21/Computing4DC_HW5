# Diabetes Mellitus Prediction (OOP) – Computing for Data Science HW5

## Group members
- Mariana Troncoso
- Jose Luis Fernández

## Project structure
- `src/computing4dc_hw5/hw5.py`: exercises 1–3 (classes, inheritance and abstract classes)
- `src/computing4dc_hw5/loading/`: class to load the data and split it into train/test (step 6a)
- `src/computing4dc_hw5/preprocessing/`: preprocessor classes to drop and fill missing values (steps 6b, 6c)
- `src/computing4dc_hw5/features/`: feature classes with a common abstract parent (step 6d)
- `src/computing4dc_hw5/modeling/`: model class with `train` and `predict` (steps 6e, 6f)
- `data/`: dataset
- `notebooks/`: notebook that imports the classes and runs all the steps

## How to run
1. Install the environment: `uv sync`
2. Open the notebook in `notebooks/` with the project's `.venv` kernel and run all cells.