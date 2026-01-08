from dotenv import load_dotenv
import os

load_dotenv()               #загружаем .env

app_name = os.getenv("APP_NAME")
debug = os.getenv("DEBUG")

print(app_name)
print(debug)