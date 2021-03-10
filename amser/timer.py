"""
Amser: Python Timer Utility

(C) 2021 Justin Joyce.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import time

class Timer(object):
    
    def __init__(self, name="unnamed"):
        self.name = name
        self.start = 0

    def __enter__(self):
        self.start = time.perf_counter_ns()

    def __exit__(self, type, value, traceback):
        t = (time.perf_counter_ns() - self.start) / 1e9
        print(F"{self.name} took {t} seconds")
