#!/bin/bash
set -e

# colors
RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'

function run(){
  local DETACH=$2

  echo -e "${RED}Running whole app by docker-compose.yml in root dir...${NC}"
  echo -e "${GREEN}RUNNING \"docker-compose build\"...${NC}"
  docker-compose build
  echo -e "${GREEN}RUNNING \"docker-compose up\"...${NC}"
  if [ ! -z "${DETACH}" ]; then
    docker-compose up "${DETACH}"
  else
    docker-compose up
  fi
}

if [[ $1 == "run" ]]; then
  if [[ $2 == "-d" ]]; then
    run $2 "--detach"
  else
    run
  fi
  exit 0
fi