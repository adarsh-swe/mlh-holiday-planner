indexres=$(curl -f -s 'https://holidayplanner.tech' && echo "Test: Index page success" || echo "Test: Index page failed to load")
indexres=$(echo $indexres | sed 's/^.*Test/Test/')
echo $indexres