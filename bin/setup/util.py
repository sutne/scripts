import sys


def min_python_version(major: int, minor: int, micro: int = 0) -> None:
    """Make sure users python version is equal or higher than the minimum specified"""
    act_major = sys.version_info.major
    act_minor = sys.version_info.minor
    act_micro = sys.version_info.micro
    if act_major >= major and act_minor >= minor and act_micro >= micro:
        return
    sys.exit(
        f"Python {major}.{minor}.{micro} or later is required.\
        \nYou have {act_major}.{act_minor}.{act_micro}"
    )
