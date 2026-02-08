import logging
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("StreamingML")

def stream_data(X, y):
    for i in range(len(X)):
        yield X[i], y[i]

class OnlineScaler:
    def __init__(self):
        self.scaler = StandardScaler()
        self.logger = logging.getLogger("OnlineScaler")

    def update_and_transform(self, x):
        x = x.reshape(1, -1)
        self.scaler.partial_fit(x)
        return self.scaler.transform(x)

class OnlineClassifier:
    def __init__(self):
        self.model = SGDClassifier(
            loss="log_loss",
            learning_rate="optimal",
            random_state=42
        )
        self.initialized = False
        self.logger = logging.getLogger("OnlineClassifier")

    def update(self, x, y, classes):
        if not self.initialized:
            self.logger.info("Initializing model with first streaming sample")
            self.model.partial_fit(x, [y], classes=classes)
            self.initialized = True
        else:
            self.model.partial_fit(x, [y])

    def predict(self, X):
        return self.model.predict(X)

class StreamingTrainer:
    def __init__(self):
        self.scaler = OnlineScaler()
        self.model = OnlineClassifier()
        self.classes = np.array([0, 1])
        self.logger = logging.getLogger("StreamingTrainer")

    def train(self, X_stream, y_stream):
        self.logger.info("Starting streaming training")
        count = 0

        for x, y in stream_data(X_stream, y_stream):
            x_scaled = self.scaler.update_and_transform(x)
            self.model.update(x_scaled, y, self.classes)

            count += 1
            if count % 100 == 0:
                self.logger.info("Processed %d streaming samples", count)

        self.logger.info(
            "Streaming training completed | Total samples: %d", count
        )

def evaluate(model, scaler, X_test, y_test):
    eval_logger = logging.getLogger("Evaluation")
    eval_logger.info("Starting evaluation")

    X_scaled = scaler.scaler.transform(X_test)
    y_pred = model.predict(X_scaled)

    acc = accuracy_score(y_test, y_pred)
    eval_logger.info("Evaluation completed | Accuracy: %.4f", acc)

    return acc

def main():
    logger.info("Loading dataset")
    X, y = load_breast_cancer(return_X_y=True)
    # Split like a real production system
    X_stream, y_stream = X[:400], y[:400]
    X_test, y_test = X[400:], y[400:]

    trainer = StreamingTrainer()
    trainer.train(X_stream, y_stream)

    acc = evaluate(trainer.model, trainer.scaler, X_test, y_test)
    print(f"\nFinal Accuracy: {acc:.4f}\n")


if __name__ == "__main__":
    main()


