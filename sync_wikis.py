#!/usr/bin/env python3
"""Sync staged wiki pages to per-repository GitHub Wikis.

Prerequisite: each target repo's wiki must be initialized once via the
GitHub web UI (repo → Wiki → "Create the first page") — GitHub does not
allow .wiki.git pushes before that. This script detects which wikis
exist and pushes the staged pages for those that do; repos whose wikis
are not yet initialized are skipped and reported.

Usage: python3 sync_wikis.py [--repo SigmaOS-foo] [--dry-run]
"""
import argparse
import os
import subprocess
import sys

OWNER = "AaryanSinghChauhan09"
STAGING = os.path.dirname(os.path.abspath(__file__))

def wiki_exists(repo):
    r = subprocess.run(
        ["git", "ls-remote", f"https://github.com/{OWNER}/{repo}.wiki.git", "HEAD"],
        capture_output=True, text=True, timeout=30)
    return r.returncode == 0

def sync_repo(repo, dry_run):
    src = os.path.join(STAGING, repo)
    if not os.path.isdir(src):
        return "no-staged-pages"
    pages = [f for f in os.listdir(src) if f.endswith(".md")]
    if not pages:
        return "no-pages"
    if dry_run:
        return f"would-push {len(pages)} pages"
    with open("/dev/null") as dn:
        pass
    # clone existing wiki (has at least one page after UI init)
    import tempfile, shutil
    with tempfile.TemporaryDirectory() as td:
        clone = os.path.join(td, "wiki")
        r = subprocess.run(["git", "clone", "-q",
                            f"https://github.com/{OWNER}/{repo}.wiki.git", clone],
                           capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            return f"clone-failed: {r.stderr.strip()[-120:]}"
        for p in pages:
            shutil.copy2(os.path.join(src, p), os.path.join(clone, p))
        subprocess.run(["git", "add", "-A"], cwd=clone, check=True)
        r = subprocess.run(["git", "-c", "user.name=SigmaOS Wiki Bot",
                            "-c", "user.email=wiki-bot@sigmaos.local",
                            "commit", "-qm", "Sync staged wiki pages"],
                           cwd=clone, capture_output=True, text=True)
        if r.returncode != 0:
            return "nothing-to-commit"
        r = subprocess.run(["git", "push", "-q"], cwd=clone,
                           capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            return f"push-failed: {r.stderr.strip()[-120:]}"
        return f"pushed {len(pages)} pages"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", help="sync only this repo")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.repo:
        repos = [args.repo]
    else:
        repos = sorted(d for d in os.listdir(STAGING)
                       if d.startswith(("SigmaOS-", "Sigma")) and
                       os.path.isdir(os.path.join(STAGING, d)))
    synced, skipped, failed = [], [], []
    for repo in repos:
        if not wiki_exists(repo):
            skipped.append(repo)
            continue
        res = sync_repo(repo, args.dry_run)
        print(f"{repo}: {res}")
        if res.startswith(("pushed", "would-push", "nothing-to-commit")):
            synced.append(repo)
        else:
            failed.append((repo, res))
    print(f"\nsummary: synced={len(synced)} skipped(no-wiki)={len(skipped)} failed={len(failed)}")
    if skipped:
        print("skipped repos need one-time wiki init in the GitHub web UI")
    for r, e in failed:
        print(f"FAILED {r}: {e}")

if __name__ == "__main__":
    main()
