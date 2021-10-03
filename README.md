# POWER_Dips-AzureServer
### EcEcursion: Andrew Chen, Shu-Yan Cheng, Yun-Hsuan Tsai, Hao Kuan, Yi-Hsuan Lai, Ming-Yi Wei
Code for app server hosted on Microsoft Azure, written for 2021 NASA Space Apps Challenge: You Are My Sunshine.
## How To Run
### Hosting on Azure
1. Follow [this tutorial](https://docs.microsoft.com/en-us/azure/app-service/configure-language-python#container-startup-process) to configure your python app for web services.
2. Then refer to the steps of [this link](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=bash&pivots=python-framework-flask) to set up your python app and enviromnent requirements in the virtual machine.
3. Configure the fetch link in our React Native app link to that of Azure Service provides before build, the server should run properly.

### Hosting Locally
1. You server and your phone must on the same network in order to test locally. 
2. First install all the required packages. 
```
pip install -r requirements.txt
```
3. run 
```
python Server.py
```
4. You will find that the server runs on a certain IP, and then you can change the "server" varaible in App.js in our app's file into that IP. 
5. Use Expo to build your application and test it. 
6. Voila! Done. 

![messageImage_1633264095902](https://user-images.githubusercontent.com/64970325/135754719-4bcf9dd5-ee3e-4b30-a209-8301d84960fd.jpeg)

#### Due to our use of Azure student accounts our release version is currently based on local hosting
