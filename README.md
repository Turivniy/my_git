# my_git test

## How to install
### Install pre-conditions (Ubuntu 16.04):
```
apt-get install git
sudo apt-get install python-pip python-dev build-essential
sudo pip install virtualenv virtualenvwrapper
sudo pip install --upgrade pip
```
### Execute following commands in terminal:

```
git clone https://github.com/Turivniy/my_git.git
cd my_git
virtualenv .venv
. .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## How to run tests

Before launching you should export some environment variables:

### Execute following commands in terminal:

```
export USERNAME="you git username"
export PASSWORD="you git password"
```

### Typical commands to launch test in different ways:

**To launch unittests tests run:**

```
python -m unittest unittests
```

**To launch functional tests run:**

```
python -m unittest functional
```