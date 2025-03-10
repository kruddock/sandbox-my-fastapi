# Sandbox FastApi

A small demo using FastApi.

## Prerequisites

- Visual Studio Code with [remote containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- Docker
- (Optionally) After installing docker, get python image using this command . Doing this optional step speeds up installation.
```bash
docker pull python:3.13.2-alpine
```
## Installation

- Download source code.
- Open source code in Visual Studio Code.
- A prompt will appear in the right hand corner. Click "Reopen in Container".
- If the prompt does not appear, open Visual Studio Code's command palette, Search and select "Dev Containers : Rebuild and Reopen in Container".
- Visual Studio Code will prompt to open in the current window or a new window. Choose accordingly
- The Containers will build and dependencies will install __(Please wait)__

## Usage

- Open a new Terminal in Visual Studio Code. The terminal should be at /api
- Run the following command
```bash
fastapi dev main.py --host="0.0.0.0"
```
- Open browser to http://localhost:9045/docs


## License

[MIT](https://choosealicense.com/licenses/mit/)
