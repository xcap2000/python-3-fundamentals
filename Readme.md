# Python 3 fundamentals

## Project dependencies

```bash
$ pip install pytest
$ pip install jupyter
$ pip install smartsheet-python-sdk
```

## Fields From Jira

You can use the play button to run the application on any file, you can run using debugger (se launch.json) or just:

```bash
$ python hello.py
```

## Python Virtual Environments


After cloning this project create a new virtual environment:

```
On vscode
1 - Type ctrl+p
2 - Select "Python: Select Interpreter"
3 - Select "Create Virtual Environment"
```

or

```
$ python -m venv .venv
$ source ./.venv/bin/activate
```

And install the packages:

```bash
$ pip install -r requirements.txt 
```

When installing a new package make sure to update the package requirements:

```bash
$ pip freeze > requirements.txt
```

To deactivate an environment just do:

```bash
$ deactivate
```

## ChatGPT Ask

```
Please write a python 3 application that will organize the files on your desktop into subfolders based on file
extensions such as images, documents, and zip archives.
```

## References

```
https://docs.pytest.org/en/8.2.x/index.html
https://code.visualstudio.com/docs/python/testing
https://sentry.io/answers/what-is-init-py-for-in-python/
https://stackoverflow.com/questions/448271/what-is-init-py-for
https://superuser.com/questions/828737/run-python-scripts-without-explicitly-invoking-python
https://stackoverflow.com/questions/13187641/run-python-programs-without-opening-a-separate-shell
https://chatgpt.com/
```