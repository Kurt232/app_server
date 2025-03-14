# Flask Server

A Flask-based REST API server that provides GPT model interaction and file management capabilities.

## Git Tips

Enhance your workflow with these detailed Git tips:

```bash
# 1. Before pushing, update your local repository:
git fetch -p  # Fetch remote changes and prune deleted branches

# 2. If the main branch has new changes:
git checkout main
git pull      # Update your local main branch with the latest commits
git checkout your_branch
git rebase -i main  # Interactively rebase your branch to integrate changes and resolve conflicts

# 3. When starting a new feature or fix:
git checkout -b your_branch  # Create a new branch based on the updated main
# Develop your feature, then repeat step 2 to stay in sync with main
git push --set-upstream origin your_branch  # Push your branch to the remote repository

# 4. Once your changes are reviewed:
# Open a pull request on GitHub to merge your_branch into main
```

Additional tips:
- Use descriptive commit messages.
- Frequently rebase to catch conflicts early.
- Leverage branch protection rules on GitHub for quality control.
- Consider squashing commits for a cleaner history.

## Setup
1. Install dependencies:
```sh
pip install -r requirements.txt
```

2. Configure environment variables:
- Create `.env` file with:
  ```
  OPENAI_API_URL=your_openai_api_url
  OPENAI_API_KEY=your_openai_api_key
  DEEPSEEK_API_URL=your_deepseek_api_url
  DEEPSEEK_API_KEY=your_deepseek_api_key
  ```

3. Run the server with additional arguments:
```sh
python src/app.py --debug --host 0.0.0.0 --port 5000
```

see more [details](https://flask.palletsprojects.com/en/stable/tutorial/factory/#run-the-application)

## Features

### 1. GPT Integration
- **Endpoint**: `/ask`
- **Method**: POST
- **Request Format**:
  ```json
  {
    "prompt": "Your question here"
  }
  ```
- **Response**:
  ```json
  {
    "response": "GPT response content"
  }
  ```

### 2. File Management

#### Upload File
- **Endpoint**: `/upload`
- **Method**: POST
- **Content-Type**: multipart/form-data
- **Parameters**:
  - `file`: File to upload
  - `path`: Target directory path
- **Response**:
  ```json
  {
    "message": "File uploaded successfully"
  }
  ```

#### List Directory
- **Endpoint**: `/list`
- **Method**: GET
- **Query Parameters**:
  - `path`: Directory path to list
- **Response**:
  ```json
  ["file1.txt", "file2.txt", "directory1"]
  ```

#### Create Directory
- **Endpoint**: `/mkdir`
- **Method**: POST
- **Request Format**:
  ```json
  {
    "path": "desired/directory/path"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Directory created successfully"
  }
  ```

## Error Codes
- 410: No prompt provided
- 411: Unknown model specified
- 420: No file part in request
- 421: No path specified
- 422: Invalid path
- 423: Path does not exist
- 424: No selected file
- 425: Path already exists

## Todo
- [x] Add Database
- [] Add an item to distinguish IOS and Android Version.

## login on ECS
Ip: 120.25.178.24 

### login 
1. download private key in group chat.

the key file name is `dataset_app.pem`
please contact Wenjie (wduaj@cse.ust.hk) 
and move it in `~/.ssh/` 

2. Add the config in ~/.ssh/config

`chmod 400 ~/.ssh/dataset_app.pem` 

```
Host ecs 
  HostName 120.25.178.24 
  Port 22 
  User root 
  IdentityFile ~/.ssh/dataset_app.pem 
```

3. Use ssh login 
Terminal or VSCode 

## References
- [Flask File Uploading](https://flask.palletsprojects.com/en/stable/patterns/fileuploads/)
- [Flask Database](https://flask.palletsprojects.com/en/stable/tutorial/database/)
- [Run application](https://flask.palletsprojects.com/en/stable/tutorial/factory/#run-the-application)
- [MongoDB](https://www.mongodb.com/zh-cn/docs/)