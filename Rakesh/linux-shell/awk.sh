awk '{
if ($3 =="" || $4 == "" || $5 == "")
	print "Some score for the student",$1,"is missing";'
}' awk.txt
