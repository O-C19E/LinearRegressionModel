# Manufacturing Output Prediction (Linear Regression)

Predicts `Parts_Per_Hour` from machine settings using linear regression.
Test R² ≈ 0.91, MAE ≈ 2.8 parts/hour.

## Files
- `CapstoneProject1_LinearRegression.ipynb` – full analysis
- `train_model.py` – rebuilds and saves the model
- `app.py` – Streamlit app
- `lin_pipeline.joblib` – trained pipeline

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
Python 3.12. The model file is sensitive to the scikit-learn version, so use
the pinned version in `requirements.txt` (or run `python train_model.py` to retrain).
