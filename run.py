from config import DevConfig,ProdConfig
from app import create_app


app=create_app(ProdConfig)
# app.run()