#!/usr/bin/env python
# Imports
import subprocess

# DTO
import dto


def execute_local_command() -> dto.CommandDTO:
    """
    Выполняет комманду pwd на хосте
    Возвращает строковый результат
    """

    cmd: subprocess.CompletedProcess = subprocess.run('pwd', shell=True, encoding='utf-8', executable='/bin/bash', stdout=subprocess.PIPE)

    return dto.CommandDTO(
        cmd=str(cmd.stdout),
        exit_code=str(cmd.returncode)
    )


if __name__=='__main__':
    execute_local_command()
