class BaselineModel:
    def __init__(self, classifier, vectorizer):
        self.classifier = classifier
        self.vectorizer = vectorizer
        
    def fit_vectorizer(self, data):
        return self.vectorizer.fit(data)
        
    def transform_vectorizer(self, data):
        return self.vectorizer.transform(data)
        
    def fit_transform(self, data):
        return self.vectorizer.fit_transform(data)
    
    def fit_model(self, data):
        return self.classifier.fit(data)
        
    def predict(self, data):
        transformed_data = self.classifier.transform(data)
        return self.classifier.predict(transformed_data)