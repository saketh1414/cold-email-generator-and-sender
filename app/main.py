import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import os
from chains import Chain
from portfolio import Portfolio
from utils import clean_text,send_email
from dotenv import load_dotenv
load_dotenv()


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-31388")
    receiver_email=st.text_input("Enter receiver email:",value=os.getenv("RECEIVER_EMAIL"))
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(f"Subject: {email[0]}\n\n{email[1]}", language='markdown')
                send_email(receiver_email,email[0],email[1])
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)

