#!/bin/bash

firewall-cmd --zone=public --add-port=6000/tcp --permanent
firewall-cmd --zone=public --add-port=6001/tcp --permanent
systemctl restart firewalld.service
firewall-cmd --reload
