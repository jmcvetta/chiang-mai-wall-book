#!/usr/bin/env bash
#
# Import the live GitHub configuration into local state, so the first plan
# adopts it instead of trying to create it.
#
# Idempotent: each import is skipped if that address is already in state.
#
# Usage:
#   export GITHUB_TOKEN=$(gh auth token)
#   export TF_VAR_release_bot_app_id=<numeric App ID>
#   tofu init
#   ./import.sh

set -euo pipefail

readonly REPO="chiang-mai-wall-book"

import() {
	local address="$1" id="$2"
	if [[ -n "$(tofu state list "$address" 2>/dev/null)" ]]; then
		echo "== skip $address (already in state)"
		return
	fi
	echo "== import $address"
	tofu import "$address" "$id"
}

import 'github_repository.this' "$REPO"
import 'github_repository_vulnerability_alerts.this' "$REPO"
import 'github_repository_dependabot_security_updates.this' "$REPO"

# Every label that exists live. `research` does not exist; the apply creates it.
for label in epic task human story bug proposal; do
	import "github_issue_label.$label" "$REPO:$label"
done

# Only if the variable already exists (check Settings -> Variables first);
# otherwise the apply creates it. The id is `<repository>:<variable name>`.
if [[ "${IMPORT_RELEASE_BOT_APP_ID:-}" == "1" ]]; then
	import 'github_actions_variable.release_bot_app_id' "$REPO:RELEASE_BOT_APP_ID"
fi

echo
echo "Import complete. Verify with: tofu plan"
