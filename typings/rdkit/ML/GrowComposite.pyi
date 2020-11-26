from rdkit.Dbase.DbConnection import DbConnect as DbConnect
from rdkit.ML import BuildComposite as BuildComposite, CompositeRun as CompositeRun, ScreenComposite as ScreenComposite
from rdkit.ML.Composite import AdjustComposite as AdjustComposite
from rdkit.ML.Data import DataUtils as DataUtils, SplitData as SplitData
from typing import Any, Optional

def message(msg: Any) -> None: ...
def GrowIt(details: Any, composite: Any, progressCallback: Optional[Any] = ..., saveIt: int = ..., setDescNames: int = ..., data: Optional[Any] = ...): ...
def GetComposites(details: Any): ...
def BalanceComposite(details: Any, composite: Any, data1: Optional[Any] = ..., data2: Optional[Any] = ...): ...
def ShowVersion(includeArgs: int = ...) -> None: ...
def Usage() -> None: ...
def SetDefaults(runDetails: Optional[Any] = ...): ...
def ParseArgs(runDetails: Any) -> None: ...