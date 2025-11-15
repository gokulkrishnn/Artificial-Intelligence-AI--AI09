---
title: Choose and deploy a language model

---

# Choose and deploy a language model

The Azure AI Foundry model catalog serves as a central repository where you can explore and use a variety of models, facilitating the creation of your generative AI scenario.

In this exercise, you'll explore the model catalog in Azure AI Foundry portal, and compare potential models for a generative AI application that assists in solving problems.

- Go The Azure Foundary potal logined we able to see like this portal
![image](https://hackmd.io/_uploads/rkpJyQUxWl.png)

In the home page, in the Explore models and capabilities section, search for the gpt-4o model; which we'll use in our project.

In the search results, select the gpt-4o model to see its details.

Read the description and review the other information available on the Details tab.

![image](https://hackmd.io/_uploads/B17uzX8lbx.png)

On the gpt-4o page, view the Benchmarks tab to see how the model compares across some standard performance benchmarks with other models that are used in similar scenarios.

![image](https://hackmd.io/_uploads/rkh_7QLg-x.png)


![image](https://hackmd.io/_uploads/rkaK7QIlWx.png)


- Use the back arrow (←) next to the gpt-4o page title to return to the model catalog.

- Search for Phi-4-mini-instruct and view the details and benchmarks for the Phi-4-mini-instruct model.

![image](https://hackmd.io/_uploads/BJIyE7UxWe.png)

## Compare models

You've reviewed two different models, both of which could be used to implement a generative AI chat application. Now let's compare the metrics for these two models visually.

- Use the back arrow (←) to return to the model catalog.

- Select Compare models. A visual chart for model comparison is displayed with a selection of common models.

![image](https://hackmd.io/_uploads/ryHXI78e-g.png)

- In the Models to compare pane, note that you can select popular tasks, such as question answering to automatically select commonly used models for specific tasks.

- Use the Clear all models (🗑) icon to remove all of the pre-selected models.

- Use the + Model to compare button to add the gpt-4o model to the list. Then use the same button to add the Phi-4-mini-instruct model to the list.

- Review the chart, which compares the models based on Quality Index (a standardized score indicating model quality) and Cost. You can see the specific values for a model by holding the mouse over the point that represents it in the chart.

![image](https://hackmd.io/_uploads/H1Q0wXUgbe.png)


- In the X-axis dropdown menu, under Quality, select the following metrics and observe each resulting chart before switching to the next:

    - Accuracy
    - Quality index

- Based on the benchmarks, the gpt-4o model looks like offering the best overall performance, but at a higher cost.

- In the list of models to compare, select the gpt-4o model to re-open its benchmarks page.

- In the page for the gpt-4o model page, select the Overview tab to view the model details.

## Create an Azure AI Foundry project
To use a model, you need to create an Azure AI Foundry project.

- At the top of the gpt-4o model overview page, select Use this model.

- When prompted to create a project, enter `Project56623773` and expand Advanced options.

- In the Advanced options section, specify the following settings for your project:

Azure AI Foundry resource: Project56623773-resource
Subscription: Your Azure subscription
Resource group: ResourceGroup1
Region: eastus2

* Some Azure AI resources are constrained by regional model quotas. In the event of a quota limit being exceeded later in the exercise, there's a possibility you may need to create another resource in a different region.

- Select Create and wait for your project to be created. If prompted, deploy the gpt-4o model using the Global standard deployment type and customize the deployment details to set a Tokens per minute rate limit of 50K (or the maximum available if less than 50K).

![image](https://hackmd.io/_uploads/HytX_QLxZl.png)

![image](https://hackmd.io/_uploads/HyNuOQIx-l.png)

# Chat with the gpt-4o model

- Now that you have a model deployment, you can use the playground to test it.

- In the chat playground, in the Setup pane, ensure that your gpt-4o model is selected and in the Give the model instructions and context field, set the system prompt to 
-` You are an AI assistant that helps solve problems`.

- Select Apply changes to update the system prompt.

- In the chat window, enter the following query

![image](https://hackmd.io/_uploads/B1dTqXIxWx.png)

![image](https://hackmd.io/_uploads/BkHZoXUxWl.png)

![image](https://hackmd.io/_uploads/BJ7BiXLlWx.png)

- View the response. Then, enter the following follow-up query:



![image](https://hackmd.io/_uploads/rkmqsQLeZe.png)

![image](https://hackmd.io/_uploads/SkhijQUe-g.png)


##  Deploy another model

When you created your project, the gpt-4o model you selected was automatically deployed. Let's deploy the *Phi-4-mini-instruct model you also considered.

- In the navigation bar on the left, in the My assets section, select Models + endpoints.

- In the Model deployments tab, in the + Deploy model drop-down list, select Deploy base model. Then search for Phi-4-mini-instruct and confirm you selection.

- Agree to the model license.

- Deploy a Phi-4-mini-instruct model with the following settings:

    - Deployment name: A valid name for your model deployment
    - Deployment type: Global Standard
    - Deployment details: Use the default settings

- Wait for the deployment to complete.

![image](https://hackmd.io/_uploads/HkUta7Igbl.png)

# Chat with the Phi-4 model

Now let's chat with the new model in the playground.

- In the navigation bar, select Playgrounds. Then select the Chat playground.

- In the chat playground, in the Setup pane, ensure that your Phi-4-mini-instruct model is selected and in the chat box, provide the first line as System message: You are an AI assistant that helps solve problems. (the same system prompt you used to test the gpt-4o model, but since there is no system message setup, we're providing it in the first chat for context.)

- On a new line in the chat window (below your system message), enter the following query

![image](https://hackmd.io/_uploads/Sk5a6m8eZl.png)

![image](https://hackmd.io/_uploads/SkMXCm8xbe.png)

![image](https://hackmd.io/_uploads/Hy_wA78gbx.png)

![image](https://hackmd.io/_uploads/BJMcCQIgbe.png)
