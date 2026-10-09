# Protection for master, as a ruleset (not classic branch protection).
resource "github_repository_ruleset" "master" {
  name        = "master"
  repository  = github_repository.this.name
  target      = "branch"
  enforcement = "active"

  conditions {
    ref_name {
      include = ["~DEFAULT_BRANCH"]
      exclude = []
    }
  }

  # Repository admins may bypass only from a pull request, so direct pushes to
  # master stay blocked even for them. actor_id 5 is the built-in admin role.
  bypass_actors {
    actor_id    = 5
    actor_type  = "RepositoryRole"
    bypass_mode = "pull_request"
  }

  rules {
    deletion                = true
    non_fast_forward        = true
    required_linear_history = true

    # Solo repository: no approvals required. The rule forces changes through a
    # pull request, resolves conversations, and pins squash as the only method.
    pull_request {
      required_approving_review_count   = 0
      dismiss_stale_reviews_on_push     = false
      require_code_owner_review         = false
      require_last_push_approval        = false
      required_review_thread_resolution = true
      allowed_merge_methods             = ["squash"]
    }

    # Each context is a check-run name: the `name:` of an Actions job. "Checks"
    # is job `checks` in ci.yml; "Release Projection" is job `release-projection`
    # in release-projection.yml. Renaming either job without editing this file
    # leaves a required check nothing reports and blocks every pull request.
    required_status_checks {
      strict_required_status_checks_policy = true
      do_not_enforce_on_create             = false

      required_check {
        context = "Checks"
      }

      required_check {
        context = "Release Projection"
      }
    }
  }
}
