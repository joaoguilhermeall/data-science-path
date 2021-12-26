# Data Science Path 🎲
Lucas's Data Science Path is a way that my friend created to help me walk and learn about data and information analysis. I am very grateful for all this.

## Source and App
To run all pipeline or steps of it, you can download this repository or clone it on your machine by the follow shell command.
```sh
git clone https://github.com/joaoguilhermeall/data-science-path.git 
```

On folder of project you can call pipeline through this command:
```sh
python -m src pipeline
```

Pipelene level will run all steps that was build, such as `extract`, `transform` and `loading`.

## Kaggle Credentials
To run `pipeline` or `extract` level it is necessary to create and enter Kaggle API credentials on Environ Variables, on folder Kaggle, or download `kaggle.json` in the `keys` folder. See [Kaggle API Documentation](https://github.com/Kaggle/kaggle-api#api-credentials) for more information.

> Download `kaggle.json` in the keys folder is a more way to authenticate on Kaggle API.

Another option is download the [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database) in the `input` folder , as a file named `pima-indians-diabetes-databetes.zip`.

If Kaggle API Credentials are not loaded in any way, they will be requested by CLI.
```plaintext
Kaggle Credentials

Credentials are being requested because the configuration file was not found and the variables were not found in the environment

Enter Kaggle API Username: #your_username
Enter Kaggle API Key: #your_api_key

Log in!
```

## About
The status and TO-DO are manager on [Notion page here](https://joaoguilhermeall.notion.site/Lucas-s-Data-Science-Path-6ae0f593984f44cf90c266a43baaeefc).

