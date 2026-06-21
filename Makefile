.PHONY: validate install-hooks help

help:
	@echo "self-improve plugin — make targets:"
	@echo "  make validate       Validate plugin/marketplace manifests + command/agent frontmatter"
	@echo "  make install-hooks  Enable the git pre-push hook so validation runs locally on every push"
	@echo ""
	@echo "Validation runs the same script in CI, here, and in the pre-push hook,"
	@echo "so quality stays gated even with zero GitHub Actions minutes."

# Same check CI runs. No dependencies beyond python3. Additionally runs the
# official `claude plugin validate` (authoritative manifest schema) when the
# claude CLI is available -- it is not on CI runners, so it is best-effort.
validate:
	@python3 scripts/validate_plugin.py
	@command -v claude >/dev/null 2>&1 && { echo "Running official claude plugin validate..."; claude plugin validate .; } || echo "(claude CLI not found; skipping official manifest validation)"

# Point git at the repo's tracked hooks. Run once per clone.
install-hooks:
	@git config core.hooksPath .githooks
	@echo "Pre-push hook enabled (core.hooksPath=.githooks). Pushes now validate locally."
