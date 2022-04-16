from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split


from mlflow import log_metric
import wandb
wandb.init(project='mlops')

config = wandb.config
config.learning_rate = 0.01

X, y = load_iris(return_X_y=True, as_frame= True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])
pipe.fit(X, y)
print(pipe.score(X_test, y_test))
wandb.log({'score': pipe.score(X_test, y_test)})
for i in range (10):
    wandb.log({"loss": i})


