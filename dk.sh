#!/bin/bash
firewall-cmd --zone=public --add-port=9527/tcp--permanent
firewall-cmd --zone=public --add-port=5443/tcp --permanent
firewall-cmd --zone=public --add-port=54321/tcp --permanent
firewall-cmd --zone=public --add-port=81tcp --permanent
firewall-cmd --zone=public --add-port=8081/tcp --permanent
firewall-cmd --zone=public --add-port=6005/tcp --permanent
firewall-cmd --zone=public --add-port=29432/tcp --permanent
firewall-cmd --zone=public --add-port=6000/tcp --permanent
firewall-cmd --zone=public --add-port=6001/tcp --permanent
firewall-cmd --zone=public --add-port=22/tcp --permanent
systemctl restart firewalld.service
firewall-cmd --reload
