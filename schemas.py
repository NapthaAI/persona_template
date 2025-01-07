from pydantic import BaseModel
from typing import Dict, List

class Persona(BaseModel):
    name: str
    bio: List[str]
    lore: List[str]
    adjectives: List[str]
    topics: List[str]
    style: Dict[str, List[str]]
    messageExamples: List
    postExamples: List