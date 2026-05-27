import threading
import time
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import uvicorn
from main import app


def iniciar_servidor():

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )


def esperar_servidor():

    for _ in range(10):

        try:

            requests.get(
                "http://127.0.0.1:8000/docs"
            )

            return

        except:

            time.sleep(1)


def test_compra_e2e():

    servidor = threading.Thread(
        target=iniciar_servidor,
        daemon=True
    )

    servidor.start()

    esperar_servidor()

    options = Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        options=options
    )

    driver.get(
        "http://127.0.0.1:8000/docs"
    )

    assert "FastAPI" in driver.title

    driver.quit()