// Example Playwright config scaffolded by /self-improve:setup for UI target repos.
// Adapt baseURL, the webServer command, and ports to the target project, then remove this notice.
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests/journeys',
  // Fail the build if test.only is committed; retry once to absorb rare flakiness.
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  reporter: [['list'], ['html', { open: 'never' }]],
  // Visual-regression defaults: small threshold so real UI changes are caught,
  // but anti-aliasing noise does not cause false failures.
  expect: {
    toHaveScreenshot: { maxDiffPixelRatio: 0.01, animations: 'disabled' },
  },
  use: {
    baseURL: process.env.BASE_URL ?? 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [{ name: 'chromium', use: { ...devices['Desktop Chrome'] } }],
  // Let Playwright start the app and wait for it to be ready (no arbitrary sleeps).
  webServer: {
    command: process.env.START_CMD ?? 'npm run dev',
    url: process.env.BASE_URL ?? 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
    timeout: 120_000,
  },
});
