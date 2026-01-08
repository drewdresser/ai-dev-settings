"""Markdown parser for strategy files (epics and tasks)."""

import re
from pathlib import Path

from models import Epic, Task, Project, Vision, Objective, KeyResult

# Regex patterns for epic parsing
EPIC_TITLE_PATTERN = re.compile(r"^# Epic:\s*(.+)$", re.MULTILINE)
EPIC_STATUS_PATTERN = re.compile(r"^## Status\s*\n+`([^`]+)`", re.MULTILINE)
EPIC_PRIORITY_PATTERN = re.compile(r"\*\*Priority:\*\*\s*`([^`]+)`")
EPIC_TASK_PATTERN = re.compile(r"- \[([ x])\] \[([^\]]+)\]\(([^)]+)\)")

# Regex patterns for task parsing
TASK_TITLE_PATTERN = re.compile(r"^# Task:\s*(.+)$", re.MULTILINE)
TASK_STATUS_PATTERN = re.compile(r"\*\*Status:\*\*\s*`([^`]+)`")
TASK_SIZE_PATTERN = re.compile(r"\*\*Size:\*\*\s*`([^`]+)`")
TASK_EPIC_PATTERN = re.compile(r"\*\*Epic:\*\*\s*\[([^\]]+)\]\(([^)]+)\)")


def parse_epic(file_path: Path, project_name: str) -> Epic | None:
    """Parse an epic markdown file and return an Epic object."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    # Extract title
    title_match = EPIC_TITLE_PATTERN.search(content)
    title = title_match.group(1).strip() if title_match else file_path.stem

    # Extract status
    status_match = EPIC_STATUS_PATTERN.search(content)
    status = status_match.group(1).strip() if status_match else "Not Started"

    # Extract priority
    priority_match = EPIC_PRIORITY_PATTERN.search(content)
    priority = priority_match.group(1).strip() if priority_match else None

    # Count tasks from the ## Tasks section
    task_matches = EPIC_TASK_PATTERN.findall(content)
    task_count = len(task_matches)
    completed_tasks = sum(1 for checkbox, _, _ in task_matches if checkbox == "x")

    return Epic(
        id=file_path.stem,
        title=title,
        status=status,
        project=project_name,
        file_path=str(file_path),
        priority=priority,
        task_count=task_count,
        completed_tasks=completed_tasks,
    )


def parse_task(file_path: Path, project_name: str) -> Task | None:
    """Parse a task markdown file and return a Task object."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    # Extract title
    title_match = TASK_TITLE_PATTERN.search(content)
    title = title_match.group(1).strip() if title_match else file_path.stem

    # Extract status
    status_match = TASK_STATUS_PATTERN.search(content)
    status = status_match.group(1).strip() if status_match else "Todo"

    # Extract size
    size_match = TASK_SIZE_PATTERN.search(content)
    size = size_match.group(1).strip() if size_match else "M"

    # Extract epic link
    epic_match = TASK_EPIC_PATTERN.search(content)
    if epic_match:
        epic_link = epic_match.group(2)
        # Extract epic id from link like "../epics/epic-name.md"
        epic_id = Path(epic_link).stem
    else:
        # Try to infer from filename (e.g., epic-name-001-task.md)
        parts = file_path.stem.split("-")
        # Find where the number starts
        epic_parts = []
        for part in parts:
            if part.isdigit():
                break
            epic_parts.append(part)
        epic_id = "-".join(epic_parts) if epic_parts else "unknown"

    return Task(
        id=file_path.stem,
        title=title,
        status=status,
        size=size,
        project=project_name,
        epic_id=epic_id,
        file_path=str(file_path),
    )


def format_project_name(dir_name: str) -> str:
    """Convert directory name to display name."""
    # Replace hyphens with spaces and title case
    return dir_name.replace("-", " ").title()


def extract_section(content: str, header: str) -> str | None:
    """Extract content under a markdown header until the next header or end."""
    pattern = rf"^##\s*{re.escape(header)}.*?\n(.*?)(?=^##|\Z)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def extract_bullet_list(text: str | None) -> list[str]:
    """Extract bullet points from text."""
    if not text:
        return []
    bullets = []
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("- ") or line.startswith("* "):
            # Remove the bullet and clean up
            item = line[2:].strip()
            # Remove checkbox if present
            if item.startswith("[ ] ") or item.startswith("[x] "):
                item = item[4:]
            if item:
                bullets.append(item)
    return bullets


def extract_numbered_list(text: str | None) -> list[str]:
    """Extract numbered items from text."""
    if not text:
        return []
    items = []
    for line in text.split("\n"):
        line = line.strip()
        # Match "1. text" or "1) text" patterns
        match = re.match(r"^\d+[.)]\s*(.+)$", line)
        if match:
            items.append(match.group(1).strip())
    return items


