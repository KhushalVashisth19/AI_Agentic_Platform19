import logging
from abc import ABC, abstractmethod

# Configure logging to display workflow execution logs
logging.basicConfig(level=logging.INFO)

# Abstract base class for workflow execution strategy
class WorkflowExecutor(ABC):
    @abstractmethod
    async def execute(self, workflow_id: str, workflow_data: dict) -> None:
        pass

# In-memory workflow executor for testing purposes
class InMemoryWorkflowExecutor(WorkflowExecutor):
    async def execute(self, workflow_id: str, workflow_data: dict) -> None:
        logging.info(f"Executing workflow {workflow_id}: {workflow_data}")
