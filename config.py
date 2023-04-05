from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "20143520"))
API_HASH = getenv("API_HASH", "a61010e8ebf2ba6f697c1ffb5541b7fa")

BOT_TOKEN = getenv("BOT_TOKEN", "6105301345:AAF6AC__TFU9lQo46YRbCZ1Leg0ntgJzrlE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID", "6259531153"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/fce68da3f21aa5a6a9fbb.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BQBH18-2yb8djAkdksuxkjmczpx8m2uwnkSR0lDPweQDxte3iBuYRfvB1LUn7FvmssNlG_F3PmIMQWlEp_ctGyS9e6pBDDh8HZ3mXCfdFnfuXNFNkPdPAgYvNcur7bY8jOh8XUJ8ZBKjn9gDIWz5gxh5iq-vu_v-UI5mwj0mpuhHhmwoDsqbxUdpNk4zqXKMZUOc-GJdBAeM7fGskH21WoVTXd6UoJa45G_fj0Kz8l2F5Be6bJpnVh-6xAcEvkxIfSflWms6cYYLvNO4LK5-XTRGNmIwL1s76PauRiG3yTsuFau5K8YzshekauX5tBW-GRY53PRVBv6jRBDCYsWH7mUiS93TIAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kinoshitasupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kinoshitaee")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6259531153").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
