#-*-coding:utf-8-*-
import logging.config
import os
import sys

logging.config.fileConfig('config.ini')

def info(message):
    logging.info(message)

def error(message):
    logging.error(message)

def debug(message):
    logging.debug(message)

if __name__ == '__main__':
    info('do noting')