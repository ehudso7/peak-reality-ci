import * as path from 'path';
import { runTests } from 'vscode-test';

async function main() {
  try {
    const extensionDevelopmentPath = path.resolve(__dirname, '../../vscode-extension');
    const extensionTestsPath = path.resolve(__dirname, './suite');
    await runTests({
      extensionDevelopmentPath,
      extensionTestsPath,
      launchArgs: ['--disable-extensions']
    });
  } catch (err) {
    console.error('Failed to run VS Code extension tests', err);
    process.exit(1);
  }
}

main();