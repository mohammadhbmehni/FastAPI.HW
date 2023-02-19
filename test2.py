# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:37:38 2023

@author: mohammadhbmehni
"""
from typing import Union
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

_dict = {"Football": "A sport with foot and ball.",
        "Handball": "A sport with Hand and Ball."}


@app.get("/search/{key}")
def read_root(key:str=Query):
    _list = []
    for i in _dict:
        if key in i:
            _list.append(i)

    return _list


