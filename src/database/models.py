from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Website(Base):
    __tablename__ = "websites"
    
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_analyzed = Column(DateTime, nullable=True)
    
    seo_data = relationship("SEOData", back_populates="website")
    keywords = relationship("Keyword", back_populates="website")

class SEOData(Base):
    __tablename__ = "seo_data"
    
    id = Column(Integer, primary_key=True)
    website_id = Column(Integer, ForeignKey("websites.id"))
    analyzed_at = Column(DateTime, default=datetime.utcnow)
    metrics = Column(JSON)
    recommendations = Column(JSON)
    
    website = relationship("Website", back_populates="seo_data")

class Keyword(Base):
    __tablename__ = "keywords"
    
    id = Column(Integer, primary_key=True)
    website_id = Column(Integer, ForeignKey("websites.id"))
    keyword = Column(String, index=True)
    search_volume = Column(Integer, nullable=True)
    difficulty = Column(Float, nullable=True)
    position = Column(Integer, nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow)
    
    website = relationship("Website", back_populates="keywords")

class AgentMemory(Base):
    __tablename__ = "agent_memory"
    
    id = Column(Integer, primary_key=True)
    context = Column(String)
    observation = Column(JSON)
    action_taken = Column(String)
    result = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow)
    importance_score = Column(Float, default=1.0) 