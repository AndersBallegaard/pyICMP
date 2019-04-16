#!/bin/sh

#install dev version from current branch
pip3 install .

#run pytest
pytest test/