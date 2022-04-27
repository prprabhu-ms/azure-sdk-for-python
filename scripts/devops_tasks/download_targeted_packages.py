
import argparse
import sys
import os
from common_tasks import (
    process_glob_string,
    run_check_call,
    cleanup_folder,
    clean_coverage,
    is_error_code_5_allowed,
    create_code_coverage_params,
    filter_packages_by_compatibility_override
)

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..", ".."))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download wheels and source distributions (if possible) for a set of targeted specifiers."
    )

    parser.add_argument(
        "target_packages",
        nargs="?",
        help=(
            "An array of targeted specifiers, in a json string."
        ),
    )

    parser.add_argument(
        "-d",
        "--dest-dir",
        dest="dest_dir",
        help="Temporary Location of downloaded bits",
    )

    args = parser.parse_args()


    print(args.target_packages)