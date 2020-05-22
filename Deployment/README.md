![image](https://user-images.githubusercontent.com/56355704/82323128-3c8afb80-99f5-11ea-836d-fcb5ccb11930.png)  
<hr> 

<h1>Create your Heroku account</h1>  

### **[LOCATION]**  FLASK application folder and run the following commands:  
mkdir web_app  
mv -t web_app data worldbankapp wrangling_scripts worldbank.py   
### **[CREATE]** virtual enviroment
conda update python  
python3 -m venv worldbankvenv  
source worldbankenv/bin/activate  
pip install flask pandas plotly gunicorn  
### [HEROKU] login in it  
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh  
https://devcenter.heroku.com/articles/heroku-cli#standalone-installation  
heroku --version  
heroku login    
touch Procfile  
web gunicorn worldbank:app    **<-- inside Procfile**  
### [run] pip freeze to save a list of modules in your environment in requirements.txt  
pip freeze > requirements.txt  
git init  
git add .   
git commit -m "First Commit"  

### [PUSH] your repo to master  
**my-app-name <-- this should be unique**  
heroku create my-app-name  
git remote -v  
git push heroku master  

