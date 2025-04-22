import re

PATTERNS = {
    "failed_login": re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"),
    "sudo_misuse":   re.compile(r"authentication failure;.*sudo"),
    # add more as needed
}
