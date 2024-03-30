from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("7603458"))
API_HASH = getenv("910e420f1f74f40305a684a331dade35")
BOT_TOKEN = getenv("7117010157:AAH_sS3WVBQA6wYrclWFLZGP7c6v7KZ3DMk")

MONGO_DB_URI = getenv("mongodb+srv://BashBot02:BashBot@bashbot.8uzlxey.mongodb.net/?retryWrites=true&w=majority")

INDEX_ID = int(getenv("-1001433720912"))
UPLOADS_ID = int(getenv("-1001438374709"))

STATUS_ID = int(getenv("-1001438374709"))
SCHEDULE_ID = int(getenv("-1001438374709"))

CHANNEL_TITLE = getenv("Anime_Bash")
INDEX_USERNAME = getenv("@All_new_Doraemon_movies")
UPLOADS_USERNAME = getenv("@Ongoing_Bash")
