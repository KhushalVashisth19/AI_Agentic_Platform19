from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Workflow
from database import SessionLocal

class WorkflowFetcher(ABC):
    @abstractmethod
    async def fetch_workflow(self, workflow_id: str) -> dict:
        pass

class DBWorkflowFetcher(WorkflowFetcher):
    async def fetch_workflow(self, workflow_id: str) -> dict:
        async with SessionLocal() as session:  # Corrected session usage
            result = await session.execute(select(Workflow).filter_by(id=workflow_id))
            workflow = result.scalars().first()

        return {"id": workflow.id, "steps": workflow.steps} if workflow else None
