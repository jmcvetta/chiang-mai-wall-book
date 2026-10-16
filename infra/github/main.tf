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