def parse_vision(file_path: Path) -> Vision | None:
    """Parse a VISION.md file and return a Vision object."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    # Extract North Star (single paragraph after header)
    north_star_section = extract_section(content, "North Star")
    north_star = north_star_section.split("\n")[0] if north_star_section else None

    # Extract Vision (paragraph content)
    vision_section = extract_section(content, r"Vision.*")
    vision_text = None
    if vision_section:
        # Get first paragraph before any sub-headers or lists
        lines = []
        for line in vision_section.split("\n"):
            if line.startswith("#") or line.startswith("-") or line.startswith("*"):
                break
            if line.strip():
                lines.append(line.strip())
        vision_text = " ".join(lines) if lines else None

    # Extract Mission bullets
    mission_section = extract_section(content, "Mission")
    mission = extract_bullet_list(mission_section)

    # Extract Strategic Bets (numbered list)
    bets_section = extract_section(content, "Strategic Bets")
    strategic_bets = extract_numbered_list(bets_section) or extract_bullet_list(
        bets_section
    )

    # Extract Non-Goals
    non_goals_section = extract_section(content, "Non-Goals")
    non_goals = extract_bullet_list(non_goals_section)

    # Extract Success Metrics
    metrics_section = extract_section(content, "Success Metrics")
    success_metrics = extract_bullet_list(metrics_section)

    return Vision(
        north_star=north_star,
        vision=vision_text,
        mission=mission if mission else None,
        strategic_bets=strategic_bets if strategic_bets else None,
        non_goals=non_goals if non_goals else None,
        success_metrics=success_metrics if success_metrics else None,
    )


def parse_okrs(file_path: Path) -> list[Objective]:
    """Parse an OKRs.md file and return a list of Objective objects."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []

    objectives = []

    # Find all Objective headers (## Objective N — Title)
    obj_pattern = re.compile(
        r"^##\s*Objective\s*(\d+)\s*[—–-]\s*(.+?)$", re.MULTILINE
    )

    matches = list(obj_pattern.finditer(content))

    for i, match in enumerate(matches):
        obj_num = match.group(1)
        obj_title = match.group(2).strip()
        obj_id = f"O{obj_num}"

        # Get content until next Objective or end
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        obj_content = content[start:end]

        # Extract intent (line starting with **Intent:**)
        intent_match = re.search(r"\*\*Intent:\*\*\s*(.+?)(?:\n|$)", obj_content)
        intent = intent_match.group(1).strip() if intent_match else None

        # Extract Key Results (### Key Results section or - **KR1:** patterns)
        key_results = []
        kr_pattern = re.compile(
            r"-\s*\*\*KR(\d+):\*\*\s*(.+?)(?=\n-\s*\*\*KR|\n##|\n---|\Z)",
            re.DOTALL,
        )
        for kr_match in kr_pattern.finditer(obj_content):
            kr_id = f"KR{kr_match.group(1)}"
            kr_text = kr_match.group(2).strip()
            # Clean up multi-line KRs
            kr_text = " ".join(line.strip() for line in kr_text.split("\n") if line.strip())
            key_results.append(KeyResult(id=kr_id, text=kr_text))

        objectives.append(
            Objective(
                id=obj_id,
                title=obj_title,
                intent=intent,
                key_results=key_results if key_results else None,
            )
        )

    return objectives


def scan_project(project_path: Path) -> tuple[Project, list[Epic], list[Task]]:
    """Scan a single project's strategy folder and return all epics and tasks."""
    project_name = project_path.name
    strategy_path = project_path / "strategy"

    project = Project(id=project_name, name=format_project_name(project_name))
    epics: list[Epic] = []
    tasks: list[Task] = []

    if not strategy_path.exists():
        return project, epics, tasks

    # Parse VISION.md
    vision_path = strategy_path / "VISION.md"
    if vision_path.exists():
        project.vision = parse_vision(vision_path)

    # Parse OKRs.md (try both cases)
    okrs_path = strategy_path / "OKRs.md"
    if not okrs_path.exists():
        okrs_path = strategy_path / "OKRS.md"
    if okrs_path.exists():
        project.okrs = parse_okrs(okrs_path)

    # Scan epics
    epics_path = strategy_path / "epics"
    if epics_path.exists():
        for epic_file in sorted(epics_path.glob("*.md")):
            epic = parse_epic(epic_file, project_name)
            if epic:
                epics.append(epic)

    # Scan tasks
    tasks_path = strategy_path / "tasks"
    if tasks_path.exists():
        for task_file in sorted(tasks_path.glob("*.md")):
            task = parse_task(task_file, project_name)
            if task:
                tasks.append(task)

    return project, epics, tasks


def scan_all_projects(
    projects_dir: Path, project_names: list[str]
) -> tuple[list[Project], list[Epic], list[Task]]:
    """Scan all configured projects and return aggregated data."""
    all_projects: list[Project] = []
    all_epics: list[Epic] = []
    all_tasks: list[Task] = []

    for name in project_names:
        project_path = projects_dir / name
        if project_path.exists():
            project, epics, tasks = scan_project(project_path)
            all_projects.append(project)
            all_epics.extend(epics)
            all_tasks.extend(tasks)

    return all_projects, all_epics, all_tasks
