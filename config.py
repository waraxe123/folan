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

SESSION = getenv("SESSION", "BQAeNGDW0aEmcKBEfnczciF0jduxx5ggOUhJ9mPef16pCqcGYyaIDsgj40wPiTIj-_nZGHtxd3AsW1lfVIeoB7oOJm3w26YZuXrTBYkvHUbplKe-Ph72zxv9fQ-4ccSsOIJRDx63UIC5BSZhrtTu4NsWsBI-zKTuZGc28rBPrf4fQOZ3HlkZzsED7aJtuD1XEK90D_VFqsDBYz21liCFNXr2CMaVOzYRx1MptWSEFlsIDjYZFoPZAsfc-pVb6i47kYXJQuNSTI1164dUm4qGuUBiPU68nInlgQVhZy31EYqSw0GtXBSV24nw6DNpm0FR1OFxdNhGo1Z36Vfs5us8a5YbS93TIAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/yahkenatipu")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kinoshitaee")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6259531153").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
