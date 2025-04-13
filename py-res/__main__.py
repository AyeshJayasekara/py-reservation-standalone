import json
import logging as log
import os
from pathlib import Path

import config
import cli
import gui
from tkinter import *

# pyinstaller --onefile --noconsole --paths=subfolder __main__.py

root_directory = str(os.getcwd()) + "/data"
if not os.path.exists(root_directory):
    os.makedirs(root_directory)

log.basicConfig(
    encoding="utf-8",
    level=log.INFO,
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    handlers=[
        log.FileHandler(str(os.getcwd()) + "/data/app.log"),
        log.StreamHandler()
    ]
)

log.info("STARTING APPLICATION >> ")

# Opening JSON file
config_file = open(os.getcwd() + '/data/config.json')

# Load initial configurations to object
config_parameters = json.load(config_file)

log.info('------  USING CONFIG PARAMETERS -------')
log.info(config_parameters)
log.info('------  ----------------------- -------')

# Getting the list of directories
# data_directory = os.listdir(str(Path.home()) + config_parameters['data_folder'])
data_directory = os.listdir(os.getcwd() + config_parameters['data_folder'])
# data_directory = os.listdir( config_parameters['data_folder'])

# Checking if the list is empty or not
database = None

if not any(fname.endswith('.db') for fname in data_directory):
    log.warning("EMPTY DATA FOLDER DETECTED >>> PREPARING FOR INITIAL STARTUP!")
    database = config.Database(log, config_parameters, True)
else:
    database = config.Database(log, config_parameters, False)
    print("EXISTING DATA FOLDER >> PROCEEDING")

if config_parameters['interface'] == "cli":
    log.info("EXECUTION MODE: CLI [SELECTED] STARTING CLI APPLICATION ")
    log.info("STARTING CLI APPLICATION >> ")
    cli.Cli(config_parameters, database)
else:
    log.info("EXECUTION MODE: GUI [SELECTED] STARTING GUI APPLICATION ")
    log.info("STARTING GUI APPLICATION >> ")
    root = Tk()
    w = Label(root, text='Reservations Application')
    gui.Gui(root, config_parameters)








