from typing import Any

from django.contrib.gis.ptr import CPointerBase as CPointerBase

class GDALBase(CPointerBase):
    null_ptr_exception_class: Any = ...
