from sqlalchemy import Column, String, JSON
from database import Base

class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(String, primary_key=True, index=True)  # Unique workflow ID
    steps = Column(JSON, nullable=False)  # JSON field to store workflow steps
