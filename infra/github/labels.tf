# The standard issue labels: six issue kinds plus the supplemental `story`
# marker, with the colours and descriptions shared with the owner's other
# repositories.
#
# Tofu owns only what it declares, so an apply leaves GitHub's other stock
# labels and unrelated labels untouched. Every label that already exists must
# be imported before the first apply (see import.sh); `research` is the only
# one the apply creates.

resource "github_issue_label" "epic" {
  repository  = github_repository.this.name
  name        = "epic"
  color       = "5319e7"
  description = "Coordinates a sequence of other issues"
}

# A lighter purple than its epic parent distinguishes a story in issue lists.
resource "github_issue_label" "story" {
  repository  = github_repository.this.name
  name        = "story"
  color       = "d4c5f9"
  description = "A focused piece of work within an epic"
}

resource "github_issue_label" "task" {
  repository  = github_repository.this.name
  name        = "task"
  color       = "0e8a16"
  description = "Discrete work, specified and ready for an agent"
}

# Red is GitHub's own colour for this label, kept so an imported `bug` reports
# no change on the first plan beyond its description.
resource "github_issue_label" "bug" {
  repository  = github_repository.this.name
  name        = "bug"
  color       = "d73a4a"
  description = "Bug report"
}

resource "github_issue_label" "proposal" {
  repository  = github_repository.this.name
  name        = "proposal"
  color       = "1d76db"
  description = "Proposed feature"
}

resource "github_issue_label" "research" {
  repository  = github_repository.this.name
  name        = "research"
  color       = "fbca04"
  description = "A question to settle"
}

# Not a status. `human` says the work itself is a person's -- credentials no
# agent holds, a decision only the user can make, an action outside the
# repository -- and an agent that stops on one stops because of what the work
# is, not because of where it got to.
resource "github_issue_label" "human" {
  repository  = github_repository.this.name
  name        = "human"
  color       = "006b75"
  description = "Work only a person can do"
}
