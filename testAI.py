import streamlit as st
import pickle
from sklearn.datasets import load_iris

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


iris = load_iris()
X, y =iris.data, iris.target

print(X.shape)
#print(y.shape)

X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.2)
print(X_train.shape)
print(y_train.shape)

clf=RandomForestClassifier()
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))

print('Saving model to pickle file')
pickle.dump(clf, open("iris_model.pkl", 'wb'))



# Load the trained model
clf = pickle.load(open('iris_model.pkl', 'rb'))

# Sidebar for user input
st.sidebar.title('Iris Classifier')
sepal_length = st.sidebar.slider('Sepal Length', 4.0, 8.0, 5.0)
sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider('Petal Length', 1.0, 7.0, 4.0)
petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 1.0)

# Make predictions
prediction = clf.predict([[sepal_length, sepal_width, petal_length, petal_width]])

# Display prediction
st.write('## Prediction:')
st.write(iris.target_names[prediction[0]])
