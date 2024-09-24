# cold-email-generator-and-sender

1)saaki.ai is an AI Consulting Firm,company has employees skilled in variety of software fields.  
2)the project is to build a model which generates and send cold emails to other companies stating them not to hire new employess instead have a deal with saaki.ai to use there employees under contract based.  
3)model takes the url, reads the content, it matches the skills mentioned with DB where the saaki.ai's info is present.  
4) llama-3.1-70b-versatile llm is used to generate cold emails and Chroma DB is used to store saaki.ai's portfolio links.  
5)the model produces the cold email giving the links to saaki.ai's portfolio in required software field, and showing ability of saaki.ai.  
6)the model will generate as many cold emails as the job applications are present in provided url.so give specific job url.  
7)the project will automatically send email to the clent after generating it.  



INSTRUCTIONS:
1)create your conda virtural environment venv.  
2)activate venv.  
3)install all the packages present in requirements.txt  
4)copy paste your GROQ api key in .env file.  
5)create an app password for Gmail in your google account.  
6)enter sender and receiver email and app password of sender in .env file.  
7)now run- streamlit run main.py   
8)a default link is given-this may not work in future as the job posting may get removed-so use your own link.  
9)go to any job application page-in careers of any company-copy the url and paste it in our streamlit website.  
10)some suggested companies for job application urls-(apple,nike,google)  
11)also there is a section to enter the receiver email.enter client email to directly send an email to the client. a default mail is given already.  
12)enter submit to generate and send email to the client.  

See the video below for working...
https://drive.google.com/file/d/1ep3R8NRJTAr91aXq-BCs1EEt0-grraDv/view?usp=sharing
