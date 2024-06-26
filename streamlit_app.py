import streamlit as st
from simpletransformers.question_answering import QuestionAnsweringModel
import os

# Modeli yükle
model_path = 'https://drive.google.com/drive/folders/1lpQOhb9hUccJzeSJN8MQ5EWx_4V6cOLj?usp=sharing'

if not os.path.exists(model_path):
    st.error("Model path does not exist. Please check the path and try again.")
else:
    model = QuestionAnsweringModel('bert', model_path)

    # Soru cevaplama işlevi
    def answer_question(context, question):
        answers, probabilities = model.predict([
            {
                'context': context,
                'qas': [
                    {'question': question, 'id': '0'}
                ]
            }
        ])
        return answers[0]['answer']

    # Streamlit uygulaması
    st.title('Simple Viewer - Soru Cevaplama')

    context = st.text_area('Bağlam (Context)', 'Buraya metin girin...')
    question = st.text_input('Soru', 'Buraya soru girin...')

    if st.button('Cevapla'):
        answer = answer_question(context, question)
        st.write('Cevap:', answer)
