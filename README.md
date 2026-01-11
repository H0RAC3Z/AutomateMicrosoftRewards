## Quick Start

WILL ONLY RUN IF ALL MICROSOFT EDGE PROGRAMS CLOSED, BACKGROUND TASKS COUNT

### Requirements
- Preferrably python 3.14 or 3.13 for best compatibility as of this commit.
- Pip.
- Edge webdriver. Will install the zip, extract the executable.

### 1. Clone the Repository
Clone the project to your local machine.

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 4. Install dependencies
```bash
pip install selenium
```

### 5. Modify user data file location, profile if needed, and webdriver executable location
Change the strings within the following lines to match your file folders/locations:
```python
edge_options.add_argument(r"--user-data-dir=C:\Users\horac\AppData\Local\Microsoft\Edge\User Data") # to use automated edge with profile, we have to locate user data
edge_options.add_argument("--profile-directory=Default") # default profile, could potentially be profile 1, 2, and so on
service = Service(r"C:\Users\horac\Documents\msedgedriver.exe") # explicitly defining where the webdriver executable is located
```

### 6. Run
```bash
python main.py
```


