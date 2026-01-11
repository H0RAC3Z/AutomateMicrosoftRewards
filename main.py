from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

searches1 = ["what", "why", "when", "how", "where"]
searches2 = ["is", "are", "might", "never", "would", "should", "could", "cant", "didnt"]
searches3 = [
    # animals
    "dogs", "cats", "rats", "horses", "birds", "fish", "hamsters",
    "snakes", "lizards", "frogs", "insects", "bees", "ants",

    # food & consumables
    "donuts", "pizza", "bread", "chocolate", "cheese", "milk",
    "coffee", "energy drinks", "protein bars",

    # tech devices
    "laptops", "phones", "tablets", "computers", "desktops",
    "servers", "routers", "modems", "switches",
    "keyboards", "mice", "monitors", "printers",

    # power & hardware
    "batteries", "chargers", "power supplies", "extension cords",
    "generators", "engines", "motors", "fans",

    # vehicles & machines
    "cars", "electric vehicles", "trucks", "bikes",
    "drones", "robots", "machines",

    # software & systems
    "apps", "programs", "scripts", "algorithms", "ai systems",
    "models", "databases", "servers", "cloud services",
    "websites", "browsers", "operating systems",
    "updates", "drivers", "plugins", "extensions",

    # networks & data
    "networks", "connections", "signals", "packets",
    "requests", "responses", "sessions",

    # people & behavior
    "people", "kids", "students", "employees", "managers",
    "drivers", "teams", "users", "customers",

    # abstract things
    "arguments", "conversations", "meetings", "projects",
    "plans", "systems", "processes", "workflows"
]

searches4 = [
    # failures & issues
    "explode", "overheat", "crash", "freeze", "fail",
    "break", "stop working", "malfunction",
    "restart randomly", "shut down unexpectedly",

    # performance
    "run slowly", "run fast", "slow down", "speed up",
    "lag", "stutter", "timeout",

    # power & heat
    "consume too much power", "drain batteries",
    "lose charge", "heat up", "overload",

    # data & software problems
    "lose data", "corrupt data", "cause errors",
    "produce warnings", "throw exceptions",
    "fail silently", "behave strangely",
    "act unpredictably",

    # networking issues
    "disconnect", "lose signal", "drop connections",
    "fail to connect", "block traffic",

    # physical actions
    "spin", "jump", "vibrate", "shake",
    "move randomly", "fall over",

    # human behavior
    "argue", "panic", "complain", "make mistakes",
    "ignore warnings", "miss deadlines",

    # misc search-style endings
    "cause problems",
    "work intermittently",
    "stop responding",
    "perform poorly",
    "work as expected"
]


len1 = len(searches1)
len2 = len(searches2)
len3 = len(searches3)
len4 = len(searches4)

lenArr = [len1-1, len2-1, len3-1, len4-1]


# hard-coded searches below
# searches = [
#     "python selenium tutorial",
#     "how to automate web testing",
#     "best python libraries 2026",
#     "machine learning basics",
#     "random forest regression example",
#     "streamlit dashboard ideas",
#     "google gemini api python",
#     "web scraping with selenium",
#     "edge webdriver setup",
#     "chrome vs edge webdriver",
#     "how to use pandas dataframe",
#     "numpy array operations",
#     "scikit-learn model saving",
#     "joblib vs pickle python",
#     "python virtual environment",
#     "pip install requirements",
#     "debugging python scripts",
#     "async programming python",
#     "python http requests",
#     "rest api integration",
#     "data visualization matplotlib",
#     "seaborn vs matplotlib",
#     "sql database connection python",
#     "postgresql python tutorial",
#     "wsl networking issues",
#     "linux command line basics",
#     "windows environment variables",
#     "software testing automation",
#     "ai chatbot architecture",
#     "search engine optimization basics"
# ]

edge_options = Options()

edge_options.add_argument(r"--user-data-dir=C:\Users\horac\AppData\Local\Microsoft\Edge\User Data") # to use automated edge with profile, we have to locate user data
edge_options.add_argument("--profile-directory=Default") # default profile, could potentially be profile 1, 2, and so on
service = Service(r"C:\Users\horac\Documents\msedgedriver.exe") # explicitly defining where the webdriver executable is located

driver = webdriver.Edge(service=service, options=edge_options)
driver.get("https://www.bing.com/") # get to bing

# hard-coded searches
# for search in searches:
#     elem = driver.find_element(By.NAME, "q")
#     elem.clear()
    
#     elem.send_keys(search + Keys.ENTER)
#     time.sleep(7) # search cooldown, recommended 7-10 seconds

for i in range(30): # 30 times assuming 90 point maximum and 3 points per search
    arr = []
    prompt = ""
    for index in lenArr:
        rand = random.randint(1, index)
        arr.append(rand)
    prompt += searches1[arr[0]] + " "
    prompt += searches2[arr[1]] + " "
    prompt += searches3[arr[2]] + " "
    prompt += searches4[arr[3]]
    # wait until search bar is clickable
    elem = WebDriverWait(driver, 10).until( 
        EC.element_to_be_clickable((By.NAME, "q"))
    )
    elem.clear()
    for c in prompt: # human-like typing
        elem.send_keys(c)
        time.sleep(random.uniform(0.05, 0.15))
    elem.send_keys(Keys.ENTER)
    time.sleep(5) # search cooldown, recommended 5-7 seconds on decent wifi
driver.close()