#!/usr/bin/env python3
import os, json, glob, time, shutil
from pathlib import Path

def mark_superseded(path: Path):
  try:
    data=json.loads(path.read_text())
  except Exception:
    return
  data["superseded_at"]=int(time.time())
  data["superseded_by"]="ci-live"
  path.write_text(json.dumps(data,indent=2))

def main():
  for root, _, files in os.walk("evidence"):
    for fn in files:
      if fn.endswith("-BOOTSTRAP.json"):
        p=Path(root)/fn
        mark_superseded(p)
        dst=Path(root)/"bootstrap"/fn
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(p), str(dst))
  print("Bootstrap evidence archived (if present).")

if __name__=="__main__":
  main()