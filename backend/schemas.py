from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class JobTrack(str, Enum):
    ML = "Machine Learning"
    DATA_SCIENCE = "Data Science"
    GEN_AI = "Generative AI"
    DATA_ENG = "Data Engineering"
    OTHER = "Other"

class SkillCategory(str, Enum):
    HARD_SKILL = "hard_skill"
    TOOL_FRAMEWORK = "tool_framework"
    SOFT_SKILL = "soft_skill"
    RESPONSIBILITY = "responsibility"

class ExtractedJobOffer(BaseModel):
    title: str = Field(description="Normalized job title")
    company: Optional[str] = Field(default=None)
    track: JobTrack = Field(default=JobTrack.OTHER)
    seniority: str = Field(default="Mid")
    summary: str = Field(description="Brief summary of the role")
    responsibilities: List[str] = Field(default_factory=list)
    hard_skills: List[str] = Field(default_factory=list)
    tools: List[str] = Field(default_factory=list)
    soft_skills: List[str] = Field(default_factory=list)

class ExtractedUserProfile(BaseModel):
    known_skills: List[str] = Field(default_factory=list)
    experience_chunks: List[str] = Field(default_factory=list)

class AnalyzeOfferRequest(BaseModel):
    url: Optional[str] = None
    raw_text: Optional[str] = None

class JobOfferRecord(BaseModel):
    id: int
    title: str
    company: Optional[str]
    track: str
    seniority: str
    url: Optional[str]
    summary: str
    created_at: str
    responsibilities: List[str] = []
    hard_skills: List[str] = []
    tools: List[str] = []
    soft_skills: List[str] = []
    novel_skills: List[str] = []
    relevant_user_context: List[str] = []

class UserProfileUpdate(BaseModel):
    additional_notes: Optional[str] = ""

class UserProfileData(BaseModel):
    resume_text: str = ""
    additional_notes: str = ""
    known_skills: List[str] = []
    updated_at: Optional[str] = None

class SkillFrequency(BaseModel):
    skill: str
    count: int
    is_known: bool

class TrackSkillGaps(BaseModel):
    track: str
    top_missing_skills: List[SkillFrequency]
    total_offers: int

class ProjectEvaluation(BaseModel):
    score: float = Field(description="Score from 1.0 to 10.0")
    skill_coverage_ratio: float = Field(default=1.0)
    feasibility_score: float = Field(default=8.5)
    feedback: str = Field(description="Technical critique")
    missing_elements: List[str] = Field(default_factory=list)

class ProjectBlueprint(BaseModel):
    project_title: str
    target_track: JobTrack
    covered_skills: List[str]
    business_problem: str
    system_architecture: str
    implementation_milestones: List[str]
    suggested_datasets_and_apis: List[str]
    evaluation_and_llmops: List[str]
    evaluation_score: float = 8.5
    critic_feedback: str = ""
    rag_context_used: List[str] = Field(default_factory=list)

class GenerateProjectRequest(BaseModel):
    track: JobTrack
    max_skills: int = 5

class LLMOpsTraceRecord(BaseModel):
    id: int
    workflow_type: str
    provider: str
    latency_ms: float
    nodes_executed: List[str]
    status: str
    metadata: Dict[str, Any]
    created_at: str

class EvaluationBenchmarkReport(BaseModel):
    extraction_precision: float
    extraction_recall: float
    extraction_f1: float
    blueprint_skill_coverage: float
    blueprint_faithfulness: float
    total_test_cases: int
    case_details: List[Dict[str, Any]]
