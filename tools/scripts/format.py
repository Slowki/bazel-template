"""Format the repository.

Usage: bazel run //tools/scripts:format
"""

import multiprocessing
import os
import subprocess
import sys
from pathlib import Path

import black
import isort
import python.runfiles.runfiles

RUNFILES = python.runfiles.runfiles.Create()
BUILDIFIER = RUNFILES.Rlocation("com_github_bazelbuild_buildtools/buildifier/buildifier_/buildifier")

WORKSPACE = Path(os.environ["BUILD_WORKSPACE_DIRECTORY"])
TARGET_BRANCH = "origin/master"
LINE_LENGTH = 120

CXX_FILE_EXTENSIONS = frozenset((".cc", ".hh"))
PYTHON_FILE_EXTENSIONS = frozenset((".py", ".pyi"))


def format_file(file: str) -> None:
    file_path = Path(file)
    if file_path.suffix in PYTHON_FILE_EXTENSIONS:
        mode = black.FileMode(
            target_versions={black.TargetVersion.PY38},
            line_length=LINE_LENGTH,
            is_pyi=file_path.suffix == ".pyi",
            string_normalization=True,
        )
        isort.SortImports(file_path)
        black.format_file_in_place(file_path, False, mode, black.WriteBack.YES)
    elif file_path.suffix in CXX_FILE_EXTENSIONS:
        subprocess.run(["clang-format", "-i", "-style=file", file_path], cwd=WORKSPACE)
    elif file_path.suffix == ".bzl" or file_path.name in {"BUILD", "WORKSPACE"}:
        subprocess.run([BUILDIFIER, "-lint", "fix", file_path], cwd=WORKSPACE)


def main(all_files: bool = False) -> None:
    if all_files:
        changed_files = (
            subprocess.run(
                ["git", "ls-files"], universal_newlines=True, stdout=subprocess.PIPE, check=True, cwd=WORKSPACE,
            )
            .stdout.strip()
            .splitlines()
        )
    else:
        merge_base = subprocess.run(
            ["git", "merge-base", "--fork-point", TARGET_BRANCH],
            universal_newlines=True,
            stdout=subprocess.PIPE,
            check=True,
            cwd=WORKSPACE,
        ).stdout.rstrip()
        changed_files = (
            subprocess.run(
                ["git", "diff", "--name-only", merge_base, "--diff-filter=AM"],
                universal_newlines=True,
                stdout=subprocess.PIPE,
                check=True,
                cwd=WORKSPACE,
            )
            .stdout.strip()
            .splitlines()
        )
    with multiprocessing.Pool(processes=round((os.cpu_count() or 8) * 1.5)) as pool:
        pool.map(
            format_file, [str((WORKSPACE / file_str).absolute()) for file_str in changed_files],
        )


if __name__ == "__main__":
    try:
        # TODO: actually parse arguments
        main(all_files="--all" in sys.argv)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
