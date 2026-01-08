"""Data models for the strategy dashboard."""

from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class Epic:
    """Represents an epic from a project's strategy folder."""

    id: str  # filename without .md
    title: str  # from "# Epic: [Title]"
    status: str  # Done | In Progress | Not Started
    project: str  # parent project name
    file_path: str  # absolute path for linking
    priority: str | None  # from Dependencies section
    task_count: int  # total tasks listed
    completed_tasks: int  # tasks with [x]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Task:
    """Represents a task from a project's strategy folder."""

    id: str  # filename without .md
    title: str  # from "# Task: [Title]"
    status: str  # Todo | In Progress | Done
    size: str  # S | M | L | XL
    project: str  # parent project name
    epic_id: str  # parsed from epic link
    file_path: str  # absolute path for linking

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Project:
    """Represents a project being tracked."""

    id: str  # directory name
    name: str  # display name
    vision: "Vision | None" = None
    okrs: list["Objective"] | None = None

    def to_dict(self) -> dict[str, Any]:
        result = {"id": self.id, "name": self.name}
        if self.vision:
            result["vision"] = self.vision.to_dict()
        if self.okrs:
            result["okrs"] = [o.to_dict() for o in self.okrs]
        return result


@dataclass
class Vision:
    """Represents a project's vision document."""

    north_star: str | None = None
    vision: str | None = None
    mission: list[str] | None = None
    strategic_bets: list[str] | None = None
    non_goals: list[str] | None = None
    success_metrics: list[str] | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class KeyResult:
    """Represents a key result under an objective."""

    id: str  # e.g., "KR1"
    text: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Objective:
    """Represents an OKR objective."""

    id: str  # e.g., "O1"
    title: str
    intent: str | None = None
    key_results: list[KeyResult] | None = None

    def to_dict(self) -> dict[str, Any]:
        result = {"id": self.id, "title": self.title, "intent": self.intent}
        if self.key_results:
            result["key_results"] = [kr.to_dict() for kr in self.key_results]
        return result
