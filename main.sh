echo 'starting.'
sleep 0.2
clear
echo 'starting..'
sleep 0.2
clear
echo 'starting...'
sleep 0.2
clear
echo 'starting....'
sleep 0.2
clear
echo 'starting.'
sleep 0.2
clear
echo 'starting..'
sleep 0.2
clear
echo 'starting...'
sleep 0.2
clear
echo 'starting....'
clear
echo 'write help if you need help'
read -p "enter a command: " command
if [ "$command" == "help" ]
then
    echo 'commands:'
    echo 'exit'
    echo 'update'
    echo 'start'
elif [ "$command" == "exit" ]
then
    exit
elif [ "$command" == "update" ]
then
    bash update.sh
    read -p "enter a command: " command
elif [ "$command" == "start" ]
then
    python3 notepad.py
else
    echo "invalid command"
    read -p "enter a command: " command
fi
    
