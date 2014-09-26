#!/bin/bash
clear
#create project
curl --data "csrfmiddlewaretoken=QX4YKZLbWnYH6RGBdcEqe6CezwHlLej1&_content_type=application%2Fx-www-form-urlencoded&_content=title%3Dt1%26author%3Da1%26wiki%3Dw1%26project_id%3D3" http://localhost:8000/create_new_project/
#update project
curl --data "csrfmiddlewaretoken=QX4YKZLbWnYH6RGBdcEqe6CezwHlLej1&_content_type=application%2Fx-www-form-urlencoded&_content=author%3Da2%26wiki%3Dw2%26project_id%3D3" http://localhost:8000/update_project/

