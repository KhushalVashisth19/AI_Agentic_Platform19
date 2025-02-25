from fetcher import DBWorkflowFetcher
from executor import InMemoryWorkflowExecutor
from services import WorkflowExecutionManager

def get_execution_manager():
    fetcher = DBWorkflowFetcher()
    executor = InMemoryWorkflowExecutor()
    return WorkflowExecutionManager(fetcher, executor)
