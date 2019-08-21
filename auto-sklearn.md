# Auto-sklearn

## 1 installation
https://automl.github.io/auto-sklearn/master/installation.html
### 1.1Installing auto-sklearn
Please install all dependencies manually with:
```
curl https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt | xargs -n 1 -L 1 pip install
```
### 1.2 Anaconda installation
```
conda install gxx_linux-64 gcc_linux-64 swig
```
### 1.3 install auto-sklearn
```
pip install auto-sklearn
```
- possible fail because of pyrfr, via conda environment
    - solution:
```
conda install swig --yes
pip install  pyrfr # probably don't need this b/c it reinstalls in auto-sklearn
pip install auto-sklearn
```
## 2 Manual
https://automl.github.io/auto-sklearn/master/

## 3 Usage Example
```python
import autosklearn.classification
import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics
X, y = sklearn.datasets.load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = \
    sklearn.model_selection.train_test_split(X, y, random_state=1)
automl = autosklearn.classification.AutoSklearnClassifier()
automl.fit(X_train, y_train)
y_hat = automl.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_hat))
```
