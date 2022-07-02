from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump, load
import mlflow

X, y = load_iris(return_X_y = True, as_frame = True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

pipe = Pipeline(steps = [
    ('model', RandomForestClassifier(n_estimators=100, max_depth=16))
])

with mlflow.start_run():
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 16)
    mlflow.log_metric("acc", acc)
    mlflow.sklearn.log_model(pipe, "model")



