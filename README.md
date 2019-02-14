# LetsMeet
Let's Meet is a social web site which aims to organize events easier. This project is an assignment for Sofware Engineering Concepts lecture.


![](https://lh6.googleusercontent.com/ofuWr7rtq0wufSLp17sfTc4CX3Ubh8dNCvJYLlb6BEWHBIOrNME5uMgdV9NnLYRiPDPQ4obRuYTs3Otf6yBzdsJdn6QHpYQ_Bbf6bfGlUVEn8idkVrkBlqGcPcc6OGYVmT-_q190)

----------

![](https://lh4.googleusercontent.com/M5gsYC6xSD4R9IM9H-Wy04pFLA8I79Z-HcK54D7xT9TCfpkpvWYNu43WBUd_Za9sxk_DJ5FG6nIDC09oG6WJ5loEySWw2CEz5mP_zlhPVjiinrkvRl_zKIBIWm7lVkdD5ve5kin5)

----------

![](https://lh5.googleusercontent.com/juZhuV9X8qFtmGkZ7GO_yZXaskIdUchNNCjF4l9m5DZtKDaMIgeCRIb3f2jpj9BeiiOHO2G9mYOFBz2QWh73fYDkdxLsWFzGd1su_vgIlLf0T8FnArMi_LAm4sc-Woamxz_yr58i)

Prepared by:

İbrahim Doğan - 11512112

Burak Demirel - 115200034

Engin Can Höke - 116202067

Recep Goger - 114200078

Kadir Akgül - 115200081

  

Semester: Fall 2018

  

Course: Software Engineering Consepts

  

Instructed by Pınar Hacıbeyoğlu

![](https://lh5.googleusercontent.com/fi5dhx0gZg9YgUoRdwCV-FiJX0dh8TzmkbwGrZIRhIWUjyN14F3mFPo9yfBZSqf7Jhk1SbUDwQW-zJW8BqneSd4YRpUjeuv1vOEVBikeQe3HFef5Gqrjm_UoN0H4HorrwHpEikff)

  

## Aim of the project

The aim of our project is to make it easier for people to meet each other in daily life. The members will share the activities they are going to do, and their friends will say whether they will join it or not.

## Roles of members

-   İbrahim Doğan (Design & Programming)
    
-   Burak Demirel (Tester)
    
-   Engin Can Höke (UI Design)
    
-   Recep Goger (Documentation)
    
-   Kadir Akgül (Analysis & Programming)
    

## Detailed timeline

1.  Analysis : 27-30 November
    
2.  Design  : 1-3 December
    
3.  Programming: 3-15 December
    
4.  UI Design: 4-15 December
    
5.  Testing : 7-16 December
    
6.  Documentation & Presentation : 10-16 December
    

![](https://lh6.googleusercontent.com/hgszLVwC26IqadU7WzE1bmKuZb2mbFDmfTAHS0Ks7aBOPxlvwgMhHxiVR-Pw-MfXOOq9coLx5GDPy8ezgNWm01AVn-JMc_M2r5Fez1799UPHac1Y7JMdJDbq4e400kVjV4U1krjE)

  

## Structure of system

The project is web application which is based on Python/Django Library. In Django, every application is called ‘Project’. Inside a project the modules called ‘app’. So we have ‘LetsMeet’ project and inside of it we have ‘main’ app which includes our web application. If we want to add ‘blog’ module in the future we are going to just create ‘blog’ app inside our ‘LetsMeet’ project.

  

Like every web application the django uses ‘Model View Controller’ structure. The Django project has urls.py which controlls every route value and redirects the request from route to controller. eg: example.com/events after / we see ‘events’ so our route is ‘event’ and it calls to views.events function which is act like controller. After the function call the request the view will be prepared for logged in user and shows the rendered page to the user.

## Structure of DB

Django has its own User Model. The Profile is extended version of User Model.


  

![](https://lh3.googleusercontent.com/nChX01YtJS6SoZVgxImWdf9bvDWLaxOXuPJ8raF7L9z_UZRjsEH3dTPeU1_HnK42cw1I_uxva5nlwgS491RO7MQ1y5smIYEUb7eboq7LW99cdFyHpDY48fSYjQ5SAseCfdiS2ah-)

  
    

## Future works

-   ## Commenting system can be added to the events. Users have to have a permit that allows them to comment positively or negatively.
    
-   ## Users can share their photos in past event on their profile and another users can like or dislike them. Like any kind of social media.
    
-   ## The “ Discovery” system also can be added. When any user create an event , there is a choice that allows the other user can see or not. Then in the discovery section all users can see available events.
    

  
  
  
  
  
  
  
  
  
  
  
  
  

## Software development tolls or platforms

[https://trello.com/b/uj4zRKT5/lets-meet](https://trello.com/b/uj4zRKT5/lets-meet)

[https://github.com/dedinededin/LetsMeet](https://github.com/dedinededin/LetsMeet)

  

![](https://lh3.googleusercontent.com/kMgxoqdg4H0o4dK8AOtxELFEiUAi0FHDgMU117BuQGzNo7DVOQpPL05PqRJKS331Z0vt_LgvJB4VpNb767kTgaEoKwdhJzFOjKqCg8lYYOTNrcOpU1I3E5fFXAQ5EMCqPpsvTBg4)

  
  
  
  
  
  
  
  
  
  
  
  
 

  

## Screen shots![](https://lh4.googleusercontent.com/IMJAzcmoPoWl_9SFCgrsjZZB8Qnw2DkNM7p-QpNvAEXHOR-yt0Jzwh1C_nzw9IxW1ifQTdr37V693_5QKTs33t7LLRb-R9VYS_oGxCnBoqnii2slNi7GAxwPCz6OwMbOudvBg4fK)![](https://lh5.googleusercontent.com/3-k3YV0kbTfAshK9q8Gb1pyg6wz4jvjbJMKvz7KxIf0ubYbUIsU0VtKegIPJU6RM-yV3zkaTU1pvmqC9K3t9jod2l1HnQSRwra5g7Easukn1UKcxXmd5ZvKYbMiuO84c9r45sLpQ)![](https://lh6.googleusercontent.com/NksUkmYMmz-T08L3Z6Yj9xUCt9t7S3oo9Zqsu13SxzfWNs0VgU5ZasVf99bTgM9ps5sNja0jHweDmZ8EbQfSpBufHhzduf8u8W1G6YFSlxGwBc24e0Yk8TaOFvSgPDRu5u7ktyfO)![](https://lh6.googleusercontent.com/Opj1dkRSKmLhEpW2cW6uxbZZnkvsR9jKv84d-sI9j4gfOW6Gmbbn0zCdeOgFNzAJFWQhgTJUS9x1HL9oieZWKCaCcDS92nQWH9ZjhaoH-h-iiFEwjnpXiyym3TptcHnH3gUbVcCl)![](https://lh3.googleusercontent.com/sgLUu75It3Qu4-LJPpQF7riqXfZ2O-KalTPFDngxN6R6JdE80jBWDyixZruZ7rCNdornnyduWhYMkfsJMN64Ve2Qnva1amXHAr5I0Oq5c8rcoUEpagB855uEMLRJE54XbzSqjQW4)![](https://lh6.googleusercontent.com/ApvP6CKTwrPz6jvsa4gSJQlg80cnPI81izzQBpDJmk12mCbwCXYF8-uK3AM6SEhliQ4Y3THgWvhjZYf4_t1YDAkZPTfkJWOwNh8QvKdy9lZyftmQn2xAjjSrW5sjZh2B1DwGieI7)![](https://lh6.googleusercontent.com/LPh4YJzQoiLYuOOdx5FW7UiynWdp6iPUDwpU0vcPvK9AnPYyw-6hA8hbYExaObxzwoqrEQVGUPXWwXsRVMFHbYDpZjOMVwC8p7pztodVFzkRXThISUFSXIGfrhc5awpSKTL7n3zZ)![](https://lh4.googleusercontent.com/vSI2_ilA1M3aD-7nUDt-amLlfY91Wvjfp40BM7a4yQ8GCFPUilcsv_trzG2Ed6aDpM7Jj5wQzJL1sinhzGB6D5BdWiQU5c-d6PSBncQdgXD9U29QSTdohVrcilBXO0I_bVI5fhpV)

## Resources

  

(n.d.). Retrieved from http://www.kennethcachia.com/plain-pattern/app/

Advanced Django Models - Python Django Tutorials. (n.d.). Retrieved from https://djangobook.com/advanced-models/

Best Free Pattern Generators for Designers - 27 to Choose From. (n.d.). Retrieved from https://www.whoishostingthis.com/resources/pattern-generators/

Bootstrap. (n.d.). Start Bootstrap. Retrieved from https://startbootstrap.com/

Bootstrap 3 Registration Form with Validation. (n.d.). Retrieved from https://codepen.io/juff03/pen/OXaXRG

Buildwithpython. (2018, September 07). Django 2.1 - Creating a Django App (StartApp) - 3/14. Retrieved from https://www.youtube.com/watch?v=ck8XDGnM2aA

D'Avignon, D. (2018, April 16). Django 2.0 - Make clicked tab active with Bootstrap. Retrieved from https://medium.com/@dustindavignon/django-2-0-make-clicked-tab-active-with-bootstrap-de27a74f6b76

Django template: Check for empty query set. (n.d.). Retrieved from https://stackoverflow.com/questions/17435233/django-template-check-for-empty-query-set

Django url pattern - string parameter. (n.d.). Retrieved from https://stackoverflow.com/questions/11894916/django-url-pattern-string-parameter

Django: How to Extend The User Model (aka Custom User Model). (2018, October 26). Retrieved from https://wsvincent.com/django-custom-user-model-tutorial/

Documentation. (n.d.). Retrieved from https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.exists

Goodridge, M. (2017, January 10). How to Upload and Display a Profile Picture in Django Development (Django Tutorial) | Part 36. Retrieved from https://www.youtube.com/watch?v=tT2JOpfelSg

HTML Snippets for Twitter Boostrap framework. (n.d.). Retrieved from https://bootsnipp.com/snippets/aMNV3

HTML Snippets for Twitter Boostrap framework. (n.d.). Retrieved from https://bootsnipp.com/snippets/56ExR

Printed, P. (2018, January 16). Django Authentication Basics. Retrieved from https://www.youtube.com/watch?v=dBctY3-Z5hY

Schafer, C. (2018, August 31). Python Django Tutorial: Full-Featured Web App Part 8 - User Profile and Picture. Retrieved from https://www.youtube.com/watch?v=FdVuKt_iuSI

The QuerySet value for an exact lookup must be limited to one result using slicing-Django. (n.d.). Retrieved from https://stackoverflow.com/questions/50431810/the-queryset-value-for-an-exact-lookup-must-be-limited-to-one-result-using-slici?noredirect=1&lq=1

Vitorfs. (2016, July 21). How to Extend Django User Model. Retrieved from https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

Vitorfs. (2017, February 18). How to Create User Sign Up View. Retrieved from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

Young, M. (n.d.). Image hover effects. Retrieved from https://miketricking.github.io/bootstrap-image-hover/
