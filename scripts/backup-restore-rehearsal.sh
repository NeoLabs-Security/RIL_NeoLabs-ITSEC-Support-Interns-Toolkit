#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 /path/ending-in-neolabs-recovery-lab" >&2
  exit 2
fi

workspace="$(realpath -m "$1")"
case "$workspace" in
  /|"$HOME"|/home|/root)
    echo "Refusing unsafe workspace: $workspace" >&2
    exit 2
    ;;
esac

if [[ "$(basename "$workspace")" != "neolabs-recovery-lab" ]]; then
  echo "Workspace directory must be named neolabs-recovery-lab" >&2
  exit 2
fi

source_dir="$workspace/source"
backup_dir="$workspace/backup"
restore_dir="$workspace/restored"
evidence_dir="$workspace/evidence"

mkdir -p "$source_dir" "$backup_dir" "$restore_dir" "$evidence_dir"

cat > "$source_dir/asset-register.csv" <<'DATA'
asset_id,hostname,owner,classification
LAB-001,training-endpoint-01,NeoLabs,synthetic
LAB-002,training-endpoint-02,NeoLabs,synthetic
DATA

cat > "$source_dir/support-notes.txt" <<'DATA'
Synthetic recovery rehearsal data.
No live credentials or personal information belong in this workspace.
DATA

find "$source_dir" -type f -print0 | sort -z | xargs -0 sha256sum > "$evidence_dir/source-manifest.sha256"

stamp="$(date -u +%Y%m%dT%H%M%SZ)"
archive="$backup_dir/neolabs-recovery-$stamp.tar.gz"
tar -C "$source_dir" -czf "$archive" .
sha256sum "$archive" > "$archive.sha256"
sha256sum -c "$archive.sha256"

rm -rf "$restore_dir"
mkdir -p "$restore_dir"
tar -C "$restore_dir" -xzf "$archive"

(
  cd "$restore_dir"
  find . -type f -print0 | sort -z | xargs -0 sha256sum
) > "$evidence_dir/restored-manifest.sha256"

sed "s#${source_dir}/#./#" "$evidence_dir/source-manifest.sha256" > "$evidence_dir/source-manifest-relative.sha256"

diff -u "$evidence_dir/source-manifest-relative.sha256" "$evidence_dir/restored-manifest.sha256"

cat > "$evidence_dir/rehearsal-result.txt" <<RESULT
status=success
completed_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
archive=$(basename "$archive")
archive_checksum_file=$(basename "$archive.sha256")
source_files=$(find "$source_dir" -type f | wc -l | tr -d ' ')
restored_files=$(find "$restore_dir" -type f | wc -l | tr -d ' ')
RESULT

echo "NeoLabs recovery rehearsal completed successfully in $workspace"
