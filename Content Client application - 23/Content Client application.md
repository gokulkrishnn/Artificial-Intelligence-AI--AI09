---
title: Content Client application

---

# Content Client application 

## Develop a Content Understanding client application

## Create an Azure AI Foundry hub and project

- In a web browser, open the Azure AI Foundry portal at https://ai.azure.com and sign in using the username 
- `User1-56622114@LODSPRODMSLEARNMCA.onmicrosoft.com` and the password `V#42X2*@`. Close any tips or quick start panes that are opened the first time you sign in, and if necessary use the Azure AI Foundry logo at the top left to navigate to the home page, which looks similar to the following image (close the Help pane if it's open)


- In the browser, navigate to `https://ai.azure.com/managementCenter/allResources` and select Create new. Then choose the option to create a new AI hub resource.

![image](https://hackmd.io/_uploads/BJvQsW8gWx.png)

- n the Create a project wizard, enter a valid name for your project, and select the option to create a new hub. Then use the Rename hub link to specify a valid name for your new hub, expand Advanced options, and specify the following settings for your project:

Project: project56622114
Hub: hub56622114
Subscription: Your Azure subscription
Resource group: ResourceGroup1
Location: swedencentral

![image](https://hackmd.io/_uploads/rJZPoZLxZe.png)

![image](https://hackmd.io/_uploads/rJCcj-IgWl.png)

# Use the REST API to create a Content Understanding analyzer

- **In the cloud shell pane, enter the following commands to clone the GitHub repo containing the code files for this exercise (type the command, or copy it to the clipboard and then right-click in the command line and paste as plain text):**

```
rm -r mslearn-ai-info -f
git clone https://github.com/microsoftlearning/mslearn-ai-information-extraction mslearn-ai-info
```

- After the repo has been cloned, navigate to the folder containing the code files for your app

- Enter the following command to edit the configuration file that has been provided

```
python -m venv labenv
./labenv/bin/Activate.ps1
pip install -r requirements.txt
```

- 

![image](https://hackmd.io/_uploads/HJzZJMUlbe.png)

![image](https://hackmd.io/_uploads/rkRJxz8l-l.png)

![image](https://hackmd.io/_uploads/SyKtgGUxWg.png)

![image](https://hackmd.io/_uploads/SkbDbM8eWx.png)

![image](https://hackmd.io/_uploads/HJ_1MzIlbg.png)

![image](https://hackmd.io/_uploads/HynbzfIgZg.png)

![image](https://hackmd.io/_uploads/Hke7ff8xZx.png)

![image](https://hackmd.io/_uploads/Sk3ZLfUxbl.png)


![image](https://hackmd.io/_uploads/S1cyUGIxWl.png)

