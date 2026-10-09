# GitHub repository configuration.
#
# Encodes the settings of the jmcvetta/chiang-mai-wall-book repository itself:
# merge strategy, the ruleset on master, security features, standard labels
# and the non-secret release App ID. Run with a token carrying repo admin
# rights. State is local and committed to Git by whoever applies the stack.
#
# Actions *secrets* are deliberately absent -- the provider would write their
# plaintext into this committed state. Set them by hand and leave them there.

provider "github" {
  owner = local.owner
}

locals {
  owner      = "jmcvetta"
  repository = "chiang-mai-wall-book"
}

# The release App's ID. Not a secret, so it is managed here. The private key
# (RELEASE_BOT_PRIVATE_KEY) is a repository secret set by hand; it is never a
# Tofu input, output or state value. No default: pass the value at plan time
# (TF_VAR_release_bot_app_id) so it is not hard-coded in configuration.
variable "release_bot_app_id" {
  description = "Numeric ID of the release GitHub App (non-secret)"
  type        = string
}
