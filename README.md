# Semantic Kernel API

Un'API basata su FastAPI che utilizza Microsoft Semantic Kernel per creare un agente intelligente in grado di rispondere a domande utilizzando ricerche web in tempo reale.

## Descrizione

Questo progetto implementa un servizio web che sfrutta il framework Microsoft Semantic Kernel per creare un agente AI in grado di:

- Rispondere a domande in linguaggio naturale
- Cercare informazioni sul web utilizzando SerpAPI
- Integrare modelli linguistici locali tramite Ollama

L'applicazione è costruita con FastAPI e offre un endpoint REST per interagire con l'agente.

## Requisiti

- Python 3.8+
- Ollama installato localmente (per l'esecuzione di modelli LLM)
- Chiave API SerpAPI (per le ricerche web)

## Installazione

1. Clona il repository:
   ```
   git clone <url-repository>
   cd semantic-kernel-samples
   ```

2. Crea e attiva un ambiente virtuale:
   ```
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Installa le dipendenze:
   ```
   pip install -r requirements.txt
   ```

4. Configura le variabili d'ambiente:
   - Crea un file `.env` nella directory principale (o modifica quello esistente)
   - Aggiungi la tua chiave API SerpAPI:
     ```
     SERPAPI_API_KEY=la_tua_chiave_api
     OLLAMA_BASE_URL=http://localhost:11434/v1
     OLLAMA_MODEL=llama3.2:latest
     ```

5. Assicurati che Ollama sia in esecuzione e che il modello specificato sia disponibile.

## Avvio dell'applicazione

Per avviare l'applicazione in modalità sviluppo:

```
uvicorn main:app --reload
```

L'API sarà disponibile all'indirizzo: http://localhost:8000

La documentazione interattiva (Swagger UI) sarà disponibile all'indirizzo: http://localhost:8000/docs

## Struttura del progetto

```
semantic-kernel-samples/
├── core/                  # Logica principale dell'applicazione
│   └── agent.py           # Implementazione dell'agente Semantic Kernel
├── dependencies/          # Gestione delle dipendenze
│   └── dependencies.py    # Provider per le dipendenze FastAPI
├── models/                # Modelli di dati
│   └── ask_model.py       # Modelli per le richieste e risposte
├── plugin/                # Plugin per Semantic Kernel
│   └── serpapi.py         # Plugin per la ricerca web con SerpAPI
├── routers/               # Router FastAPI
│   └── ask.py             # Endpoint per le domande all'agente
├── .env                   # Variabili d'ambiente
├── main.py                # Punto di ingresso dell'applicazione
└── requirements.txt       # Dipendenze Python
```

## Utilizzo dell'API

### Endpoint principale: `/api/ask`

**Metodo**: POST

**Payload**:
```json
{
  "question": "La tua domanda qui"
}
```

**Risposta**:
```json
{
  "answer": "La risposta dell'agente"
}
```

### Esempio di utilizzo con curl

```bash
curl -X POST "http://localhost:8000/api/ask" \
     -H "Content-Type: application/json" \
     -d '{"question":"Quali sono le ultime notizie su Microsoft?"}'
```

## Tecnologie utilizzate

- **FastAPI**: Framework web ad alte prestazioni
- **Microsoft Semantic Kernel**: Framework per l'integrazione di AI e LLM
- **Ollama**: Esecuzione locale di modelli linguistici
- **SerpAPI**: API per ricerche web
- **Pydantic**: Convalida dei dati e serializzazione

## Licenza

[Inserire informazioni sulla licenza]

## Contatti

[Inserire informazioni di contatto] 