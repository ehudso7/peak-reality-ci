const path = require('path');
const { execa } = require('execa');

describe('Peak Platform CLI', () => {
  const cliPath = path.resolve(__dirname, '../src/cli.js');

  test('prints version', async () => {
    const { stdout } = await execa('node', [cliPath, '--version']);
    const pkg = require('../package.json');
    expect(stdout.trim()).toBe(pkg.version);
  });

  test('prints help text', async () => {
    const { stdout } = await execa('node', [cliPath, '--help']);
    expect(stdout).toMatch(/Commands:/);
    expect(stdout).toMatch(/review \[files...\]/);
  });
});