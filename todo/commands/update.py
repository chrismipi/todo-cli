from __future__ import absolute_import

import os
import subprocess
import sys

from todo.commands.base import Command
from todo.utils.styles import Fore, Style


class UpdateCommand(Command):
    def run(self):
        """
        Updates the application by fetching and running the latest install script.
        """
        print('{info}Updating todo-cli...{reset}'.format(
            info=Fore.INFO,
            reset=Style.RESET_ALL,
        ))

        try:
            # The command to download and run the installer script
            install_command = "curl -sSL https://raw.githubusercontent.com/francoischalifour/todo-cli/master/install.sh | bash"

            # We use subprocess.run to execute the command.
            # We capture the output to show it only if there's an error.
            result = subprocess.run(install_command, shell=True, check=True, capture_output=True, text=True)

            print('{success}Update successful!{reset}'.format(
                success=Fore.SUCCESS,
                reset=Style.RESET_ALL,
            ))
            # The script will replace the current executable, so we exit.
            sys.exit(0)

        except subprocess.CalledProcessError as e:
            print(
                '{fail}Update failed. Please try again later or update manually.{reset}'
                .format(
                    fail=Fore.FAIL,
                    reset=Style.RESET_ALL,
                )
            )
            print("\n--- Installer Output ---")
            print(e.stdout)
            print(e.stderr)
            print("------------------------")
            sys.exit(1)
        except Exception as e:
            print(
                '{fail}An unexpected error occurred: {error}{reset}'
                .format(
                    fail=Fore.FAIL,
                    error=e,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit(1)


Update = UpdateCommand()
