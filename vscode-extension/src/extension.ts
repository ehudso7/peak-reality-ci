import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  console.log('Peak Reality++ extension is now active!');
  let disposable = vscode.commands.registerCommand(
    'peak-reality.helloWorld',
    () => {
      vscode.window.showInformationMessage('Peak Reality++ says hello!');
    }
  );
  context.subscriptions.push(disposable);
}

export function deactivate() {}