from fastapi import FastAPI, HTTPException, Depends
from dependencies import get_execution_manager
from services import WorkflowExecutionManager
from database import get_db  
from models import Workflow  
from sqlalchemy.orm import Session
import asyncio
import httpx

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is working!"}

@app.get("/workflows")
def get_workflows(db: Session = Depends(get_db)):
    workflows = db.query(Workflow).all()
    return {"workflows": workflows}

@app.post("/execute/{workflow_id}")
async def execute_workflow(workflow_id: str, wem: WorkflowExecutionManager = Depends(get_execution_manager)):
    try:
        response = await wem.execute_workflow(workflow_id)  # Ensure async execution
        return response
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

async def call_api():
    workflow_id = input("Enter workflow_id to execute: ")
    async with httpx.AsyncClient() as client:
        response = await client.post(f"http://127.0.0.1:8000/execute/{workflow_id}")
        print("\nAPI Response:", response.json())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
