# The repository itself. Imported, never recreated: name and visibility are the
# live values and must not change.
#
# Squash-only with PR_TITLE as the commit subject keeps Conventional Commit
# titles on master, which release-please reads.
resource "github_repository" "this" {
  name        = local.repository
  description = "WIP"
  visibility  = "public"

  has_issues      = true
  has_projects    = true
  has_wiki        = true
  has_discussions = false
  is_template     = false
  allow_forking   = true
  archived        = false

  web_commit_signoff_required = false

  allow_squash_merge          = true
  allow_merge_commit          = false
  allow_rebase_merge          = false
  allow_auto_merge            = true
  allow_update_branch         = false
  delete_branch_on_merge      = true
  squash_merge_commit_title   = "PR_TITLE"
  squash_merge_commit_message = "PR_BODY"

  # Inert while merge commits are disabled, but the API reports these values,
  # so declaring them keeps the plan quiet.
  merge_commit_title   = "MERGE_MESSAGE"
  merge_commit_message = "PR_TITLE"

  # Already enabled live; declared so they stay enabled.
  security_and_analysis {
    secret_scanning {
      status = "enabled"
    }
    secret_scanning_push_protection {
      status = "enabled"
    }
  }
}

# Dependabot alerts. Its own resource rather than the repository's deprecated
# vulnerability_alerts field.
resource "github_repository_vulnerability_alerts" "this" {
  repository = github_repository.this.name
  enabled    = true
}

resource "github_repository_dependabot_security_updates" "this" {
  repository = github_repository.this.name
  enabled    = true

  depends_on = [github_repository_vulnerability_alerts.this]
}

# Default workflow token is read-only and may not create or approve pull
# requests; the release App does that work.
resource "github_workflow_repository_permissions" "this" {
  repository                       = github_repository.this.name
  default_workflow_permissions     = "read"
  can_approve_pull_request_reviews = false
}

# Credential interface for release-please.yml (vars.RELEASE_BOT_APP_ID).
resource "github_actions_variable" "release_bot_app_id" {
  repository    = github_repository.this.name
  variable_name = "RELEASE_BOT_APP_ID"
  value         = var.release_bot_app_id
}
