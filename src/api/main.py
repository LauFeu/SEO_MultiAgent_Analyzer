from fastapi import FastAPI, HTTPException
from typing import Dict, Any
from ..agent.seo_agent import SEOAgent
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI(title="SEO MultiAgent Analyzer")

# Configuration de la base de données
DATABASE_URL = "sqlite+aiosqlite:///./seo_analysis.db"
engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

@app.post("/analyze")
async def analyze_website(url: str) -> Dict[str, Any]:
    """
    Point d'entrée principal pour l'analyse SEO
    """
    async with AsyncSessionLocal() as session:
        agent = SEOAgent(session)
        try:
            results = await agent.analyze_website(url)
            return results
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """
    Vérifie l'état de santé de l'API
    """
    return {"status": "healthy"} 