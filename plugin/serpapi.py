from semantic_kernel.functions.kernel_function_decorator import kernel_function
from pydantic import BaseModel, Field
from typing import List
import os
from serpapi import GoogleSearch

class WebSearchInput(BaseModel):
    """Schema di input per la ricerca sul web."""
    query: str = Field(..., description="La query di ricerca.")
    num_results: int = Field(default=5, description="Il numero di risultati da restituire.")


class WebSearchResult(BaseModel):
    """Schema per un singolo risultato di ricerca."""
    title: str = Field(..., description="Il titolo del risultato.")
    url: str = Field(..., description="L'URL del risultato.")
    snippet: str = Field(..., description="Un breve estratto del risultato.")


class WebSearchOutput(BaseModel):
    """Schema di output per la ricerca sul web."""
    results: List[WebSearchResult] = Field(..., description="I risultati della ricerca.")


class WebSearchTool:
    """Tool per la ricerca sul web utilizzando SerpAPI."""
    input_schema = WebSearchInput
    output_schema = WebSearchOutput

class WebSearchPlugin:
    """
    Plugin per Semantic Kernel che implementa la ricerca web utilizzando SerpAPI.
    """
    def __init__(self):
        # Ottieni la chiave API di SerpAPI
        self.api_key = os.getenv("SERPAPI_API_KEY")
        if not self.api_key:
            raise ValueError("La variabile d'ambiente SERPAPI_API_KEY non è impostata.")
    
    @kernel_function(
        description="Cerca informazioni sul web utilizzando Google Search",
        name="search"
    )
    async def search(self, query: str, num_results: int = 5) -> WebSearchOutput:
        """
        Esegue una ricerca sul web utilizzando SerpAPI con Google Search.
        
        Args:
            query: La query di ricerca.
            num_results: Il numero di risultati da restituire.
            
        Returns:
            I risultati della ricerca.
        """
        
        # Configura i parametri di ricerca
        params = {
            "engine": "google",
            "q": query,
            "api_key": self.api_key,
            "num": num_results,
            "gl": "it",  # Località: Italia
            "hl": "it"   # Lingua: Italiano
        }
        
        # Esegui la ricerca
        search = GoogleSearch(params)
        results = search.get_dict()
        
        # Estrai i risultati organici
        organic_results = results.get("organic_results", [])
        
        # Converti i risultati nel formato richiesto
        search_results = []
        for result in organic_results:
            search_results.append(
                WebSearchResult(
                    title=result.get("title", ""),
                    url=result.get("link", ""),
                    snippet=result.get("snippet", "")
                )
            )
        
        return search_results