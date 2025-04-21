from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Configuration OpenAI
    OPENAI_API_KEY: str
    
    # Configuration Base de données
    DATABASE_URL: str = "sqlite+aiosqlite:///./seo_agent.db"
    
    # Configuration Elasticsearch
    ELASTICSEARCH_HOST: str = "localhost"
    ELASTICSEARCH_PORT: int = 9200
    
    # Configuration du moteur de recherche
    SEARCH_RESULT_LIMIT: int = 10
    SEARCH_MIN_SCORE: float = 0.5
    
    # Configuration de l'agent
    AGENT_MEMORY_LIMIT: int = 1000
    AGENT_TEMPERATURE: float = 0.7
    
    class Config:
        env_file = ".env"

settings = Settings() 