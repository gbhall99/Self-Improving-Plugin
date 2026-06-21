.PHONY: validate install-hooks help

help:
	@echo "self-improve plugin — make targets:"
	@echo "  make validate       Validate plugin/marketplace manifests + command/agent frontmatter"
	@echo "  make install-hooks  Enable the git pre-push hook so validation runs locally on every push"
	@echo ""
	@echo "Validation runs the same script in CI, here, and in the pre-push hook,"
	@echo "so quality stays gated even with zero GitHub Actions minutes."

# Same check CI runs. No dependencies beyond python3.
validate:
	@python3 scripts/validate_plugin.py

# Point git at the repo's tracked hooks. Run once per clone.
install-hooks:
	@git config core.hooksPath .githooks
	@echo "Pre-push hook enabled (core.hooksPath=.githooks). Pushes now validate locally."
