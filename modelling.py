from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns

class BaseModel:
    def __init__(self, model):
        self.model = model

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test, plot_roc=False):
        y_pred = self.predict(X_test)
        y_proba = self.model.predict_proba(X_test)[:, 1] if hasattr(self.model, "predict_proba") else None

        print("Classification Report:\n", classification_report(y_test, y_pred))
        
        print("\nConfusion Matrix:")
        conf_matrix = confusion_matrix(y_test, y_pred)
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
        plt.title("Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.show()

        if y_proba is not None:
            roc_score = roc_auc_score(y_test, y_proba)
            print(f"\nROC AUC Score: {roc_score:.2f}")

            if plot_roc:
                fpr, tpr, thresholds = roc_curve(y_test, y_proba)
                plt.figure(figsize=(8, 6))
                plt.plot(fpr, tpr, label=f'ROC AUC = {roc_score:.2f}')
                plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
                plt.xlabel("False Positive Rate")
                plt.ylabel("True Positive Rate")
                plt.title("ROC Curve")
                plt.legend()
                plt.grid(True)
                plt.show()

        def predict_proba(self, X_test):
        # Expose predict_proba from the underlying model, if it exists
            if hasattr(self.model, "predict_proba"):
                return self.model.predict_proba(X_test)
            else:
                raise AttributeError(f"{self.model.__class__.__name__} does not support predict_proba")
class LogisticModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(LogisticRegression(**kwargs))


class DecisionTreeModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(DecisionTreeClassifier(**kwargs))
