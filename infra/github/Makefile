.PHONY: check-fmt validate check-infra

# Verify OpenTofu formatting.
check-fmt:
	tofu fmt -check -recursive .

# Validate without touching the backend or contacting GitHub.
validate:
	tofu init -backend=false && tofu validate

check-infra: check-fmt validate
