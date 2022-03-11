export kypher="kgtk --debug query --graph-cache wikidata.sqlite3.db"
$kypher -i edgefile.tsv -o objects.tsv --match  '()-[]->(object)' --return 'distinct object as id'
$kypher -i edgefile.tsv -o subjects.tsv --match  '(subject)-[]->()' --return 'distinct subject as id'
kgtk ifnotexists --input-file objects.tsv --filter-on subjects.tsv --o objects_nosubjects.tsv
kgtk ifexists --input-file objects.tsv --filter-on subjects.tsv --o objects_subjects.tsv