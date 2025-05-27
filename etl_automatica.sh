#!/bin/bash
cd /logstash1/anaconda3/;
source bin/activate;
python  D:/DevHitss/unir/Maestria/TFM/etl_automatica.py >> D:/DevHitss/unir/Maestria/TFM/logs/etl_automatica.log
deactivate