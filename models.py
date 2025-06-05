from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

class BaseModel:
    def __init__(self, model):
        self.model = model

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))
        return y_pred


class LogisticModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(LogisticRegression(**kwargs))


class DecisionTreeModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(DecisionTreeClassifier(**kwargs))

