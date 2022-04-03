# blog-search-api 🚀
This is a API which serves blog post based on the user input Query.
## Technologies <img src="https://user-images.githubusercontent.com/52165188/161188781-a81fc693-3f13-455d-8b71-185c356852c8.gif" height=20 width=20 >

A list of technologies used within the project:
* 🔍[ElasticSearch](https://www.elastic.co/downloads/past-releases/elasticsearch-7-17-1): Version 7.17.1
* 🌐[Django REST Framework](https://www.django-rest-framework.org/): Version 3.13.1
* 🐍[Python](https://www.python.org/): Version 3.8
* 🐧[Ubuntu](https://ubuntu.com/download/desktop): Version 18.04.6 LTS
* 🔍[elasticSearch](https://elastic.co/downloads/elasticsearch/): Version 7.17.1
* 🔥[HayStack](https://pypi.org/project/django-haystack/): Version 3.1.1

## Installation <img src="https://user-images.githubusercontent.com/52165188/161188962-6e47aecf-dc0f-4631-9d06-04ef64f44e51.gif" height=20 width=20 >

##### In a Seprate Folder first install ElasticSearch 
```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.17.1-amd64.deb
sudo dpkg -i elasticsearch-7.17.1-amd64.deb
sudo rm -r elasticsearch-7.17.1-amd64.deb
sudo service elasticsearch start
```
Clone Repo & Setup Enviroment 🌿
```
$ git clone https://github.com/sauravsharmaz/blog-search-api.git
$ cd blog-search-api
$ sudo apt update
$ sudo apt-get install python3.8-venv python3-dev
$ python3.8 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ ./manage.py migrate blog
$ ./manage.py createsuperuser
$ ./manage.py runserver
```

## Collaboration 👨‍💻
#### Working on a repository
For most multi-contributor projects we use [GitHub pull requests](https://guides.github.com/activities/forking/#making-a-pull-request) as the workflow for contributions/code review.

We recommend the following steps for getting started with a code repository 🪜

* In the GitHub UI, [fork the main repository](https://help.github.com/articles/fork-a-repo/) to your own account.
* Add your fork of the repository as the origin
  ``` bash
  clone the forked dir
  cd blog-search-api
  ```

Do all of your work in this fork, make a bunch of commits, push frequently, etc. Once a feature is done, use the GitHub UI to create a pull request from your fork to the upstream repository, so that it may be code reviewed.

## Connect with me on <img src="https://user-images.githubusercontent.com/52165188/161188452-7569d87f-6173-413a-8767-4d88817c649c.gif" width=20 height=20 >
   * <img src="https://user-images.githubusercontent.com/52165188/161187887-e8e58094-2627-4403-9ad1-db9de1a77b85.gif" width=20 height=20 > <a href="https://twitter.com/sauravs19399515" target="_blank">Twitter</a>
   * 📨 [Saurav Sharma](mailto:saurav.sharma.zz445@gmail.com)
