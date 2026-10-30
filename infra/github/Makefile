.PHONY: check-fmt validate checkov check-infra

# Verify OpenTofu formatting.
check-fmt:
	tofu fmt -check -recursive .

# Validate without touching the backend or contacting GitHub.
validate:
	tofu init -backend=false && tofu validate

# Scan the stack against Checkov policies. The config names `infra` relative
# to the repository root, so run from there.
checkov:
	cd ../.. && checkov --config-file .checkov.yaml

check-infra: check-fmt validate checkov
