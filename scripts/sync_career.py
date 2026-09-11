#!/usr/bin/env python3
"""
Career System Sync & Audit Script
Maintains synchronization between structured data.json, tracker.md, validates pre-commit rules,
checks for secrets, commits with structured message, pushes to origin master, and verifies remote status.
"""

import json
import os
import subprocess
import sys
import re

CAREER_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JSON_PATH = os.path.join(CAREER_ROOT, "data.json")
TRACKER_MD_PATH = os.path.join(CAREER_ROOT, "applications", "tracker.md")

SECRET_PATTERNS = [
    r"sk-[a-zA-Z0-9]{20,}",
    r"ghp_[a-zA-Z0-9]{36}",
    r"github_pat_[a-zA-Z0-9_]{30,}",
    r"api[_-]key\s*[:=]\s*['\"'][a-zA-Z0-9-_]{16,}['\"']",
    r"password\s*[:=]\s*['\"'].+['\"']"
]

def run_cmd(cmd, cwd=CAREER_ROOT):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def load_data():
    if not os.path.exists(DATA_JSON_PATH):
        print(f"[-] Error: {DATA_JSON_PATH} not found.")
        sys.exit(1)
    with open(DATA_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def update_tracker_from_json(data):
    """Regenerates applications/tracker.md from data.json to ensure 100% consistency."""
    lines = [
        "# Job Application Tracker",
        "",
        "| Empresa | Cargo | URL | Descoberta | Status | Fit | Salário | Local | Modalidade | Próx. ação | Obs. |",
        "|---|---|---|---|---|---|---|---|---|---|---|"
    ]
    for app in data.get("applications", []):
        company = app.get("company", "")
        role = app.get("role", "")
        url = app.get("url", "")
        discovery = app.get("discovery_date", "")
        status = app.get("status", "")
        fit = f"{app.get('fit_score', 0)}%"
        salary = app.get("salary", "")
        local = app.get("location", "")
        modality = app.get("modality", "")
        next_action = app.get("next_action", "")
        notes = app.get("notes", "")
        
        row = f"| {company} | {role} | {url} | {discovery} | {status} | {fit} | {salary} | {local} | {modality} | {next_action} | {notes} |"
        lines.append(row)
    
    with open(TRACKER_MD_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("[+] applications/tracker.md successfully updated from data.json.")

def audit_workspace():
    print("[*] Running pre-commit audit...")
    code, stdout, stderr = run_cmd("git status --porcelain")
    if code != 0:
        print(f"[-] BLOCKED: Git status failed: {stderr}")
        return "BLOCKED"
    
    changed_files = [line.strip()[3:] for line in stdout.splitlines() if line.strip()]
    
    # Check for secrets in modified/new files
    for fpath in changed_files:
        full_path = os.path.join(CAREER_ROOT, fpath)
        if os.path.isfile(full_path):
            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    for pattern in SECRET_PATTERNS:
                        if re.search(pattern, content, re.IGNORECASE):
                            print(f"[-] BLOCKED: Potential secret found in {fpath} matching pattern {pattern}")
                            return "BLOCKED"
            except Exception as e:
                pass

    print("[+] Audit PASSED: No secrets detected, workspace is clean.")
    return "PASS"

def sync_and_push(commit_msg):
    data = load_data()
    update_tracker_from_json(data)
    
    audit_result = audit_workspace()
    if audit_result != "PASS":
        print("[-] Sync aborted due to audit failure.")
        sys.exit(1)
        
    code, stdout, stderr = run_cmd("git add .")
    if code != 0:
        print(f"[-] Failed to stage files: {stderr}")
        sys.exit(1)
        
    # Check if there's anything to commit
    code, stdout, stderr = run_cmd("git diff --cached --quiet")
    if code == 0:
        print("[*] No changes to commit.")
        return
        
    code, stdout, stderr = run_cmd(f'git commit -m "{commit_msg}"')
    if code != 0:
        print(f"[-] Commit failed: {stderr}")
        sys.exit(1)
    print(f"[+] Committed: {commit_msg}")
    
    # Push to origin master
    code, stdout, stderr = run_cmd("git push origin master")
    if code != 0:
        print(f"[-] Push failed: {stderr}")
        sys.exit(1)
    print("[+] Successfully pushed to GitHub (origin master).")
    
    # Verify remote head
    code, local_sha, _ = run_cmd("git rev-parse HEAD")
    code_rem, remote_sha, _ = run_cmd("git rev-parse origin/master")
    if local_sha == remote_sha:
        print(f"[+] Verified remote sync: HEAD matches origin/master ({local_sha[:7]})")
    else:
        print(f"[!] Warning: local HEAD ({local_sha[:7]}) differs from origin/master ({remote_sha[:7]})")

if __name__ == "__main__":
    msg = "sync: update career hub data and tracker synchronization"
    if len(sys.argv) > 1:
        msg = sys.argv[1]
    sync_and_push(msg)
