#    Copyright 2023 SECTRA AB
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""Module for handling instance level objects."""

from wsidicom.instance.instance import WsiInstance
from wsidicom.instance.dataset import WsiDataset, ImageType, TileType
from wsidicom.instance.image_data import ImageData
from wsidicom.instance.image_origin import ImageOrigin
from wsidicom.instance.wsidicom_image_data import WsiDicomImageData
from wsidicom.instance.pillow_image_data import PillowImageData
