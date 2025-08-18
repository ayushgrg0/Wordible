## Wordible

 **Wordible**: a super fast tool built with Django that breaks down any text you give. It's simplifies count, it also tells you which words appear most often, helping you get insights at a glance. 

## 🚀 Features

* Quickly count words, characters, and sentences  
* See which words show up the most with frequency rankings  
* User-friendly interface that makes text analysis effortless  
* Fast and responsive, even with large chunks of text  



## 🛠️ Setup

Installation  

**1. Clone the repository**  
```bash
https://github.com/ayushgrg0/Wordible
cd Wordible
```

**2. Create and activate virtual environment**  
```bash
#Create virtual environment  

uv venv  

#Activate on Windows  

.\venv\Scripts\activate  

#Activate on Linux/Mac  

source venv/bin/activate  
``` 

**3.Install dependencies**  

```bash
uv sync  

#Setup database 

python manage.py migrate  
``` 

**4. Start development server**  
```bash
python manage.py runserver  
``` 
