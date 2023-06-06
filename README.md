# Hello World ChatGPT Plugin Example

The source code of our [Hello World ChatGPT Plugin YouTube tutorial](https://converter.app/blog/creating-your-first-chat-gpt-plugin-a-step-by-step-guide). For developing your own plugin you will need to [join the OpenAI waitlist](https://openai.com/waitlist/plugins) for plugin developments.

## Setup

In the guide we will use Vercel to automatically deploy the plugin in an elegant way. To install the required packages for this plugin in your local environment, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

## Deployment and Installation

Follow the steps below to begin the process of integrating your Hello World Chat GPT plugin:

1. **Open the OpenAI Chat Interface**: Start by navigating to the OpenAI chat interface at https://chat.openai.com.

2. **Select the 'Plugins' Model**: Look for the model drop-down menu. From the options, choose 'Plugins'. If you do not see this option, it means you may not have access yet.

3. **Open the Plugin Store**: Once you have chosen 'Plugins', the Plugin Store will be available. Click on it to open it.

4. **Initiate Development of Your Plugin**: Within the Plugin Store, you will find an option that says 'Develop your own plugin'. Click on it to get started with your plugin development.

5. **Enter Localhost URL**: At this stage, you will need to enter your server's URL. Since your server is running locally, type in `https://hello-world-chatgpt-plugin.vercel.app` and then click on 'Find manifest file'.

6. **Enter Localhost URL**: Press install and confirm that you want to install an unverified plugin. Your first ChatGPT Plugin should be ready for usage now.

**Note:** The URL in the steps above points to our deployed version of this plugin. If you want to develop it actively, you will need to replace it by your local or remote plugin URL.


