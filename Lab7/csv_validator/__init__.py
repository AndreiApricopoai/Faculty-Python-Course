# Ex1
# Create a package that reads CSV files and validates their contents based on user-defined
# rules (e.g., checking for missing values, ensuring data types are correct).

from .validator import validate_csv
__all__ = ['validate_csv']
