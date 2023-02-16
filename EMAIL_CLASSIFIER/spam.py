import streamlit as st
import pickle
from win32com.client import Dispatch
from sklearn.feature_extraction.text import CountVectorizer
import pythoncom
pythoncom.CoInitialize()

def speak(text):
	speak=Dispatch(("SAPI.SpVoice"))
	speak.Speak(text)
	

model = pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))

def main():
	st.title("Spam Email Classification ")
	
	msg=st.text_input("Enter a text")
	if st.button("Predict"):
		data=[msg]
		vect=cv.transform(data).toarray()
		prediction=model.predict(vect)
		result=prediction[0]
		if result==1:
				st.error("This is A Spam Email")
				speak("This is A Spam Email")
		else:
				st.success("This is a ham Email")
				speak("This is A Ham  Email")
main()
