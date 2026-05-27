import pytest
import os
import sqlite3
import sys
from pathlib import Path
from fastapi.testclient import TestClient


# adiciona a pasta raiz do projeto ao PATH
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

os.environ["DB_PATH"] = "test.db"

from main import app, init_db


@pytest.fixture
def db():

    if os.path.exists("test.db"):
        os.remove("test.db")

    init_db()

    conn = sqlite3.connect("test.db")

    yield conn

    conn.close()

    if os.path.exists("test.db"):
        os.remove("test.db")


@pytest.fixture
def client(db):

    yield TestClient(app)