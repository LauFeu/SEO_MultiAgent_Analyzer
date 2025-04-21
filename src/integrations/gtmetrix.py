"""
Module d'intégration GTmetrix
"""
import aiohttp
from typing import Dict, Any

class GTmetrixClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://gtmetrix.com/api/2.0"
        
    async def test_url(self, url: str) -> Dict[str, Any]:
        """Lance un test GTmetrix sur une URL"""
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Basic {self.api_key}",
                "Content-Type": "application/json"
            }
            async with session.post(
                f"{self.base_url}/tests", 
                json={"url": url},
                headers=headers
            ) as response:
                return await response.json() 