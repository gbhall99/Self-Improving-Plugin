// Example P0-journey test scaffolded by /self-improve:setup. One spec per journey in
// journeys.md. Replace the persona/journey, steps, selectors, and assertions with the real
// flow, then remove this notice. Walk the journey exactly as the persona would.
import { test, expect } from '@playwright/test';

// Journey: <id> -- <name> (persona: <persona>)
// Trigger -> steps -> expected outcome (mirror journeys.md).
test('<journey-id>: <persona> can <achieve the journey outcome>', async ({ page }) => {
  // 1. Entry point of the journey.
  await page.goto('/');

  // 2. Walk the steps with realistic input. Prefer role/label selectors over brittle CSS.
  //    await page.getByRole('button', { name: 'Get started' }).click();
  //    await page.getByLabel('Email').fill('persona@example.com');

  // 3. Assert the real outcome the persona cares about (not just that a page rendered).
  //    await expect(page.getByRole('heading', { name: 'Welcome' })).toBeVisible();

  // 4. Visual checkpoint at a key step. First run records the baseline; later runs diff
  //    against it and FAIL on an unexpected change (the visual-regression gate).
  await expect(page).toHaveScreenshot('<journey-id>-key-step.png');
});
