# Copyright 2022 The Numaproj Authors.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class ModelInitializationError(Exception):
    pass


class ModelNotFoundError(Exception):
    pass


class InvalidRangeParameter(Exception):
    pass


class LayerSizeMismatchError(Exception):
    pass


class DataModuleError(Exception):
    pass


class InvalidDataShapeError(Exception):
    pass


class UnknownConfigArgsError(Exception):
    pass


class ModelVersionError(Exception):
    pass


class RedisRegistryError(Exception):
    pass


class ModelKeyNotFound(RedisRegistryError):
    pass
