#!/bin/bash
#clear
#IF YOU ARE EVER HAVING TROUBLE, MAKE SURE YOU HAVE / AT END OF URI!!!
#http://localhost:8000/  <----- the / after 8000 MATTERS!!!!!!!!!! LIKE SOOOO MUCH.

#create project
#curl --data "csrfmiddlewaretoken=QX4YKZLbWnYH6RGBdcEqe6CezwHlLej1&_content_type=application%2Fx-www-form-urlencoded&_content=title%3Dt1%26author%3Da1%26wiki%3Dw1%26project_id%3D3" http://localhost:8000/create_new_project/
#update project
#curl --data "csrfmiddlewaretoken=QX4YKZLbWnYH6RGBdcEqe6CezwHlLej1&_content_type=application%2Fx-www-form-urlencoded&_content=author%3Da2%26wiki%3Dw2%26project_id%3D3" http://localhost:8000/update_project/


#get project details. specify time to get historical version.
#curl "http://localhost:8000/project_detail/?project_id=1&date=11-02-2014"


#sleep 2
echo ""

#input should be project_id, title, author, wiki, date
function create_project { #MUST HAVE SPACE BETWEEN name_of_function and {##############
    echo "creating new project with project_id=$1, title=$2, author=$3, wiki=$4 on date=$5"
    curl --data "csrfmiddlewaretoken=QX4YKZLbWnYH6RGBdcEqe6CezwHlLej1&_content_type=application%2Fx-www-form-urlencoded&_content=title%3Dt1%26author%3Da1%26wiki%3Dw1%26project_id%3D2%26date%3D09-20-2014" http://localhost:8000/create_new_project/
    echo ""
    echo ""
}

#input should be project_id date then optional arguments -t title -a author -w wiki
function update_project {
# : as the very first make silent error args.
# a means looking for option -a.
# "asd" means looking for options -a -s -d.
# "f:" means -f expects parameter which is accessed via $OPTARG
    outputString= "updating project with project_id=$1"
     #so author=a2, wiki=w2 for date $2"

    while getopts ":t:a:w:" opt; do
      case $opt in
        t)
          echo "$OPTARG" >&2
          ;;
        \?)
          echo "Invalid option: -$OPTARG" >&2
          exit 1
          ;;
        :)
          echo "Option -$OPTARG requires an argument." >&2
          exit 1
          ;;
      esac
    done




    echo "updating project so author=a2, wiki=w2 for date 09-21-2014"
    curl --data "csrfmiddlewaretoken=QX4YKZLbWnYH6RGBdcEqe6CezwHlLej1&_content_type=application%2Fx-www-form-urlencoded&_content=author%3Da2%26wiki%3Dw2%26project_id%3D2%26date%3D09-21-2014" http://localhost:8000/update_project/
    echo ""
    echo ""

}


#all steps in order. hopefully this works. cross fingers.
#echo "creating new project with project_id=2, title=t1, author=a1, wiki=w1 on date=09-20-2014"
#curl --data "csrfmiddlewaretoken=QX4YKZLbWnYH6RGBdcEqe6CezwHlLej1&_content_type=application%2Fx-www-form-urlencoded&_content=title%3Dt1%26author%3Da1%26wiki%3Dw1%26project_id%3D2%26date%3D09-20-2014" http://localhost:8000/create_new_project/
#echo ""
#echo ""

create_project 2 "t1" "a1" "w1" "09-20-2014"




echo "updating project so author=a2, wiki=w2 for date 09-21-2014"
curl --data "csrfmiddlewaretoken=QX4YKZLbWnYH6RGBdcEqe6CezwHlLej1&_content_type=application%2Fx-www-form-urlencoded&_content=author%3Da2%26wiki%3Dw2%26project_id%3D2%26date%3D09-21-2014" http://localhost:8000/update_project/
echo ""
echo ""
echo "view current version which should be (with the updates) (2, t1, w2, a2)"
curl "http://localhost:8000/project_detail/?project_id=2"
echo ""
echo ""
echo "view historical for date=09-20-2014 so should be (2, t1, w1, a1)"
curl "http://localhost:8000/project_detail/?project_id=2&date=09-20-2014"
echo ""
echo ""


#UPDATING EVEN MORE!!!
echo "updating project so title=t3 for date 09-23-2014 so result is (2, t3, w2, a2)"
curl --data "csrfmiddlewaretoken=QX4YKZLbWnYH6RGBdcEqe6CezwHlLej1&_content_type=application%2Fx-www-form-urlencoded&_content=title%3Dt3%26project_id%3D2%26date%3D09-23-2014" http://localhost:8000/update_project/
echo ""
echo ""
echo "view current version which should be (with the updates) (2, t3, w2, a2)"
curl "http://localhost:8000/project_detail/?project_id=2"
echo ""
echo ""
echo "view historical for date=09-20-2014 so should be (2, t1, w1, a1)"
curl "http://localhost:8000/project_detail/?project_id=2&date=09-20-2014"
echo ""
echo ""
echo "view historical for date=09-22-2014 so should be (2, t1, w2, a2)"
curl "http://localhost:8000/project_detail/?project_id=2&date=09-22-2014"
echo ""
echo ""



