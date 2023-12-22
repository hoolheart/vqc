"""Special validators for VQC"""

from typing import (
    Any,
    Optional,
    Sequence,
)
from softlab.jin.validator import (
    Validator,
    validate_value,
)
import pandas as pd

class ValDataFrame(Validator):
    """
    Validator required a pandas.DataFrame with given columns

    Args:
    - columns --- sequence of required column names
    - additional --- whether additional columns are permitted
    """

    def __init__(self,
                 columns: Optional[Sequence[str]] = None,
                 additional: bool = True) -> None:
        if isinstance(columns, Sequence):
            self._columns = tuple(filter(
                lambda col: len(col) > 0,
                map(lambda col: str(col), columns)
            ))
        else:
            self._columns = ()
        self._additional = additional if isinstance(additional, bool) else True
        if len(self._columns) == 0:
            self._additional = True

    @property
    def required_columns(self) -> tuple[str]:
        """Tuple of required column names"""
        return self._columns

    @property
    def allow_additional(self) -> bool:
        """Whether additional columns are permitted"""
        return self._additional

    def validate(self, value: Any, context: str = '') -> None:
        if not isinstance(value, pd.DataFrame):
            raise TypeError(
                f'Required pandas.DataFrame but {type(value)} in "{context}"')
        columns = value.columns
        for col in self._columns:
            if not col in columns:
                raise ValueError(f'Column "{col}" is missing')
        if not self._additional and len(columns) > len(self._columns):
            redundency = ', '.join(
                filter(lambda col: not col in self._columns, columns))
            raise ValueError(f'Redundent columns: {redundency}')

    def __repr__(self) -> str:
        if len(self._columns) > 0:
            return '<pandas.DataFrame>({})'.format(','.join(self._columns))
        return '<pandas.DataFrame>'

if __name__ == '__main__':
    for value, validator in [
        ({'a': [5.0], 'b': [6.0]}, ValDataFrame(['a', 'b'])),
        (pd.DataFrame({'a': [5.0], 'b': [6.0]}), ValDataFrame(['a', 'b'])),
        (pd.DataFrame({'a': [5.0], 'b': [6.0]}), ValDataFrame(['a', 'c'])),
        (pd.DataFrame({'a': [5.0], 'b': [6.0]}), ValDataFrame(['a'])),
        (pd.DataFrame({'a': [5.0], 'b': [6.0]}), ValDataFrame(['a'], False)),
    ]:
        rst = validate_value(value, validator, 'test')
        print(f'validate {value} by {validator}: {rst}')
