#!/usr/bin/env bash
#
# author: Vinh Nguyen
# ===================
# housekeeping file for elasticsearch cluster fo-test
#
# $1 = index and environment like fo-dev
# $2 = archive after n days
# $3 = delete after n days
#
PORT=9200
export URL="http://$1:$PORT"
echo $URL
export CATALOG_URL="$URL/_cat/indices/$1-*"
echo $CATALOG_URL

# Check that Elasticsearch is running
curl -s $URL 2>&1 > /dev/null
if [ $? != 0 ]; then
    echo "Unable to contact Elasticsearch on port $PORT."
    echo "Please ensure Elasticsearch is running and can be reached at $URL"
    exit -1
fi

# archive date
ARCHIVE_DATE=$(date -d "-$2 days" +"%Y%m%d")
# expiration date
EXP_DATE=$(date -d "-$3 days" +"%Y%m%d")
# current date
CURRENT_DATE=$(date +"%Y%m%d")

is_Index(){
    if [ $(echo $1 | grep '[0-9]') ] ; then
            return 0
    else
        return 1
    fi
}

close_Index() {
    if [ $1 -le $ARCHIVE_DATE ]; then
        echo -en "\n --close index $2 .. => ";
        curl -s -XPOST "$URL/$2/_close"
        echo -e "\n"
    fi
}

delete_Index() {
    if [ $1 -le $EXP_DATE ]; then
        echo -en "\n --delete index $2 .. => ";
        curl -s -XDELETE "$URL/$2/"
        echo -e "\n"
    fi
}

out=$(curl -s $CATALOG_URL | awk -F ' +' '{print $3}')
out=$(echo $out | tr ' ' ',')
IFS=$',' read -r -a indices <<< "$out"
unset IFS

for i in "${!indices[@]}"
do
   if is_Index ${indices[$i]}; then
      printf "%s\t%s\n" "$i" "${indices[$i]}"
      index_date=$(echo "${indices[$i]}" | tr -d '.[a-zA-Z]-')
      close_Index $index_date "${indices[$i]}"
      delete_Index $index_date "${indices[$i]}"
   else
      echo -e "\n ${indices[$i]} is not an index for housekeeping, ignore index \n"
   fi
done
