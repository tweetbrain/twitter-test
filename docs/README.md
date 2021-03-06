# twitter-test
testing twitter's api

## Installation

**Clone repository**
```
git clone https://github.com/tweetbrain/twitter-test
```

**Navigate into repository**
```
cd twitter-test
```

**🐍 Create Python virtual environment**

There are a good amount of depencies for this project -- it will be good practice to use a virtual environment, albeit not necessary.

On macOS and Linux:
```
python3 -m virtualenv env
```

On Windows:
```
python -m venv env
```
The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it env.


**✅ Activate virtual environment**

On macOS and Linux:
```
source env/bin/activate
```

On Windows Command Line:
```
.\env\Scripts\activate.bat
```

One Windows Powershell
```
.\env\Scripts\activate.ps1
```

**Install dependencies**
```
python -m pip install -r requirements.txt
```

**Paste secrets.json**
Within the repo folder, paste the secrets.json that I sent on the discord chat.

**Run example**
This will get the tweets of Montell Fish (Lo-Fi artist)
```
python twitter_test.py
```
