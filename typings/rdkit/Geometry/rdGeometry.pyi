import Boost.Python

def ComputeDihedralAngle(*args, **kwargs) -> Any: ...
def ComputeGridCentroid(*args, **kwargs) -> Any: ...
def ComputeSignedDihedralAngle(*args, **kwargs) -> Any: ...
def FindGridTerminalPoints(*args, **kwargs) -> Any: ...
def ProtrudeDistance(*args, **kwargs) -> Any: ...
def TanimotoDistance(*args, **kwargs) -> Any: ...
def TverskyIndex(*args, **kwargs) -> Any: ...
def UniformGrid3D(*args, **kwargs) -> Any: ...
def WriteGridToFile(*args, **kwargs) -> Any: ...

class Point2D(Boost.Python.instance):
    __instance_size__: Any = ...
    __safe_for_unpickling__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def AngleTo(self, *args, **kwargs) -> Any: ...
    @classmethod
    def DirectionVector(self, *args, **kwargs) -> Any: ...
    @classmethod
    def DotProduct(self, *args, **kwargs) -> Any: ...
    @classmethod
    def Length(RDGeom) -> Any: ...
    @classmethod
    def LengthSq(RDGeom) -> Any: ...
    @classmethod
    def Normalize(RDGeom) -> Any: ...
    @classmethod
    def SignedAngleTo(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __add__(self, other) -> Any: ...
    @classmethod
    def __getinitargs__(RDGeom) -> Any: ...
    @classmethod
    def __getitem__(RDGeom, int) -> Any: ...
    @classmethod
    def __iadd__(boost, RDGeom) -> Any: ...
    @classmethod
    def __idiv__(RDGeom, double) -> Any: ...
    @classmethod
    def __imul__(RDGeom, double) -> Any: ...
    @classmethod
    def __isub__(boost, RDGeom) -> Any: ...
    @classmethod
    def __len__(RDGeom) -> Any: ...
    @classmethod
    def __mul__(RDGeom, double) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @classmethod
    def __sub__(self, other) -> Any: ...
    @classmethod
    def __truediv__(RDGeom, double) -> Any: ...
    @property
    def x(self) -> Any: ...
    @x.setter
    def x(self, val: Any) -> None: ...
    @property
    def y(self) -> Any: ...
    @y.setter
    def y(self, val: Any) -> None: ...

class Point3D(Boost.Python.instance):
    __instance_size__: Any = ...
    __safe_for_unpickling__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def AngleTo(self, *args, **kwargs) -> Any: ...
    @classmethod
    def CrossProduct(self, *args, **kwargs) -> Any: ...
    @classmethod
    def DirectionVector(self, *args, **kwargs) -> Any: ...
    @classmethod
    def Distance(self, *args, **kwargs) -> Any: ...
    @classmethod
    def DotProduct(self, *args, **kwargs) -> Any: ...
    @classmethod
    def Length(RDGeom) -> Any: ...
    @classmethod
    def LengthSq(RDGeom) -> Any: ...
    @classmethod
    def Normalize(RDGeom) -> Any: ...
    @classmethod
    def SignedAngleTo(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __add__(self, other) -> Any: ...
    @classmethod
    def __getinitargs__(RDGeom) -> Any: ...
    @classmethod
    def __getitem__(RDGeom, int) -> Any: ...
    @classmethod
    def __iadd__(boost, RDGeom) -> Any: ...
    @classmethod
    def __idiv__(RDGeom, double) -> Any: ...
    @classmethod
    def __imul__(RDGeom, double) -> Any: ...
    @classmethod
    def __isub__(boost, RDGeom) -> Any: ...
    @classmethod
    def __len__(RDGeom) -> Any: ...
    @classmethod
    def __mul__(RDGeom, double) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @classmethod
    def __sub__(self, other) -> Any: ...
    @classmethod
    def __truediv__(RDGeom, double) -> Any: ...
    @property
    def x(self) -> Any: ...
    @x.setter
    def x(self, val: Any) -> None: ...
    @property
    def y(self) -> Any: ...
    @y.setter
    def y(self, val: Any) -> None: ...
    @property
    def z(self) -> Any: ...
    @z.setter
    def z(self, val: Any) -> None: ...

class PointND(Boost.Python.instance):
    __instance_size__: Any = ...
    __safe_for_unpickling__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def AngleTo(self, *args, **kwargs) -> Any: ...
    @classmethod
    def DirectionVector(self, *args, **kwargs) -> Any: ...
    @classmethod
    def Distance(self, *args, **kwargs) -> Any: ...
    @classmethod
    def DotProduct(self, *args, **kwargs) -> Any: ...
    @classmethod
    def Length(RDGeom) -> Any: ...
    @classmethod
    def LengthSq(RDGeom) -> Any: ...
    @classmethod
    def Normalize(RDGeom) -> Any: ...
    @classmethod
    def __add__(self, other) -> Any: ...
    @classmethod
    def __getinitargs__(RDGeom) -> Any: ...
    @classmethod
    def __getitem__(RDGeom, int) -> Any: ...
    @classmethod
    def __getstate__(RDGeom) -> Any: ...
    @classmethod
    def __iadd__(boost, RDGeom) -> Any: ...
    @classmethod
    def __idiv__(RDGeom, double) -> Any: ...
    @classmethod
    def __imul__(RDGeom, double) -> Any: ...
    @classmethod
    def __isub__(boost, RDGeom) -> Any: ...
    @classmethod
    def __len__(RDGeom) -> Any: ...
    @classmethod
    def __mul__(RDGeom, double) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...
    @classmethod
    def __setitem__(RDGeom, int, double) -> Any: ...
    @classmethod
    def __setstate__(RDGeom, boost) -> Any: ...
    @classmethod
    def __sub__(self, other) -> Any: ...
    @classmethod
    def __truediv__(RDGeom, double) -> Any: ...

class UniformGrid3D_(Boost.Python.instance):
    __instance_size__: Any = ...
    __safe_for_unpickling__: Any = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def CompareParams(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetGridIndex(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetGridIndices(RDGeom, unsignedint) -> Any: ...
    @classmethod
    def GetGridPointIndex(self, *args, **kwargs) -> Any: ...
    @classmethod
    def GetGridPointLoc(RDGeom, unsignedint) -> Any: ...
    @classmethod
    def GetNumX(RDGeom) -> Any: ...
    @classmethod
    def GetNumY(RDGeom) -> Any: ...
    @classmethod
    def GetNumZ(RDGeom) -> Any: ...
    @classmethod
    def GetOccupancyVect(RDGeom) -> Any: ...
    @classmethod
    def GetOffset(RDGeom) -> Any: ...
    @classmethod
    def GetSize(RDGeom) -> Any: ...
    @classmethod
    def GetSpacing(RDGeom) -> Any: ...
    @classmethod
    def GetVal(RDGeom, unsignedint) -> Any: ...
    @classmethod
    def GetValPoint(self, *args, **kwargs) -> Any: ...
    @classmethod
    def SetSphereOccupancy(self, *args, **kwargs) -> Any: ...
    @classmethod
    def SetVal(self, *args, **kwargs) -> Any: ...
    @classmethod
    def SetValPoint(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __getinitargs__(RDGeom) -> Any: ...
    @classmethod
    def __iadd__(boost, RDGeom) -> Any: ...
    @classmethod
    def __iand__(boost, RDGeom) -> Any: ...
    @classmethod
    def __ior__(boost, RDGeom) -> Any: ...
    @classmethod
    def __isub__(boost, RDGeom) -> Any: ...
    @classmethod
    def __reduce__(self) -> Any: ...