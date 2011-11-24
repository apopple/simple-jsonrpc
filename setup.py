#!/usr/bin/env python
import distutils.core

distutils.core.setup(
    name = "simplejsonrpc",
    version = "0.1",
    py_modules = ["jsonrpc"],
    author = "Deng Zhiping",
    author_email = "kofreestyler@gmail.com",
    url = "https://github.com/dengzhp/simple-jsonrpc",
    license = "http://www.apache.org/licenses/LICENSE-2.0",
    description = "a simple JSON-RPC v2.0 library",
    long_description = "A python library of JSON-RPC v2.0 specification"
)
