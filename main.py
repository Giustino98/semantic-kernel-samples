import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers import ask

# Carica le variabili d'ambiente dal file .env
load_dotenv()

if not os.getenv("SERPAPI_API_KEY"):
    raise ValueError("La variabile d'ambiente SERPAPI_API_KEY non è impostata. Assicurati di averla configurata nel file .env.")

# Crea l'applicazione FastAPI
app = FastAPI(
    title="Semantic Kernel API",
    description="API per interagire con agenti che utilizzano il framework Microsoft Semantic Kernel",
    version="1.0.0"
)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In produzione, specifica i domini consentiti
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Includi i router
app.include_router(ask.router, prefix="/api", tags=["api"])

# Endpoint di root
@app.get("/")
async def root():
    return {
        "message": "Benvenuto nel servizio che sfrutta Microsoft Semantic Kernel per soddisfare le tue esigenze",
        "docs": "/docs",
        "endpoints": {
            "ask": "/api/ask",
        }
    }

# Se questo file viene eseguito direttamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 