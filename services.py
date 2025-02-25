import asyncio
import logging
from fetcher import DBWorkflowFetcher
from executor import WorkflowExecutor

logging.basicConfig(level=logging.INFO)

class WorkflowExecutionManager:
    def __init__(self, fetcher: DBWorkflowFetcher, executor: WorkflowExecutor):
        self.fetcher = fetcher  # Injected dependency
        self.executor = executor  # Injected dependency

    async def execute_workflow(self, workflow_id: str):
        await asyncio.sleep(2)  # Simulate processing delay
        workflow = await self.fetcher.fetch_workflow(workflow_id)
        if not workflow:
            raise ValueError("Workflow not found")  # Raise error if workflow does not exist

        await self.executor.execute(workflow["id"], workflow["steps"])  # Execute workflow
        return {"status": "Workflow executed", "workflow_id": workflow["id"]}
