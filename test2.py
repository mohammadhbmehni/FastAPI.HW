# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:37:38 2023

@author: mohammadhbmehni
"""
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


