# Incognito

Incognito is an AWS application which can be used to create a API to redact documents. The overall goal of incognito is to make redaction easy with specified filters and a easy-to-use application. 

## Getting Started

These instructions will help you deploy incognito into an AWS stack.

### Prerequisites

What things you need to install the software and how to install them

```
Docker/Docker Desktop
AWS Account
AWS CLI
SAM CLI
pipenv
```

### Installing

1. Verify docker is running
2. Ensure your AWS CLI is configured with `aws configure` 
3. Inside your project folder run
`pipenv shell` to create your virtual environment
4. Run `sam build --use-container` to build your aws application
5. Run `sam deploy --guided` and go through the instruction to deploy your application in a stack onto your AWS account.

## Locally testing

### Quick testing

To test your application, ensure docker is running, then run `pipenv run sam local start-api` which will open up local API endpoints at localhost. 

### Line by line debugging with VSCode

Ensure these lines are at the top of your `app.py` file: 
```
import ptvsd

# Enable ptvsd on 0.0.0.0 address and on port 5890 that we'll connect later with our IDE
ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
ptvsd.wait_for_attach()
```

Add a debug configuration with this template:
```
{
    "name": "SAM CLI Python",
    "type": "python",
    "request": "attach",
    "port": 5890,
    "host": "localhost",
    "pathMappings": [
        {
            "localRoot": "${workspaceFolder}/src/",
            "remoteRoot": "/var/task"
        }
    ]
}
```
Now to run the line by line debugger with vscode run `pipenv run sam local start-api -d 5890` 
Hit your endpoint first, then run the debugger configuration. 


## Authors

* **Anderson  Chen** - (https://github.com/AChenny)
* **Kevin Vo** - (https://github.com/KevyVo)

## License

[TBA]
