#!/bin/bash

PASSWORD_FILE="ID.txt"


PASSWORD=$(base64 --decode < "$PASSWORD_FILE")

SSH_USER="esd-user"  
SSH_HOST="172.16.20.25" 


sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no "$SSH_USER"@"$SSH_HOST" 'sudo reboot'

echo "Commande de redémarrage envoyée au serveur."
