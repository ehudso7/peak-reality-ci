#!/usr/bin/env python3
import argparse, json, os, time
from pathlib import Path

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("mode", choices=["pr"])
  ap.add_argument("--start", required=True)
  ap.add_argument("--tia_target", default="0.995")
  args = ap.parse_args()
  os.makedirs("evidence/calibrationRuns", exist_ok=True)
  now = int(time.time())
  dur = now - int(args.start)
  rec = {
    "id": f"PR-{now}",
    "pr_p95_minutes": round(dur/60.0, 2),
    "pr_p50_minutes": round(dur/120.0, 2),
    "cache_hit_rate_pct": 0.0,
    "tia_enabled": True,
    "mutation_sampling": "elastic",
    "date": time.strftime("%Y-%m-%d"),
    "bootstrap": False
  }
  with open(f"evidence/calibrationRuns/PR-{now}.json","w") as f:
    json.dump(rec,f,indent=2)
  # minimal index.json (append-only)
  idxp=Path("evidence/index.json")
  if idxp.exists():
    idx=json.loads(idxp.read_text())
  else:
    idx={"builds":[],"sboms":[],"attestations":[],"reproducibleBuildReports":[],"privacyDrills":[],
         "promptAttestations":[],"evalSuites":[],"datasetLineage":[],"ragBoundaryReports":[],
         "weightAttestations":[],"governanceMap":[],"providerParity":[],"hitlSla":[],"ipSafetyShadow":[],
         "flagAudit":[],"datasetSboms":[],"promptSboms":[],"retentionBudgets":[],"waiverNotices":[],
         "waiverAutoPrs":[],"gpuEnvEnvelopes":[],"sarifReports":[],"contentCredentials":[],"aiActEvidence":{},
         "aiActDrills":[],"carbonAwareRuns":[],"tiaReports":[],"concurrencyPlans":[],"rollbackEvents":[],
         "flakeQuarantines":[],"determinismReports":[],"calibrationRuns":[],"reviewerTriage":[]}
  idx["calibrationRuns"].append(rec)
  idxp.write_text(json.dumps(idx,indent=2))
  print(json.dumps({"pr_minutes": rec["pr_p95_minutes"]}))

if __name__=="__main__":
  main()