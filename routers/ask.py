from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from dependencies.dependencies import get_websearch_agent
from core.agent import SemanticKernelAgent
from models.ask_model import AskRequest, AskResponse
import logging
router = APIRouter()

@router.post("/ask", response_model=AskResponse)
async def ask_question(
    request: AskRequest,
    agent: SemanticKernelAgent = Depends(get_websearch_agent)
):
    """
    Endpoint per fare una domanda all'agente info e ricevere una risposta.
    """
    try:
        answer = await agent.ask(request.question)
        logging.info(f"Risposta: {answer.value[0].content}")
        return AskResponse(answer=answer.value[0].content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore durante l'elaborazione della domanda: {str(e)}")
