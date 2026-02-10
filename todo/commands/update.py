from __future__ import absolute_import

import os
import subprocess
import sys

from todo.commands.base import Command
from todo.utils.styles import Fore, Style


class UpdateCommand(Command):
    def run(self):
        """
        Updates the application by pulling the latest changes and re-running the install script.
        """
        print('{info}Updating todo-cli...{reset}'.format(
            info=Fore.INFO,
            reset=Style.RESET_ALL,
        ))

        source_dir = os.path.expanduser("~/.todo-cli-source")
        install_script = os.path.join(source_dir, "install.sh")

        if not os.path.isdir(source_dir):
            print(
                '{fail}Source directory not found at {dir}. Please reinstall.{reset}'
                .format(fail=Fore.FAIL, dir=source_dir, reset=Style.RESET_ALL)
            )
            sys.exit(1)

        try:
            # Re-run the install script to build and install the new version
            print(f"{{info}}Re-running installation script...{{reset}}")
            result = subprocess.run(
                ["bash", install_script],
                check=True,
                capture_output=True,
                text=True,
            )

            print('{success}Update successful!{reset}'.format(
                success=Fore.SUCCESS,
                reset=Style.RESET_ALL,
            ))
            sys.exit(0)

        except subprocess.CalledProcessError as e:
            print(
                '{fail}Update failed. Please try again later or update manually.{reset}'
                .format(fail=Fore.FAIL, reset=Style.RESET_ALL)
            )
            print("\n--- Error Details ---")
            print(e.stdout)
            print(e.stderr)
            print("-----------------------")
            sys.exit(1)
        except Exception as e:
            print(
                '{fail}An unexpected error occurred: {error}{reset}'
                .format(fail=Fore.FAIL, error=e, reset=Style.RESET_ALL)
            )
            sys.exit(1)


Update = UpdateCommand()
