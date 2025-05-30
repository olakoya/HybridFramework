#!/bin/bash
source .venv/bin/activate
.venv/bin/python -m pytest -s -v -m "sanity" --browser chrome testCases.py


