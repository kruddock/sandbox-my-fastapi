# Sandbox FastApi

A small demo using FastApi.

## Prerequisites

- Visual Studio Code with [remote containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- Docker
- (Optionally) After installing docker, get python image using this command . Doing this optional step speeds up installation.
```bash
docker pull python:3.13.2-alpine
```
- (Optionally) After installing docker, get mongo image using this command . Doing this optional step speeds up installation.
```bash
docker pull mongo:latest
```
- (Optionally) GUI to connect to mongo instance. [MongoDB Compass](https://www.mongodb.com/docs/compass/current/install) is recommended

## I did READ ME from main branch
- Click "Dev Container ..." in the left hand bottom corner of Visual Studio Code, Click "Close Remote Connections" from the contextual menu that appears.
- Compose down or destroy the __sandbox-my-fastapi_devcontainer__ stack.
- Continue to bullet item #4 below.


## Installation

- If not already, download source code.
- Open source code in Visual Studio Code.
- A prompt will appear in the right hand corner. __Dismiss or Ignore this!__
- Switch to branch __with-mongo-db__
- Make a copy of .env.example (Rename to .env)
- Open Visual Studio Code's command palette, Search and select "Dev Containers : Rebuild and Reopen in Container".
- Visual Studio Code will prompt to open in the current window or a new window. Choose accordingly
- The Containers will build and dependencies will install __(Please wait)__


## Usage

- Open a new Terminal in Visual Studio Code. The terminal should be at /api
- Run the following command
```bash
fastapi dev main.py --host="0.0.0.0"
```
- Open browser to http://localhost:9045/docs
- (Optionally) Open GUI to connect to mongo instance. See .env.example


## License

[MIT](https://choosealicense.com/licenses/mit/)
