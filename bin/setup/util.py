import sys


def min_python_version(major: int, minor: int, micro: int = 0) -> None:
    """Make sure users python version is equal or higher than the minimum specified"""
    sys_version_up_to_date = (
        major <= sys.version_info.major
        and minor <= sys.version_info.minor
        and micro <= sys.version_info.micro
    )
    if not sys_version_up_to_date:
        feedback = f"Python {major}.{minor}.{micro} or later is required.\n"
        feedback += f"You have {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        sys.exit(feedback)
