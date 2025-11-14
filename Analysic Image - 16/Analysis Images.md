---
title: Analysis Images

---


# Analyze Images
AI-102T00-A Design and Implement a Microsoft Azure AI Solution [Cloud Slice Provided], Lab 16 (CSS)

## Step-1
- Login to the azure portal 
![image](https://hackmd.io/_uploads/HysQrNEgWl.png)
- After Login to the portal
![image](https://hackmd.io/_uploads/Bk_qrENeZl.png)
- Select Create a Resource
- In the search bar search for Computer vision, Select Computer vision and create the human resoures with the following settings
    - Subscription: `Your Azure subscription`
    - Resource group: `ResourceGroup1`
    - Region: `southeastasia`
    - Name: `vision56585498`
    - Pricing tier: `Free F0`
![image](https://hackmd.io/_uploads/rkRWv44x-g.png)
![image](https://hackmd.io/_uploads/BJvSD4Ee-g.png)


- Select the required checkboxes and create the resource.
- Wait for deployment to complete, and then view the deployment details.
- When the resource has been deployed, go to it and under the Resource management node in the navigation pane, view its Keys and Endpoint page. You will need the endpoint and one of the keys from this page in the next procedure.

- Once the Resource is completed
![image](https://hackmd.io/_uploads/S1qiJHNeWx.png)
- Use the endpoints and based key based 
![image](https://hackmd.io/_uploads/ByDMeBEgZe.png)
- Use the git command to clone the file
![image](https://hackmd.io/_uploads/rks8grEg-g.png)
# Develop an image analysis app with the Azure AI Vision SDK
```
rm -r mslearn-ai-vision -f
git clone https://github.com/MicrosoftLearning/mslearn-ai-vision
```
- Inatall all the packages
![image](https://hackmd.io/_uploads/HytuZrNlZe.png)
- Install the Azure AI Vision SDK package and other required packages by running the following commands
```
 python -m venv labenv
./labenv/bin/Activate.ps1
pip install -r requirements.txt azure-ai-vision-imageanalysis==1.0.0
```
- Enter the following command to edit the configuration file for your app
`code .env`
- In the code file, update the configuration values it contains to reflect the endpoint and an authentication key for your Computer Vision resource (copied from its Keys and Endpoint page in the Azure portal).
- After completed the code 
- We got the below resluts.
![image](https://hackmd.io/_uploads/HkHMHSNlZl.png)

![image](https://hackmd.io/_uploads/SJQHSHNeWg.png)

![image](https://hackmd.io/_uploads/HyoLSrExbx.png)

