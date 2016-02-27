# E.A.T. School Lunch UX Challenge

This is my entry for the [E.A.T. School Lunch UX Challenge](http://lunchux.devpost.com/)

## How to use

Start an application [http://kaulgud.webfactional.com/eat/](http://kaulgud.webfactional.com/eat/)

Admin Interface [http://kaulgud.webfactional.com/eat/admin/dashboard](http://kaulgud.webfactional.com/eat/admin/dashboard)


Username: admin

Password: lunch123


## Technologies used

### Python Django (Frontend)
Django is a robust [Python Web framework](https://www.djangoproject.com) that encourages rapid development and clean, pragmatic design. It takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s *free, open source, fast, secure and exceedingly scalable*.

#### Installing Django
Django has an awesome tutorial on how to get started [https://www.djangoproject.com/start/](https://www.djangoproject.com/start/)


### SQLite (Backend)
[SQLite](https://www.sqlite.org/) is free opensource, self-contained, serverless, zero-configuration, transactional SQL database engine. SQLite is the most widely deployed database engine in the world. In this website it holds all the user and application data. As per the SQLite documentation its pretty robust however for applications like this where the number of records could grow very large, its recomemded to use a powefull RDBMS like Oracle or SQL Server, thankfully in Django it's pretty easy to switch databases.


## Design considerations for better user experience

1. Registration and Login

	Ability to save incomplete application is a very significant feature for the overall user experience of this type of application, especially important for the scenario where users have to enter the entire household information along with earnings. Typically  users are not fully prepared when they start filling out the application. Even if we present a beautiful set of instructions for every section in the application before hand, let's just face it, 95% of them will never read it. Most probably they will jump right in and try to figure it out as they go. The best user experience is to let them do just that by making the application intuitive. However in such type of applications even if we make it as intuitive as possible users will still be stuck, especially in the earnings section where they wont be sure exactly what amount to put. They might want to look it up somewhere, which might take anywhere from few minutes to days. A login system will allow them to pause and come back when they have the required information and finish rest of the application.

2. For return users provide the ability to jump right to the place where they left

	If a users logs out of the system and comes back later a way to remind them where they were when they left and take them back to that point.

3. Contextual help tips

	Show help tips related to the current page instead of having an exhaustive set of instructions on a single page. Users will read help tips shown right where they need them.  

4. Review Page

	Create a separate page to display the complete application, so that the user can glance over all the inforamtion entered by them  quickly.
