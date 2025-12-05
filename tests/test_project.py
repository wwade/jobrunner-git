import re

from jobrunner_git.project import workspaceProject


def test_workspaceProject_smoke() -> None:
    """Smoke test: workspaceProject returns valid tuple in a git repo."""
    result = workspaceProject()
    print("result:", result)

    assert isinstance(result, tuple), "Should return a tuple"
    assert len(result) == 2, "Should return a 2-element tuple"

    project_id, is_git = result

    assert isinstance(project_id, str), "First element should be a string"
    assert isinstance(is_git, bool), "Second element should be a boolean"
    assert is_git is True, "Second element should be True in a git repo"

    assert re.search(
        r"[0-9a-f]{40}", project_id
    ), "Project ID should contain a git commit hash (40 hex chars)"

    assert (
        ":" in project_id or len(project_id) == 40 or project_id.endswith("*")
    ), "Project ID should be 'toplevel:hash[*]' or just 'hash'"
